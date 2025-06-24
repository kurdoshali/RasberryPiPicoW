#based on potentiometer, should be able to run on boot up

from machine import PWM, Pin, ADC
from time import sleep

polPin=28
myPol=ADC(polPin)

outPin = 16
analogOut=PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    potVal=myPol.read_u16()
    expVal=(16/65550)*potVal
    outVal=2**expVal
    analogOut.duty_u16(int(outVal))
    sleep(.1)

    
