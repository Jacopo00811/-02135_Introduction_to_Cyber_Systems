import machine
import network
import socket
import time

def temp_c(data):
    value = data[0] << 8 | data[1]
    temp = (value & 0xFFF)/16.0
    if value & 0x1000:
        temp-= 256.0
    return temp


Green = machine.Pin(4, machine.Pin.OUT)
Yellow = machine.Pin(26,machine.Pin.OUT)
Red = machine.Pin(25,machine.Pin.OUT)


ap = network.WLAN (network.AP_IF) # instance of the station WiFi interface for access point mode
ap.active (True) # calls and uses the active method
ap.config (essid = 'ESP32-Andrea&Jacopo') # connfigures the name of the wifi network just activated
ap.config (authmode = 3, password = 'Pippetto') #  connfigures the password of the wifi and Authentication mode supported (3 is 
# WPA2-PSK cryptation)
pins = [machine.Pin(i, machine.Pin.IN) for i in (15, 27, 33)]

# creates the html web-page
html = """<!DOCTYPE html> 
<html>
    <head> <title>ESP32 Pins</title> </head>
    <body> <h1>ESP32 Pins</h1>
        <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
    </body>
</html>
"""
# a socket is the end point that sends/recives data

addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1] #Translate the host/port argument into a sequence tuples that
# contain all the necessary arguments for creating a socket connected to that service.

s = socket.socket() # creates the socket object
s.bind(addr) # binds the socket passing to it the IP and a port
s.listen(1) # prepares the queque for the incoming requests

print('listening on', addr)

while True:
    
    #Task 3 code starts here
    
    i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(23))
    #print(i2c.scan())
    address = 24
    temp_reg = 5
    res_reg = 8
    data = bytearray(2)
    i2c.readfrom_mem_into(address, temp_reg, data)
    
    temperature=temp_c(data)
    
    #print(temperature)
    
    if temperature<25.5:
        Green.on()
        Yellow.off()
        Red.off()
    if temperature>=25.5 and temperature<=28:
        Green.off()
        Yellow.on()
        Red.off()
    if temperature>28:
        Green.off()
        Yellow.off()
        Red.on()
    
    time.sleep(0.2)
    
    # Task 3 code ends here
    
    

    cl, addr = s.accept() # accepts the client with its respective address
    #print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0) #creates a file in rwb mode

    while True:
        line = cl_file.readline() #reads each line of the file 
        #print(line)
        if not line or line == b'\r\n': #checks if we arrived at the end of the text and in case breaks out
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins] # creates the updated rows with the certain pin values
    rows.append('<tr><td>Temperature</td><td>'+str(temperature)+' C'+'</td></tr>')
    response = html % '\n'.join(rows) # joins the rows and saves it in the variable "response"
    cl.send(response) # sends a certain response to the client socket
    cl.close() # close the created socket
    #print(response)