from .Sensor import Sensor
import random 
import time

class WaterChemistrySensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(RadiationSensor, self).__init__(*args, **kwargs)
    # Becquerel measure raditiaon activity
    #148 becquerels per cubic meter == safe
    def dataGeneration(self):
        time.sleep(0.5)
        return random.uniform(100, 200)