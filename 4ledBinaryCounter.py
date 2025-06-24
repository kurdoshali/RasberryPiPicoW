from machine import Pin
from utime import sleep

oneLED = Pin(12, Pin.OUT)
twoLED = Pin(13, Pin.OUT)
fourLED = Pin(14, Pin.OUT)
eightLED = Pin(15, Pin.OUT)

while True:
    oneLED.value(0)
    twoLED.value(0)
    fourLED.value(0)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(1)
    twoLED.value(0)
    fourLED.value(0)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(1)
    fourLED.value(0)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(1)
    twoLED.value(1)
    fourLED.value(0)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(0)
    fourLED.value(1)
    eightLED.value(0)
    sleep(1)

    oneLED.value(1)
    twoLED.value(0)
    fourLED.value(1)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(1)
    fourLED.value(1)
    eightLED.value(0)
    sleep(1)
    
    oneLED.value(1)
    twoLED.value(1)
    fourLED.value(1)
    eightLED.value(0)
    sleep(1)

    oneLED.value(0)
    twoLED.value(0)
    fourLED.value(0)
    eightLED.value(1)
    sleep(1)   
    
    oneLED.value(1)
    twoLED.value(0)
    fourLED.value(0)
    eightLED.value(1)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(1)
    fourLED.value(0)
    eightLED.value(1)
    sleep(1)
    
    oneLED.value(1)
    twoLED.value(1)
    fourLED.value(0)
    eightLED.value(1)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(0)
    fourLED.value(1)
    eightLED.value(1)
    sleep(1)
    
    oneLED.value(1)
    twoLED.value(0)
    fourLED.value(1)
    eightLED.value(1)
    sleep(1)
    
    oneLED.value(0)
    twoLED.value(1)
    fourLED.value(1)
    eightLED.value(1)
    sleep(1)
   
    oneLED.value(1)
    twoLED.value(1)
    fourLED.value(1)
    eightLED.value(1)
    sleep(1)
