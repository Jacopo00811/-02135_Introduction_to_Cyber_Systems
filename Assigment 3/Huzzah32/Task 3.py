import machine
import time

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF)/16.0
    if value & 0x1000:
        temp-= 256.0
    return temp

Green = machine.Pin(26, machine.Pin.OUT)
Yellow = machine.Pin(25,machine.Pin.OUT)
Red = machine.Pin(4,machine.Pin.OUT)

while True:
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
    #print(i2c.scan())
    address = 24
    temp_reg = 5
    res_reg = 8
    data = bytearray(2)
    i2c.readfrom_mem_into(address, temp_reg, data)
    
    temperature=temp_c(data)
    
    print(temperature)
    
    if temperature<25:
        Green.on()
        Yellow.off()
        Red.off()
    if temperature>=25 and temperature<=28:
        Green.off()
        Yellow.on()
        Red.off()
    if temperature>28:
        Green.off()
        Yellow.off()
        Red.on()
    
    time.sleep(0.5)
    
    

