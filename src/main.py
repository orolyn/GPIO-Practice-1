import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

try:
    for i in range(2):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(17, GPIO.LOW)
        time.sleep(0.5)

    p = GPIO.PWM(17, 50)
    p.start(0)
    p.ChangeDutyCycle(5)

    input('Enter to exit')
    #try:
    #    while True:
    #        for dc in range(0, 101, 5):
    #            p.ChangeDutyCycle(dc)
    #            time.sleep(0.02)
    #        for dc in range(100, -1, -5):
    #            p.ChangeDutyCycle(dc)
    #            time.sleep(0.02)
    #except KeyboardInterrupt:
    #    pass

    p.stop()
finally:
    GPIO.output(17, GPIO.LOW)
    GPIO.cleanup()