import os
import serial
import time
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) #don't remove this, else you will get an error
import pigpio #importing GPIO libraryimport pigpio
import sys
import FaBo9Axis_MPU9250
import math
import getAngles
import barometerinit

ESC1=13  #ESC connections with the GPIO pins; note its the BROADCOM number, not the GPIO pin number!
ESC2=12
ESC3=18
ESC4=19
pwr1=1100
pwr2=1100
pwr3=1100
pwr4=1100


max_value = 1500
min_value = 970

pi = pigpio.pi();

mpu9250 = FaBo9Axis_MPU9250.MPU9250()
#sys.path.insert(0, 'activeStateDiscretePid/PID.py')
#sys.path.append('/home/9250FlightControl/activeStateDiscretePid')
import PID
import program
#print program.getData(mpu9250)
"""
[roll,pitch,elevation]
"""
state = [PID.PID(0,0,0),PID.PID(0,0,0),PID.PID(0,0,0)]
state[0].SetPoint=0
state[1].SetPoint=0
state[2].SetPoint=barometerinit.getData()+4.5
#state = []ii
#p=PID.PID(1.0,0,0)
#p.SetPoint=0.0
current = time.time()

data =[0,0,0,0,0,0,0,0,0]

# INITIALIZATION

pi.set_servo_pulsewidth(ESC1, max_value)
pi.set_servo_pulsewidth(ESC2, max_value)
pi.set_servo_pulsewidth(ESC3, max_value)
pi.set_servo_pulsewidth(ESC4, max_value)
pi.set_servo_pulsewidth(ESC1, min_value)
pi.set_servo_pulsewidth(ESC2, min_value)
pi.set_servo_pulsewidth(ESC3, min_value)
pi.set_servo_pulsewidth(ESC4, min_value)
pi.set_servo_pulsewidth(ESC1, 1040)
pi.set_servo_pulsewidth(ESC2, 1040)
pi.set_servo_pulsewidth(ESC3, 1040)
pi.set_servo_pulsewidth(ESC4, 1040)

time.sleep(5)

while True:
     pwr1 = 1100
     pwr2 = 1100
     pwr3 = 1100
     pwr4 = 1100
     delta = time.time()-current
     current = time.time()
     data = program.getData(mpu9250)
     alt = barometerinit.getData()
     state[0].setSampleTime(delta)
     state[1].setSampleTime(delta)
     state[2].setSampleTIme(delta)
     roll, pitch = getAngles.rollpitch(data)
     state[0].update(roll)
     state[1].update(pitch)
     state[2].update(altitude)
     output=state[0].output
     pitchout = state[1].output
     heightout =  state[2].output
     if(output > 0):
        pwr2 += 10*output
        pwr3 += 10*output
        pwr4 -= 10*output
        pwr1 -= 10*output
     if(pitchout > 0):
        pwr2 += 10*output
        pwr3 -= 10*output
        pwr4 -= 10*output
        pwr1 += 10*output
     if(pitchout < 0):
        pwr2 -= 10*output
        pwr3 += 10*output
        pwr4 += 10*output
        pwr1 -= 10*output
     if(heightout > 0):
        pwr2 += 10*output
        pwr3 += 10*output
        pwr4 += 10*output
        pwr1 += 10*output
     if(heightout < 0):
        pwr2 -= 10*output
        pwr3 -= 10*output
        pwr4 += 10*output
        pwr1 += 10*output
     if(output < 0):
        pwr2 -= 10*output
        pwr3 -= 10*output
        pwr4 += 10*output
        pwr1 += 10*output

     pi.set_servo_pulsewidth(ESC1,pwr1)
     pi.set_servo_pulsewidth(ESC2,pwr2)
     pi.set_servo_pulsewidth(ESC3,pwr3)
     pi.set_servo_pulsewidth(ESC4,pwr4)
    
     
    


     
