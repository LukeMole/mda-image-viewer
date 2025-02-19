import pigpio
import time

def show_image():
    h_sync = 18430
    v_sync = 50
    h_pixels = 720
    v_pixels = 350
    h_sync_pin = 13
    v_sync_pin = 19
    intensity_pin = 18
    video_pin = 12

    pi = pigpio.pi()
    if not pi.connected:
        exit()

    pi.set_mode(h_sync_pin, pigpio.OUTPUT)
    pi.set_mode(v_sync_pin, pigpio.OUTPUT)
    pi.set_mode(intensity_pin, pigpio.OUTPUT)
    pi.set_mode(video_pin, pigpio.OUTPUT)

    pi.hardware_PWM(h_sync_pin, h_sync, 500000)  # 50% duty cycle
    pi.hardware_PWM(v_sync_pin, v_sync, 500000)  # 50% duty cycle

if __name__ == '__main__':
    show_image()

    for i in range(10):
        time.sleep(1)