import pyautogui
import time

pyautogui.click(x=1286, y=59)#Click firefox bring it to foreground.
pyautogui.press("altleft")
time.sleep(1)
pyautogui.click(x=368, y=14)#Help
time.sleep(1)
pyautogui.click(x=1008, y=228)#about Firefox