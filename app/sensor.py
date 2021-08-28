import machine
from machine import *
import gc
from bh1750 import BH1750
import dht
class sensors:
    def __init__(self,temp,scl,sda,analog):
        self.temp=temp
        self.scl=scl
        self.sda=sda
        self.analog=analog

    def temp_hum(self):
        ''' This function provides temperature and humidity readings from aquaman'''
        try:
            dht11=dht.DHT11(machine.Pin(self.temp))
            dht11.measure()
            temp_hum_read= [dht11.temperature(),dht11.humidity()]
            return temp_hum_read
        except:
            return [0,0]
        
    def amb_light(self):
        ''' This function provides ambient light readings from aquaman'''
        try:
            scl = machine.Pin(self.scl)
            sda = machine.Pin(self.sda)
            i2c = machine.I2C(scl,sda)
            s = BH1750(i2c)
            return s.luminance(BH1750.ONCE_HIRES_1)
        except:
            return 0
    
    def tds(self):
        ''' This function provides TDS & EC readings from aquaman'''
        try:
            ec=ADC(self.analog)
            ec_readings=0
            for i in range(0,10):
                ec=1024-ec.read()
                ec_readings+=ec
                time.sleep(5)
            return(ec_readings/10)
        except:
            return 0
        
