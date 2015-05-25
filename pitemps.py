import collections

class Thermometer(object):

    def __init__(self,device):
        self.device = device
        self.history = collections.deque(maxlen = 100)
        #device is the folder i.e. /sys/bus/w1/devices/xxx

    @property
    def filename(self):
        return '/sys/bus/w1/devices/' + self.device + '/w1_slave'

    def get_temperature(self):
        r = float('nan')
        try:
            with open(self.filename,'r') as f:
                result = f.read()
                r = float(result.split('\n')[1].rsplit(' ',1)[1].split('=')[1])/100
        except Exception as e:
            pass
        return r


class ThermometerArray(object):
    def __init__(self):
        self.thermometers = {}
        self.find_thermometers()

    def find_thermometers(self):
        t = '/sys/bus/w1/devices/w1_bus_master1/w1_master_slaves'
        with open(t,'r') as f:
            sensors = f.read().split('\n')

        for sensor in sensors:
            if sensor not in self.thermometers.keys():
                self.thermometers[sensor] = Thermometer(sensor) 

    def get_temperatures(self):
        return {k:self.thermometers[k].get_temperature() for k in self.thermometers}

ta = ThermometerArray()
print ta.get_temperatures()



