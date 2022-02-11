from Sensors.radiationSensor import RadiationSensor
from Sensors.temperatureSensor import TemperatureSensor
from Sensors.pressureSensor import PressureSensor
from Sensors.flowRateSensor import FlowRateSensor
from Sensors.waterChemistrySensor import WaterChemistrySensor
from threading import Thread

def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)


# client = mqtt.Client('P1')
# client.on_message = on_message

broker_address = '0.0.0.0'

flowRate = FlowRateSensor('flowRate', 'F1', broker_address)
temperature = TemperatureSensor('temperature', 'T1', broker_address)
radiation = RadiationSensor('radiation', 'R1', broker_address)
pressure = PressureSensor('pressure', 'P1', broker_address)
waterChemistry = WaterChemistrySensor('waterChemistry', 'W1', broker_address)


thread = Thread(target = temperature.stream)
thread.start()

thread2 = Thread(target = flowRate.stream)
thread2.start()

thread3 = Thread(target = radiation.stream)
thread3.start()

thread4 = Thread(target = pressure.stream)
thread4.start()

thread5 = Thread(target = waterChemistry.stream)
thread5.start()

