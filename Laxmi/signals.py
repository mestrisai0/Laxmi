from django.db.models.signals import post_save, pre_delete, pre_save, post_delete
from django.dispatch import receiver, Signal
from .models import *
from django.contrib.auth.models import User
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync
import datetime
from datetime import date, timedelta
from django.db import transaction
import json
from django.utils import timezone
from .helper_func import noti_to_consumer
# from django.core.serializers.json import DjangoJSONEncoder
# import getpass


# @receiver(post_save, sender=PunchTable)
# def punch_created_send_noti(sender, instance, created, using, **kwargs):
#     print("Inside creation code")
#     if created:
#         new_noti = Messages.objects.create()

#         subject = 'Punch Created'
#         text = f'Punch created of size {instance.punch_no} by user kaustubh at location {instance.location.location_name}'
#         color_class = 'notification_success'

#         new_noti.subject = subject
#         new_noti.text = text
#         new_noti.color_class = color_class

#         new_noti.save()

#         noti_to_consumer(color_class, text, subject)

#         print("completed orders save")