from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

while True:
    keyboard.press(Key.f5)
    keyboard.release(Key.f5)
    time.sleep(5)