import paho.mqtt.client as mqtt
from Sensors.radiationSensor import RadiationSensor
from Sensors.temperatureSensor import TemperatureSensor
from Sensors.pressureSensor import PressureSensor
from Sensors.flowRateSensor import FlowRateSensor
from Sensors.waterChemistrySensor import WaterChemistrySensor

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


# client = mqtt.Client('P1')
# client.on_message = on_message

broker_address = 'localhost'
# print(client.connect(broker_address))
# client.loop_start() 
# client.subscribe('house/light')
# client.publish('house/light', 'ON')
# import time
# time.sleep(2)
# client.publish('house/light', 'OFF')
# client.loop_stop() 

radiation = RadiationSensor('radiation', 'R1', broker_address)
temperature = TemperatureSensor('temperature', 'T1', broker_address)
pressure = PressureSensor('pressure', 'P1', broker_address)
flowRate = FlowRateSensor('flowRate', 'F1', broker_address)
waterChemistry = WaterChemistrySensor('waterChemistry', 'W1', broker_address)

radiation.stream()
# temperature.stream()
# pressure.stream()
# flowRate.stream()
# waterChemistry.stream()