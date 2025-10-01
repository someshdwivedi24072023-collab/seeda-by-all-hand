import pyautogui;
import time;
pyautogui.FAILSAFE=False
while True:
    time.sleep(5)
    for i in range(0,2):
     pyautogui.leftClick()