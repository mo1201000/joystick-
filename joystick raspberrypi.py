import Rpi.Gpio as Gpio
from time import sleep
import pygame

pygame.init()
pygame.joystick.init()
joystick=pygame.joystick.Joystick(0)

#setup the gpio pins
Gpio.setmode(Gpio.borad)
#Gpio.setmode(Gpio.BCM)
Gpio.setwarnings(False)

#declare  the pins off frist  motors
motorA1=2
motorA2=3
motorA3=4
#declare  the pins offsecond  motors
motorB1=5
motorB2=6
motorB3=7
#declare  the pins offthrid motors
motorC1=2
motorC2=3
motorC3=4
#declare  the pins off four  motors
motorD1=2
motorD2=3
motorD3=4

#declare  the pins off fifth  motors
motorE1=2
motorE2=3
motorE3=4

#declare  the pins off Sixthly  motors
motorF1=2
motorF2=3
motorF3=4

#declare  the pins off VII  motors
motorG1=2
motorG2=3
motorG3=4

#declare  the pins off Eighth  motors
motorZ1=2
motorZ2=3
motorZ3=4


#set the pins as output
Gpio.setup(motorA1,Gpio.OUT)
Gpio.setup(motorA2,Gpio.OUT)
Gpio.setup(motorA3,Gpio.OUT)

Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)
Gpio.setup(motorB1,Gpio.OUT)


Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)
Gpio.setup(motorC1,Gpio.OUT)

Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)
Gpio.setup(motorD1,Gpio.OUT)

Gpio.setup(motorE1,Gpio.OUT)
Gpio.setup(motorE2,Gpio.OUT)
Gpio.setup(motorE3,Gpio.OUT)

Gpio.setup(motorF1,Gpio.OUT)
Gpio.setup(motorF2,Gpio.OUT)
Gpio.setup(motorF3,Gpio.OUT)

Gpio.setup(motorG1,Gpio.OUT)
Gpio.setup(motorG2,Gpio.OUT)
Gpio.setup(motorG3,Gpio.OUT)

Gpio.setup(motorZ1,Gpio.OUT)
Gpio.setup(motorZ2,Gpio.OUT)
Gpio.setup(motorZ3,Gpio.OUT)

#set the pwm pins
R1=Gpio.PWM(motorA3,150)
R2=Gpio.PWM(motorB3,150)
R3=Gpio.PWM(motorC3,150)
R4=Gpio.PWM(motorD3,150)
R5=Gpio.PWM(motorE3,150)
R6=Gpio.PWM(motorF3,150)
R7=Gpio.PWM(motorG3,150)
R8=Gpio.PWM(motorZ3,150)

