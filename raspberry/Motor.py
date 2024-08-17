import RPi.GPIO as GPIO
import time

in1 = 24
in2 = 23
en = 25
temp1 = 1

GPIO.setmode(GPIO.BCM)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(en, GPIO.OUT)
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p = GPIO.PWM(en, 1000)

p.start(0)  #  Initially set the PWM signal to 0, stop the motor completely

def run(command):
        if command == 'start':
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                en.ChangeDutyCycle(50)  # %50 speed
        elif command == 'stop':
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.LOW)
                en.ChangeDutyCycle(0)  # stop the motor
        elif command == 'backward':
                GPIO.output(in1, GPIO.LOW)
                GPIO.output(in2, GPIO.HIGH)
                en.ChangeDutyCycle(50)  # %50 speed
        elif command == 'forward':
                GPIO.output(in1, GPIO.HIGH)
                GPIO.output(in2, GPIO.LOW)
                en.ChangeDutyCycle(50)  # %50 speed
    

def motor_control(command):
        if command == 'D':
                run('stop')
                time.sleep(2)
        elif command == 'B':
                run('start')
                time.sleep(2)
        elif command == 'F':
                run('forward')
                time.sleep(2)
        elif command == 'A':
                run('backward')
                time.sleep(2)
        else:
                print("Please press a buton")
        
def cleanup():
        p.stop()
        GPIO.cleanup() 
