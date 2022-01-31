from .Sensor import Sensor
import random 
import time

class PressureSensor(Sensor):
    # def __init__(self, *args, **kwargs):
    #     super(PressureSensor, self).__init__(*args, **kwargs)
    # pascal measure pressure activity
    # 100psi == safe
    def dataGeneration(self):
        time.sleep(0.5)
        return random.uniform(0, 2000)