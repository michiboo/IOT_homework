from .Sensor import Sensor
import random 
import time

class FlowRateSensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(FloRateSensor, self).__init__(*args, **kwargs)
    # cm/s measure pressure activity
    # 100cm/s == safe
    def dataGeneration(self):
        time.sleep(1)
        return random.uniform(50, 2000)