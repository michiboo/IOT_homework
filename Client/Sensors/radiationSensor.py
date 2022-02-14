from .Sensor import Sensor
import random 
import time

class RadiationSensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(RadiationSensor, self).__init__(*args, **kwargs)
    # Becquerel measure raditiaon activity
    #148 becquerels per cubic meter == safe
    def dataGeneration(self):
        time.sleep(1)
        return random.uniform(50, 300)