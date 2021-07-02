from .models import *
import datetime
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json
from django.utils import timezone
from django.core.serializers.json import DjangoJSONEncoder
from django.core.mail import EmailMessage
from datetime import date, timedelta
from django.db.models import Q

def client_name_product_helper(request):
    new_client_name = request.POST['client']

    if not ClientName.objects.filter(client_name=new_client_name).exists():
        save_new = ClientName.objects.create(client_name=new_client_name)
        save_new.save()

    new_client_product = request.POST['product']
    temp = ClientName.objects.get(client_name=new_client_name)

    if not ClientProduct.objects.filter(
        product_name=new_client_product, client_code=temp
    ).exists():
        new_id = ClientName.objects.get(client_name=new_client_name)
        print(new_id)
        save_product = ClientProduct.objects.create(
            product_name=new_client_product, client_code=new_id)
        save_product.save()

    temp2 = ClientProduct.objects.get(product_name=new_client_product)


    return temp2, temp, new_client_product



def common_notification_model_fetch(request):

    all_ms = Messages.objects.filter(notify_user=request.user).order_by("-id")
    ms_count = str(Messages.objects.filter(Q(notify_user=request.user) & Q(seen__exact='False')).count())

    return all_ms, ms_count

def create_notification(subject, text, color_class, created_by, notify_user):
    new_noti = Messages.objects.create()    

    new_noti.subject = subject
    new_noti.text = text
    new_noti.color_class = color_class
    new_noti.created_by = created_by
    new_noti.notify_user = notify_user
    new_noti.save()


def common_task_func(orr, punch_or_plate, no_of_day_to_next_alert):

    

    if punch_or_plate == 'punch':
        check_alert = orr.punch_alert_date
        order_color = orr.punch_color
        status_check = orr.punch_status
    else:
        check_alert = orr.plate_and_positive_alert_date
        order_color = orr.plate_color
        status_check = orr.plate_status

    if date.today() == check_alert:

        no_of_day = (orr.order_date.date() - date.today()).days
        client_name = orr.client_product_id.client_code.client_name
        client_product = orr.client_product_id.product_name

        if status_check == 'Send Order':
            subject = 'Send Order'
            text = f'Its been {no_of_day} and you have still not send order for {client_product} of {client_name}'
        else:
            subject = 'Punch in Progress'
            text = f'You have send punch to be made for {client_product} of {client_name}'

        color_class = 'notification_danger'

        create_notification(subject, text, color_class, None, 'admin')
        body = text
        subject = subject
        sender_mail = 'lakshit.ukani@datenwissen.com'
        email = EmailMessage(subject,body,'Kaustubh Mestri',[sender_mail])
        email.send()
        check_alert = (date.today()+timedelta(days=no_of_day_to_next_alert)).isoformat()

        if no_of_day > 3:
            order_color = 'danger'

        orr.save()



def noti_to_consumer(color_class, text, subject):
    print(color_class, subject, text)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "test_consumer_group" , {
            'type' : 'send_notification',
            'value' : json.dumps({
                'color_class': color_class,
                'text': text,
                'subject': subject,
                'date': timezone.now()
            }, cls=DjangoJSONEncoder)
        }
    )