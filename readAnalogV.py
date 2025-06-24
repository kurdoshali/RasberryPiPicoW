import machine
from time import sleep
polPin=28
myPol=machine.ADC(polPin)

while True:
    potVal=myPol.read_u16()
    voltage=(3.3/65327)*potVal - (686.4/65327)
    print(voltage)
    sleep(.5)