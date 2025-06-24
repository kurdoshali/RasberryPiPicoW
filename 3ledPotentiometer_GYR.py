import machine
from machine import Pin
from time import sleep
polPin=28
myPol=machine.ADC(polPin)

gled = Pin(15, Pin.OUT)
yled = Pin(14, Pin.OUT)
rled = Pin(13, Pin.OUT)
while True:
    potVal=myPol.read_u16()
    voltage=(100/65327)*potVal - (20800/65327)
    # sleep(.5)
    if voltage <= 70:
        rled.value(0)
        yled.value(0)
        gled.value(1)
    if voltage > 70 and voltage <= 84:
        gled.value(0)
        rled.value(0)
        yled.value(1)
    if voltage > 84:
        gled.value(0)
        yled.value(0)
        rled.value(1)
        
    

