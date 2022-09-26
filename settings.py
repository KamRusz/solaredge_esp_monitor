import machine

#Pinout
SCL_PIN = machine.Pin(5)
SDA_PIN = machine.Pin(4)
LED_PIN = machine.Pin(2, machine.Pin.OUT)
BTN_PIN = machine.Pin(12, machine.Pin.IN)
I2C_OBJ = machine.I2C(scl=SCL_PIN, sda=SDA_PIN, freq=400000)
BACKLIGHT = machine.PWM(machine.Pin(15), duty=500)
TIME_API_URL = 'https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw'

# wifimgr settings
AP_SSID = "SolarEdge_monitoring"
AP_PASSWORD = "solaredge"
AP_AUTHMODE = 3  # WPA2

