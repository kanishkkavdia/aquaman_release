import network
import machine
from machine import Pin

class connectivity:
    def __init__(self,ssid,password,pin):
        self.ssid=ssid
        self.password=password
        self.pin=pin
    
    def connect(self):
        '''This function is for connecting to internet'''
        indicate=Pin(self.pin,Pin.OUT)
        station = network.WLAN(network.STA_IF)
        station.active(True)
        station.connect(self.ssid, self.password)
        print(self.ssid,self.password)
        if station.ifconfig()[0]=="0.0.0.0":
            print("Not Connected")
            indicate.value(0)
            return station.ifconfig()[0]
        else:
            indicate.value(1)       
            print("Connected")
            return station.ifconfig()[0]
  
    def listNetwork(self):
        '''This function is for listing available wifi networks'''
        station = network.WLAN(network.STA_IF)
        station.active(True)
        network_list=[]
        for x in station.scan():
            network_list.append(x[0].decode("utf-8"))
        return network_list
  
    def disconnect(self):
        '''This function is for disconnecting internet'''
        indicate=Pin(self.pin,Pin.OUT)
        indicate.value(0)
        station = network.WLAN(network.STA_IF)
        station.disconnect()
        station.active(False)