import datetime
from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer
from .models import DataDevice,Device

class MqttConsumer(SyncConsumer):

    def mqtt_sub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        x = payload
        # print(x)
        if 'temp_air' in x:
            save_model = DataDevice(ph=x['ph'],tds=x['tds'],ec=x['ec'],temp_air=x['temp_air'],temp_udara=x['temp_udara'],turb=x['turb'],alat=Device.objects.get(id=x['alat']))
            save_model.save()
            print("topic: {0}, payload: {1}".format(topic, x))
        else:
            print('Tidak masuk database')

    def mqtt_pub(self, event):
        topic = event['text']['topic']
        payload = event['text']['payload']
        # do something with topic and payload
        print("topic: {0}, payload: {1}".format(topic, payload))
