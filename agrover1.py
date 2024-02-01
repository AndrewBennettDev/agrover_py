from machine import Pin
import utime

driveA = Pin(13, machine.Pin.OUT)
driveB = Pin(14, machine.Pin.OUT)

steeringA = Pin(17, machine.Pin.OUT)
steeringB = Pin(18, machine.Pin.OUT)

def forward():
    driveA.high()
    driveB.low()
    steeringA.low()
    steeringB.low()
    
def reverse():
    driveA.low()
    driveB.high()
    steeringA.low()
    steeringB.low()
    
def stop():
    driveA.low()
    driveB.low()
    steeringA.low()
    steeringB.low()

def turn_left():
    driveA.high()
    driveB.low()
    steeringA.low()
    steeringB.low()

def turn_right():
    driveA.high()
    driveB.low()
    steeringA.low()
    steeringB.low()

def back_left():
    driveA.low()
    driveB.high()
    steeringA.low()
    steeringB.low()

def back_right():
    driveA.low()
    driveB.high()
    steeringA.low()
    steeringB.low()