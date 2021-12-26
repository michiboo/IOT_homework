from .Sensor import Sensor
import random 
import time

class FlowRateSensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(FloRateSensor, self).__init__(*args, **kwargs)
    # pascal measure pressure activity
    # 100pa == safe
    def dataGeneration(self):
        time.sleep(0.5)
        return random.uniform(50, 2000)