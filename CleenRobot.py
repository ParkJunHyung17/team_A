import RPi.GPIO as GPIO
import time

servo_pin = 18
rain_pin = 26


in1 = 24
in2 = 23
in3 = 5
in4 = 6
en1 = 25
en2 = 13
temp1=1

GPIO.setmode(GPIO.BCM)
GPIO.setup(rain_pin, GPIO.IN)

#server motor
GPIO.setup(servo_pin, GPIO.OUT)
pwm = GPIO.PWM(servo_pin, 50)  # 50Hz

#mortor
GPIO.setmode(GPIO.BCM)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(en1,GPIO.OUT)
GPIO.setup(en2,GPIO.OUT)
p1=GPIO.PWM(en1,10)
p2=GPIO.PWM(en2,10)

def workwheel():
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        
def workwater():
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)

def stopwheel():
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        
def stopwater():
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)

def workbrush():
    time.sleep(1)
    pwm.start(3.0)
    
def stopbrush():
    time.sleep(1)
    pwm.stop()

def israining():
    rain = GPIO.input(rain_pin)
    if rain == 0:
        print("raining")
        p1.start(25)
        p2.start(25)
        workwheel()
        workwater()
        workbrush()
        
        
    if rain == 1:
        print("not raining")
        stopbrush()
        stopwater()
        stopwheel()
while True:
    israining()
    
        

#GPIO.cleanup()    