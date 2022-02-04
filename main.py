from machine import Pin
import time

input_pin = 25
output_pin = 15
input = Pin(input_pin) # Button B
output = Pin(output_pin, Pin.OUT)

output.value(0)

def valueChanged(pin):
    global input
    
    if input.value():
        print("Switch on relais")
        output.value(1)
        time.sleep(1)
        output.value(0)

input.irq(valueChanged)
