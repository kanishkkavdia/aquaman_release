import time
import network
from machine import *
from umqtt.simple import MQTTClient
from ConnectWifi import *
import sensor
from sensor import *
import gc

class execute:
    def __init__(self,server,client,channel_id,write_api_key,read_api_key):
        self.server=server
        self.client=client
        self.channel_id=channel_id
        self.write_api_key=write_api_key
        self.read_api_key=read_api_key
        self.topic = "channels/" + self.channel_id + "/publish/" + self.write_api_key

    def automate(self,action_pin,duration_on,duration_off,data,scl,sda,analog):
        ''' This function is the core module. Syntax: automate(pin connected, duration on, duration off,temperature,scl,sda,analog)'''
        duration_on=int(duration_on)
        duration_off=int(duration_off)
        execute=machine.Pin(action_pin)
        sensor_val=sensor.sensors(data,scl,sda,analog)
        counter=0
        execute.value(1)
        while counter<=int(duration_on):
            time.sleep(10)
            print(str(sensor_val.temp_hum()[0]),str(sensor_val.temp_hum()[1]))
            try:
                self.client.connect()
                # Kanishk to break sensor values individualy, if null, pass 0
                payload="field1="+str(sensor_val.temp_hum()[0])+"&field2="+str(sensor_val.temp_hum()[1])+"&field3="+str(sensor_val.tds())+"&field6="+str(sensor_val.amb_light())
                self.client.publish(self.topic,payload)
            except:
                pass
            counter+=10
        counter=0
        while counter<=int(duration_off):
            execute.value(0)
            time.sleep(10)
            counter+=10
            try:
                payload="field1="+str(sensor_val.temp_hum()[0])+"&field2="+str(sensor_val.temp_hum()[1])+"&field3="+str(sensor_val.tds())+"&field6="+str(sensor_val.amb_light())
                self.client.publish(self.topic,payload)
                self.client.disconnect()
            except:
                pass    
