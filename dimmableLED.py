#based on user input

from machine import PWM, Pin 
from time import sleep

outPin = 16
analogOut=PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
    myVoltage=float(input("what voltage would you like? "))
    pwmVal=(65550/3.3)*myVoltage
    analogOut.duty_u16(int(pwmVal))
