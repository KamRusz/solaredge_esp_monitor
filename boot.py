from lib_lcd1602_2004_with_i2c import LCD
import settings
import wifimgr
from time import sleep
import machine
import dht12
import urequests

i2c = settings.I2C_OBJ
lcd = LCD(i2c)
led = settings.LED_PIN
button = settings.BTN_PIN
sensor = dht12.DHT12(i2c)
light_sensor = settings.ADC_PIN
backlight = settings.BACKLIGHT
sleep(1)
sensor.measure() #sensor.temperature() sensor.humidity()

wlan = wifimgr.get_connection()
if wlan is None:
    print("Could not initialize the network connection.")
    while True:
        sleep(1)

#check time
time_web=urequests.get(url=settings.TIME_API_URL)
#print(time_web.json()['dayOfWeek'])
my_rtc=(time_web.json()['year'],time_web.json()['month'],time_web.json()['day'],time_web.json()['hour'],time_web.json()['minute'],time_web.json()['seconds'],0,0)

rtc=machine.RTC()
rtc.datetime(my_rtc)
#print(rtc.datetime())

print("now to main.py")