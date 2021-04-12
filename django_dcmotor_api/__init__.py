from . import mqttClient
# from threading import Thread

# class Nama:
#     def connect(self):
#         self.mqttClient.client.loop_forever()

#     clientloop_thread = Thread(target=self.connect)
#     clientloop_thread.start()



mqttClient.client.loop_start()
# mqttClient.client.loop_forever()