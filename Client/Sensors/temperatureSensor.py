from .Sensor import Sensor
import random 
import time

class TemperatureSensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(TemperatureSensor, self).__init__(*args, **kwargs)
    # degrees measure temperature activity
    # 40 degrees celcius == safe
    def dataGeneration(self):
        time.sleep(1)
        return random.uniform(0, 100)