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

    # Use hardware PWM for h_sync_pin
    pi.hardware_PWM(h_sync_pin, h_sync, 500000)  # 50% duty cycle

    # Use software PWM for v_sync_pin
    pi.set_PWM_frequency(v_sync_pin, v_sync)
    pi.set_PWM_dutycycle(v_sync_pin, 128)  # 50% duty cycle (128/255)

if __name__ == '__main__':
    show_image()

    for i in range(10):
        time.sleep(1)