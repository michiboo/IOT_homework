import paho.mqtt.client as mqtt
from Sensors.radiationSensor import RadiationSensor
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


# client = mqtt.Client('P1')
# client.on_message = on_message

broker_address = '172.17.0.4'
# print(client.connect(broker_address))
# client.loop_start() 
# client.subscribe('house/light')
# client.publish('house/light', 'ON')
# import time
# time.sleep(2)
# client.publish('house/light', 'OFF')
# client.loop_stop() 

a = RadiationSensor('radiation', 'R1', broker_address)
a.stream()