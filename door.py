import requests
import time
import RPi.GPIO as GPIO


def send_notification(message):
    response = requests.post(
    "https://api.pushover.net/1/messages.json",
    data={
        "token": app_token,
        "user": user_key,
        "message": message,
        "device": "Entre door",
    },
    verify=True
)
    print(response.status_code)
    print(response.json())


# Set up the GPIO pin
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(11,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# Replace with your own Pushover user key and app token
user_key = "urhyf5de9ngueg9nnfcvsb1ydpumrh"
app_token = "anpcq2nstk8dojm1c8n3za4wg55hoj"

# Initialize the current state of the pin
current_state = None

# Wait for the pin to be triggered
while True:
    if GPIO.input(7)==1:
        if current_state != "open":
            message = "Door is open"
            send_notification(message)
            current_state = "open"
    elif GPIO.input(7) == 0:
        if current_state != "closed":
            message = "Door is closed"
            send_notification(message)
            current_state = "closed"