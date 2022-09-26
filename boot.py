from lib_lcd1602_2004_with_i2c import LCD
import wifimgr
from time import sleep
import machine
import senko
import dht12
import urequests

try:
  import usocket as socket
except:
  import socket
  
i2c = machine.I2C(scl=machine.Pin(5), sda=machine.Pin(4), freq=400000)
lcd = LCD(i2c)
led = machine.Pin(2, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN)
sensor = dht12.DHT12(i2c)
backlight = machine.ADC(0)
pwm = machine.PWM(machine.Pin(15))
pwm.duty(500)
sleep(1)
#sensor.measure() sensor.temperature() sensor.humidity()
"""
wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        sleep(1)
"""
GITHUB_URL = "https://github.com/RangerDigital/senko/blob/master/examples/"
OTA = senko.Senko(
    user="ocktokit",
    repo="octokit-iot",
    files=["boot.py", "main.py"]
    )
'''
if OTA.update():
    print("Updated to the latest version! Rebooting...")
    lcd.puts('Updated to the',0)
    lcd.puts('latest version!',1)
    lcd.puts('Rebooting...',2)
    machine.reset()
'''
#check time
time=urequests.get(url='https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw')
#print(time.json()['dayOfWeek'])
my_rtc=(time.json()['year'],time.json()['month'],time.json()['day'],time.json()['hour'],time.json()['minute'],time.json()['seconds'],0,0)

rtc=machine.RTC()
rtc.datetime(my_rtc)
#print(rtc.datetime())

print("now to main.py")

