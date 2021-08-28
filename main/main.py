import esp
import gc
import network
import machine
import time
import dht
import machine
from machine import Pin, ADC
from bh1750 import BH1750
from ConnectWifi import *
from sensor import *
from umqtt.simple import MQTTClient
import execute

#*******************Thinkspeak Configuration**********************    
server = "mqtt.thingspeak.com"
client = MQTTClient("umqtt_client", server)
channel_id = '1468426'
write_api_key = "ER7ZJTTHUE7XVER5"
read_api_key="3W0EKHCGEU99XP69"
topic = "channels/" + channel_id + "/publish/" + write_api_key
#*******************Thinkspeak Configuration End******************

#*******************Pin Configuration*****************************
action_pin=5
light_pin=4
dispensor_pin=0
data=14
scl=13
sda=12
analog=0
#******************Pin Configuration End**************************

#*******************Variable Definition***************************
duration_on=10
duration_off=20
#******************Variable Definition End************************

#******************Main Code Begin********************************





#******************End of Main execution**************************

#**************************Example********************************
connectivity("DK Home","123456789",2).connect()
# print(sensors(5,4,12,0).temp_hum())      
aquaman=execute.execute(server,client,channel_id,write_api_key,read_api_key)
aquaman.automate(action_pin,duration_on,duration_off,data,scl,sda,analog)


#pin usage {1. Data tem 2.scl 3. sda 4. A0}
# import thsignal
# import gc
# import time
# # import urequests as requests
# # import ujson as json
# import Hydroponic_timer
# import testing
# configure_switch=Pin(4,Pin.IN)
# execute=Pin(5,Pin.OUT)
# ConnectWifi.connect("DK Home","123456789")
# print("connected")
# # print(duration_on,duration_off)
# # print("configure value:",configure_switch.value())
# duration_on=testing.api_collector("https://api.thingspeak.com/channels/1468426/fields/4.json?","field4")
# duration_off=testing.api_collector("https://api.thingspeak.com/channels/1468426/fields/5.json?","field5")
# print(duration_on)
# print(duration_off)
# while configure_switch.value()==1:
#  #<  put code here >
# # 
#     Hydroponic_timer.timer(execute,duration_on,duration_off)
#     if configure_switch.value()==0:
#         break
# #Configure mode on configure_switch.value()==1
# print("Out of loop")

#******************Example**************************