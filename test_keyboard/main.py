import keyboard
import time

while not keyboard.is_pressed("esc"):
    print("wait esc")
    time.sleep(1)

exit(1)

print(1)