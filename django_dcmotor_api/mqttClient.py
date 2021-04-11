import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print(" masuk connect ")
    client.subscribe("statl")
    # client.publish("statl", "132ldkflkajsdhf")
    #client.subscribe("statl")

def on_message(client, userdata, msg):
    print(" Halo Masuk On Message ")
    print("received message: " ,str(msg.payload.decode("utf-8")))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("test.mosquitto.org", 1883, 60)

