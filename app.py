import RPi.GPIO as GPIO
from flask import Flask, redirect
from markupsafe import escape

speedEnabled = True

# todo:
# - add deployment instructions

# GPIO setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
if speedEnabled:
    left = GPIO.PWM(8, 1000)
    right = GPIO.PWM(7, 1000)
    left.start(0)
    right.start(0)
else:
    print("Speed disabled")

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Connected</p>"

@app.route("/<stickX>/<stickY>")
def move(stickX, stickY):
    print(f"{escape(stickX)} {escape(stickY)}")
    if int(stickY) > 0:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)       
        if speedEnabled:
            left.ChangeDutyCycle(int(stickY)*0.99)
            right.ChangeDutyCycle(int(stickY))
        else:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
        print("forwards")  
    elif int(stickY) < 0:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
        if speedEnabled:
            left.ChangeDutyCycle(int(stickY)*-1)
            right.ChangeDutyCycle(int(stickY)*-1)
        else:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
        print("backwards")  
    elif int(stickX) > 0:
        GPIO.output(18, GPIO.LOW)
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(25, GPIO.LOW)
        if speedEnabled:
            left.ChangeDutyCycle(int(stickX))
            right.ChangeDutyCycle(int(stickX))
        else:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
        print("right") 
    elif int(stickX) < 0:
        GPIO.output(18, GPIO.HIGH)
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(25, GPIO.HIGH)
        if speedEnabled:
            left.ChangeDutyCycle(int(stickX)*-1)
            right.ChangeDutyCycle(int(stickX)*-1)
        else:
            GPIO.output(8, GPIO.HIGH)
            GPIO.output(7, GPIO.HIGH)
        print("left") 
    else:
        if speedEnabled:
            left.ChangeDutyCycle(0)
            right.ChangeDutyCycle(0)
        else:
            GPIO.output(8, GPIO.LOW)
            GPIO.output(7, GPIO.LOW)
        print("stop")

    
    return redirect("/")