from celery import shared_task
from celery import Celery
from .models import *
from django.core.mail import EmailMessage
from datetime import date, timedelta
from .helper_func import *

#run code is: celery -A LaxmiIndustries.celery worker --loglevel=info --pool=solo
# celery -A LaxmiIndustries beat -l info
# celery -A apexindustries purge
@shared_task
def send_mail():
    ord = OrderDetail.objects.values()
    current_date = str(date.today())
    print(current_date,'current date')
    st = ''
    for i in ord:
        sid = i['id']
        punch_alert_date = str(i['punch_alert_date'])
        plate_and_positive_alert_date = str(i['plate_and_positive_alert_date'])
        orr = OrderDetail.objects.get(id = sid)
        punch_status = i['punch_status']
        plate_status = i['plate_status']

        if punch_status == 'Available': 
            orr.punch_alert_date =  None
            orr.punch_color = 'success'
        else:
            common_task_func(orr, 'punch', 1)      
        
        if plate_status == 'Available':
            orr.plate_and_positive_alert_date =  None
            orr.plate_color = 'success'
        else:
            common_task_func(orr, 'plate', 1)      

    return 'sent'

