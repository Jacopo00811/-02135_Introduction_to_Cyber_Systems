import machine
import network
import socket
import json
import neopixel

# Server
ap = network.WLAN (network.AP_IF)
ap.active (True)
ap.config (essid = 'ESP32-Andrea&Jacopo') # connfigures the name of the wifi network just activated
ap.config (authmode = 3, password = 'Pippetto') #  connfigures the password of the wifi and Authentication mode supported (3 is 
# WPA2-PSK cryptation)

# Pins used
pins = [machine.Pin(i, machine.Pin.IN) for i in (12, 14, 15, 22, 23, 32)]

# Button
BUTTON = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)  

# Potentiometer
POTENTIOMETER = machine.ADC(machine.Pin(32))                    
POTENTIOMETER.width(machine.ADC.WIDTH_10BIT)
POTENTIOMETER.atten(machine.ADC.ATTN_11DB)

# Temperature
I2C = machine.I2C(scl = machine.Pin(22), sda = machine.Pin(23)) 
DATA = I2C.readfrom_mem(24, 5, 2)    

# Function to calculate celsius
def CELSIUS(DATA):                                                 
    VALUE = (DATA[0] << 8 | DATA[1])
    TEMPERATURE = (VALUE & 0xFFF) / 16.0
    if VALUE & 0x1000:
        TEMPERATURE = -256
    return TEMPERATURE

# LED
LED = machine.Pin(12, machine.Pin.OUT)
LED.value(0)

# NeoPixel
NeoLED = neopixel.NeoPixel(machine.Pin(14), 1)
NeoLED[0] = (0, 0, 0)
NeoLED.write()

# HTML design
html = """<!DOCTYPE html>
<html>
    <head> <title>ESP32 Pins</title> </head>
    <body> <h1>ESP32 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    
    p = [(str(p), p.value()) for p in pins]
    button = BUTTON.value()
    temp = CELSIUS(I2C.readfrom_mem(24, 5, 2))
    potentiometer = round(POTENTIOMETER.read() / 4.01) 
    
    web_path = ""
    
    while True:
        line = cl_file.readline()
        
        web_path = web_path + str(line)
        
        print(line)
        if not line or line == b'\r\n':
            break
    
    JSON = {"LED": LED.value(), "Button": button, "Temperature": temp, "Potentiometer": potentiometer, "NeoPixel": NeoLED[0]}
    
    State = JSON
    web_path_sti = web_path.split('/')
    
    # Turns the LED on
    if "pins" in web_path_sti and "pin12" in web_path_sti and "sethigh" in web_path_sti:
        State = JSON
        LED.value(1)
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["NeoPixel"]
        
        State = list(State.values())
    
    # Turns the LED off
    if "pins" in web_path_sti and "pin12" in web_path_sti and "setlow" in web_path_sti:
        State = JSON
        LED.value(0)
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["NeoPixel"]
        
        State = list(State.values())
    
    # For some reason, the color green and red are reversed on our NeoPixel LEDs.
    # This is also mentioned on the NeoPixel Uberguide where it states that some
    # NeoPixels are wired as (Green, Red, Blue)-color instead of (Red, Green, Blue)-color.
    
    # Turns the NeoPixel on
    if "pins" in web_path_sti and "pin14" in web_path_sti and "sethigh" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (255, 255, 0)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Turns the NeoPixel off
    if "pins" in web_path_sti and "pin14" in web_path_sti and "setlow" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (0, 0, 0)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Changes the NeoPixel’s color to green
    if "pins" in web_path_sti and "pin14" in web_path_sti and "green" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (255, 0, 0)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Changes the NeoPixel’s color to red
    if "pins" in web_path_sti and "pin14" in web_path_sti and "red" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (0, 128, 0)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Changes the NeoPixel’s color to blue
    if "pins" in web_path_sti and "pin14" in web_path_sti and "blue" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (0, 0, 255)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Changes the NeoPixel’s color to pink
    if "pins" in web_path_sti and "pin14" in web_path_sti and "pink" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (105, 255, 180)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Changes the NeoPixel’s color to purple
    if "pins" in web_path_sti and "pin14" in web_path_sti and "purple" in web_path_sti:
        State = JSON
        
        NeoLED[0] = (0, 128, 128)
        NeoLED.write()
        
        del State["Button"]
        del State["Temperature"]
        del State["Potentiometer"]
        del State["LED"]
        
        State = list(State.values())
    
    # Shows the status of the button
    if "pins" in web_path_sti and "button" in web_path_sti:
        State = JSON
        
        del State["Temperature"]
        del State["Potentiometer"]
        del State["NeoPixel"]
        del State["LED"]
        
        State = list(State.values())
    
    # Shows the temperature
    if "sensors" in web_path_sti and "temperature" in web_path_sti:
        State = JSON
        
        del State["Button"]
        del State["Potentiometer"]
        del State["NeoPixel"]
        del State["LED"]
        
        State = list(State.values())
    
    # Shows the status of the potentiometer
    if "pins" in web_path_sti and "potentiometer" in web_path_sti:
        State = JSON
        
        del State["Button"]
        del State["Temperature"]
        del State["NeoPixel"]
        del State["LED"]
        
        State = list(State.values())
    
    response = json.dumps(State)
    cl.send(response)
    cl.close()