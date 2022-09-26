from lib_lcd1602_2004_with_i2c import LCD
import settings
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

i2c = settings.I2C_OBJ
lcd = LCD(i2c)
led = settings.LED_PIN
button = settings.BTN_PIN
sensor = dht12.DHT12(i2c)
light_sensor = machine.ADC(0)
backlight = settings.BACKLIGHT
#pwm.duty(500)
sleep(1)
#sensor.measure() sensor.temperature() sensor.humidity()

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        sleep(1)

#GITHUB_URL = "https://github.com/RangerDigital/senko/blob/master/examples/"
OTA = senko.Senko(
    user="KamRusz",
    repo="solaredge_esp_monitor",
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
if OTA.fetch():
    print("A newer version is available!")
else:
    print("Up to date!")
#check time
time=urequests.get(url=settings.TIME_API_URL)
#print(time.json()['dayOfWeek'])
my_rtc=(time.json()['year'],time.json()['month'],time.json()['day'],time.json()['hour'],time.json()['minute'],time.json()['seconds'],0,0)

rtc=machine.RTC()
rtc.datetime(my_rtc)
#print(rtc.datetime())

print("now to main.py")

