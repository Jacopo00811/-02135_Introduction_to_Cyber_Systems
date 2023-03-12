import machine, neopixel
import time


def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF)/16.0
    if value & 0x1000:
        temp-= 256.0
    return temp

np = neopixel.NeoPixel(machine.Pin(4,machine.Pin.OUT), 2)
np.ORDER = (0,1,2)
np[0]=(0,0,0)
np[1]=(0,0,0)
np.write()

while True:
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
    address = 24
    temp_reg = 5
    res_reg = 8
    data = bytearray(2)
    i2c.readfrom_mem_into(address, temp_reg, data)
    
    temperature=temp_c(data)
    print(temperature)
 
    if temperature<=25:
        np[0]=(0,255,0)
        np[1]=(0,255,0)
        np.write()
    elif temperature>25 and temperature<27:
        np[0]=(255,255,0)
        np[1]=(255,255,0)
        np.write()
    elif temperature>=27:
        np[0]=(255,0,0)
        np[1]=(255,0,0)
        np.write()
    
    time.sleep(0.5)
    
    
    
    
    

    
    