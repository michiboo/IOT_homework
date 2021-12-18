import random 
import paho.mqtt.client as mqtt

import time
class Sensor():
    def __init__(self, topic, clientId, broker_address, broker_port='1883'):
        self.topic = topic
        self.broker_address = broker_address
        self.broker_port = int(broker_port)
        self.client = mqtt.Client(clientId)
        self.client.connect(broker_address, port=self.broker_port)
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect
        self.clientId = clientId
    
    def on_message(self, client, userdata, message):
        print("message received " ,str(message.payload.decode("utf-8")))
        print("message topic=",message.topic)
        print("message qos=",message.qos)
        print("message retain flag=",message.retain)

    def on_disconnect(self, client, userdata,rc=0):
        logging.debug("DisConnected result code "+str(rc))
        self.client.loop_stop()
    
    def dataGeneration(self):
        return random.rand(1,100)
    
    def send_data(self):
        self.client.publish(f'{self.topic}/{self.clientId}', self.dataGeneration())

    def stream(self):
        self.client.loop_start()
        while True:
            self.send_data()