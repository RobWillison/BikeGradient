from time import sleep
import RPi.GPIO as GPIO           # Allows us to call our GPIO pins and names it just GPIO
import redis

GPIO.setmode(GPIO.BCM)

sense_pin = 22
GPIO.setup(sense_pin, GPIO.IN)

upPin = 17
downPin = 27

GPIO.setup(upPin, GPIO.OUT)
GPIO.setup(downPin, GPIO.OUT)

current = False
pos = 0

GPIO.output(downPin, GPIO.LOW)
GPIO.output(upPin, GPIO.LOW)

r = redis.Redis(host='localhost', port=6379, db=0)

direction = 1

while True:
    target = int(r.get('foo') or 0)
    if pos < target:
        GPIO.output(downPin, GPIO.LOW)
        GPIO.output(upPin, GPIO.HIGH)
        direction = 1
    if pos > target:
        GPIO.output(downPin, GPIO.HIGH)
        GPIO.output(upPin, GPIO.LOW)
        direction = -1
    if pos == target:
        direction = 0
        GPIO.output(downPin, GPIO.LOW)
        GPIO.output(upPin, GPIO.LOW)

    if GPIO.input(sense_pin) and not current:
        current = True
        pos += direction
        print(pos)
    if not GPIO.input(sense_pin):
        current = False
    sleep(0.01)

GPIO.output(upPin, GPIO.LOW)
GPIO.output(downPin, GPIO.LOW)

GPIO.cleanup()
