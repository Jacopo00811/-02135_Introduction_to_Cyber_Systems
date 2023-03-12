import machine
import network
import socket


def toggle_led(t):
    led.value(not led.value())

led = machine.Pin(17, machine.Pin.OUT)

ap = network.WLAN (network.AP_IF) # instance of the station WiFi interface for access point mode
ap.active (True) # calls and uses the active method
ap.config (essid = 'ESP32-Andrea&Jacopo') # connfigures the name of the wifi network just activated
ap.config (authmode = 3, password = 'Pippetto') #  connfigures the password of the wifi and Authentication mode supported (3 is 
# WPA2-PSK cryptation)
pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

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

timer_1= machine.Timer(0)
timer_1.init(period=500, mode=machine.Timer.PERIODIC, callback=toggle_led)


while True:
    cl, addr = s.accept() # accepts the client with its respective address
    #print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0) #creates a file in rwb mode
    while True:
        line = cl_file.readline() #reads each line of the file 
        #print(line) 
        if not line or line == b'\r\n': #checks if we arrived at the end of the text and in case breaks out
            break
    rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins] # creates the updated rows with the certain pin values
    response = html % '\n'.join(rows) # joins the rows and saves it in the variable "response"
    cl.send(response) # sends a certain response to the client socket
    cl.close() # close the created socket
