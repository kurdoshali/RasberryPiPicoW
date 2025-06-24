from machine import Pin 
from utime import sleep

led=Pin("LED", Pin.OUT)

print("LED starts flashing")

while True:
    led.toggle()
    sleep(0.5)