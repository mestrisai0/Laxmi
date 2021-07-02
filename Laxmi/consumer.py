import datetime
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json
from .models import *
class AlertSystem(WebsocketConsumer):
    def connect(self):
        self.room_name = "test_consumer"
        self.room_group_name = "test_consumer_group"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({'status':'connected from django channels'}))

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,{
        #         'type': 'run',
        #         'payload': text_data
        #     }
        # )
        print(text_data_json)
        
        self.send(text_data=json.dumps({'status':'we got you'}))


    def disconnect(self, *args , **kwargs):
        print('disconnected')

    def send_notification(self, event):
        print('alert notification')
        data = json.loads(event.get('value'))
        print(f'data in consumer {data}')
        self.send(text_data=json.dumps({'noti_receive':data}))
        print('alert notification')


class UserAlert(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']
        self.room_group_name = "room_%s" % self.room_name
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        # reg = Register.give_noti_detail(self.room_name)
        # print(reg)
        self.accept()
        self.send(text_data=json.dumps({'payload':'connected on user side'}))
    def receive(self,text_data):
        text_data_json = json.loads(text_data)
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,{
        #         'type': 'run',
        #         'payload': text_data
        #     }
        # )
        print(text_data_json)
        
        self.send(text_data=json.dumps({'status':'we got your msg from admin'}))
        # async_to_sync(self.channel_layer.group_send)(
        #     self.room_group_name,
        #     {
        #         'type': 'send_alert_user',
        #         'payload': text_data
        #     }
        # )
    def disconnect(self,close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        print('disconnected')
    def send_alert_user(self, event):
        print('alert notification')
        # print(event['value'],'@@@@')
        try:
            print(event.get('value'),'sdksdkd')
            data = json.loads(event.get('value'))
            # print(f'data in consumer {data}')
            self.send(text_data=json.dumps({'payload':data}))
            print('alert notification')
        except:
            pass