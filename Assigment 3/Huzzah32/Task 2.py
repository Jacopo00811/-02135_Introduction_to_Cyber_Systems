import machine
import time
#initalinze the input and output pins
GreenPin = machine.Pin(26, machine.Pin.OUT)
YellowPin = machine.Pin(25,machine.Pin.OUT)
RedPin = machine.Pin(4,machine.Pin.OUT)
Button = machine.Pin(27,machine.Pin.IN) 

pushed = False #initialize some variables
state = "Green"
state_before = 0
#turns on the button and the green pin 
GreenPin.on()
Button.on()
  
while True:
    time.sleep(0.01)
    Button_value = Button.value()#reads the button
    
    if Button_value == 1:#if it is up then checks the state
        if state_before == 0:
            pushed = True#and change the pushed variable
            state_before = 1 #now the state before is 1
    else:
        state_before = 0
     
    #checks if it is pushed and sets the next state
    if pushed == True and state == "Green":
        state = "Yellow"
        pushed = False

    elif pushed == True and state == "Yellow":
        state = "Red"
        pushed = False
		
    elif pushed == True and state == "Red":
        state = "Green"
        pushed = False
	
    #turns on/off the led for each state
    elif state == "Green":
        GreenPin.on()
        RedPin.off()

    elif state == "Yellow":
        GreenPin.off()
        YellowPin.on()

    elif state == "Red":
        YellowPin.off()	
        RedPin.on()
   
    
    
    
    
    
    
    
    
    
    
    
    
    
 