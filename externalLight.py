from machine import Pin
from utime import sleep
redLED = Pin(15, Pin.OUT)
while True:
    redLED.toggle()
    sleep(1)