#The main code
while(1):
   
   pygame.event.pump()
   Yvert=joystick.get_axis(1)
   Xhorz=joystick.get_axis(0)

   if Yvert<0:
    print('UP')
    y=abs(Yvert*100)
    print(y)
    Gpio.setup(motorA1,Gpio.LOW)
    Gpio.setup(motorA2,Gpio.HIGH)
    Gpio.setup(motorA3,Gpio.HIGH)
    R1.start(y)

    Gpio.setup(motorB1,Gpio.LOW)
    Gpio.setup(motorB2,Gpio.HIGH)
    Gpio.setup(motorB3,Gpio.HIGH)
    R2.start(y)

    Gpio.setup(motorC1,Gpio.LOW)
    Gpio.setup(motorC2,Gpio.HIGH)
    Gpio.setup(motorC3,Gpio.OUT)
    R3.start(y)

    Gpio.setup(motorD1,Gpio.LOW)
    Gpio.setup(motorD2,Gpio.HIGH)
    Gpio.setup(motorD3,Gpio.HIGH)
    R4.start(y)

   elif Yvert>0 :
     print('DOWN')
     y=abs(Yvert*100)
     print(y)
     Gpio.setup(motorA1,Gpio.HIGH)
     Gpio.setup(motorA2,Gpio.LOW)
     Gpio.setup(motorA3,Gpio.HIGH)
     R1.start(y)

     Gpio.setup(motorB1,Gpio.HIGH)
     Gpio.setup(motorB2,Gpio.LOW)
     Gpio.setup(motorB3,Gpio.HIGH)
     R2.start(y)

     Gpio.setup(motorC1,Gpio.HIGH)
     Gpio.setup(motorC2,Gpio.LOW)
     Gpio.setup(motorC3,Gpio.HIGH)
     R3.start(y)

     Gpio.setup(motorD1,Gpio.HIGH)
     Gpio.setup(motorD2,Gpio.LOW)
     Gpio.setup(motorD3,Gpio.HIGH)
     R4.start(y)

   elif Xhorz>0 :
     print('right')
     y=abs(Xhorz*100)
     print(y)
     Gpio.setup(motorE1,Gpio.LOW)
     Gpio.setup(motorE2,Gpio.HIGH)
     Gpio.setup(motorE3,Gpio.HIGH)
     R5.start(y)

     Gpio.setup(motorF1,Gpio.LOW)
     Gpio.setup(motorF2,Gpio.HIGH)
     Gpio.setup(motorF3,Gpio.HIGH)
     R6.start(y)

     Gpio.setup(motorG1,Gpio.LOW)
     Gpio.setup(motorG2,Gpio.HIGH)
     Gpio.setup(motorG3,Gpio.HIGH)
     R7.start(y)

     Gpio.setup(motorZ1,Gpio.LOW)
     Gpio.setup(motorZ2,Gpio.HIGH)
     Gpio.setup(motorZ3,Gpio.HIGH)
     R8.start(y)
   elif Xhorz<0:
     print('left')
     y=abs(Xhorz*100)
     print(y)
     Gpio.setup(motorE1,Gpio.HIGH)
     Gpio.setup(motorE2,Gpio.LOW)
     Gpio.setup(motorE3,Gpio.HIGH)
     R5.start(y)

     Gpio.setup(motorF1,Gpio.HIGH)
     Gpio.setup(motorF2,Gpio.LOW)
     Gpio.setup(motorF3,Gpio.HIGH)
     R6.start(y)

     Gpio.setup(motorG1,Gpio.HIGH)
     Gpio.setup(motorG2,Gpio.LOW)
     Gpio.setup(motorG3,Gpio.HIGH)
     R7.start(y)

     Gpio.setup(motorZ1,Gpio.HIGH)
     Gpio.setup(motorZ2,Gpio.LOW)
     Gpio.setup(motorZ3,Gpio.HIGH)
     R8.start(y)

   else:
     Gpio.setup(motorA1,Gpio.LOW)
     Gpio.setup(motorA2,Gpio.LOW)
     Gpio.setup(motorA3,Gpio.LOW)
     Gpio.setup(motorB1,Gpio.LOW)
     Gpio.setup(motorB1,Gpio.LOW)
     Gpio.setup(motorB1,Gpio.LOW)
     Gpio.setup(motorC1,Gpio.LOW)
     Gpio.setup(motorC2,Gpio.LOW)
     Gpio.setup(motorC3,Gpio.LOW)
     Gpio.setup(motorD1,Gpio.LOW)
     Gpio.setup(motorD2,Gpio.LOW)
     Gpio.setup(motorD3,Gpio.LOW)
     Gpio.setup(motorE1,Gpio.LOW)
     Gpio.setup(motorE2,Gpio.LOW)
     Gpio.setup(motorE3,Gpio.LOW)
     Gpio.setup(motorF1,Gpio.LOW)
     Gpio.setup(motorF2,Gpio.LOW)
     Gpio.setup(motorF3,Gpio.LOW)
     Gpio.setup(motorG1,Gpio.LOW)
     Gpio.setup(motorG2,Gpio.LOW)
     Gpio.setup(motorG3,Gpio.LOW)
     Gpio.setup(motorZ1,Gpio.LOW)
     Gpio.setup(motorZ2,Gpio.LOW)
     Gpio.setup(motorZ3,Gpio.LOW)
   sleep(0.3)
Gpio.cleanup()


    


     


     


