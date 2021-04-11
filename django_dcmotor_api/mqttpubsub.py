import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(" masuk connect ")
    # client.subscribe("statl")
    client.publish("statl", "132ldkflkajsdhf")
    # client.publish("statl", "aasldkflkajsdhf", qos=0, retain=False)

def on_message(client, userdata, msg):
    print(" Halo Masuk On Message ")
    print("received message: " ,str(msg.payload.decode("utf-8")))

while True:
    client = mqtt.Client()
    
    client.on_connect = on_connect
    client.on_message = on_message
    
    client.connect("test.mosquitto.org", 1883, 60)
    input1 = input()
    client.publish("statl", input1)
    # client.loop_forever()