from .Sensor import Sensor
import random 
import time

class WaterChemistrySensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(WaterChemistrySensor, self).__init__(*args, **kwargs)
    # ph measure raditiaon activity
    # ph of 6-7 == safe
    def dataGeneration(self):
        time.sleep(0.5)
        return random.uniform(1, 10)