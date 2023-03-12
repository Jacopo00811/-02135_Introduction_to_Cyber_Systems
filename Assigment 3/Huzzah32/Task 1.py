import machine
from time import time,sleep,ticks_ms

LED = machine.Pin(17, machine.Pin.OUT) #set the pin as output
current_time = ticks_ms()
while True:
    if (ticks_ms() - current_time)/1000 >= 0.5:
        LED.value(not LED.value())
        current_time = ticks_ms()