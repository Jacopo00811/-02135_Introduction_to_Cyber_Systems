import machine, neopixel
from machine import Pin, ADC
import time

pot = ADC(Pin(34))
pot.atten(ADC.ATTN_11DB) #Full range: 3.3v
np = neopixel.NeoPixel(machine.Pin(13,machine.Pin.OUT), 2)
np.ORDER = (0,1,2)
np[0]=(0,0,0)
np[1]=(0,0,0)
np.write()

while True:
    pot_value = pot.read()
    print(pot_value)
    
    val_rgb=int(pot_value/16)
    
    np[0]=(val_rgb,0,val_rgb)
    np[1]=(val_rgb,0,val_rgb)
    np.write()
    
    time.sleep(0.1)
    
    

