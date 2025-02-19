import RPi.GPIO as GPIO
import time

def show_image():
    h_sync = 18430
    v_sync = 50
    h_pixels = 720
    v_pixels = 350
    h_sync_pin = 8
    v_sync_pin = 19
    intensity_pin = 18
    video_pin = 12

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(h_sync_pin, GPIO.OUT)
    GPIO.setup(v_sync_pin, GPIO.OUT)
    GPIO.setup(intensity_pin, GPIO.OUT)
    GPIO.setup(video_pin, GPIO.OUT)

    h_pwm = GPIO.PWM(h_sync_pin, 1000)
    v_pwm = GPIO.PWM(v_sync_pin, v_sync)
    h_pwm.start(0)
    v_pwm.start(0)




if __name__ == '__main__':
    show_image()

    for i in range(10):
        time.sleep(1)