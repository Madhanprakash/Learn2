import pyautogui
import time

pyautogui.typewrite("Hello, this is an automated message!", interval=0.1)
time.sleep(1)

pyautogui.hotkey('cmd', 'c')  
print("Hotkey 'cmd + c' pressed successfully")
pyautogui.hotkey('cmd', 'v')
print("Hotkey 'cmd + v' pressed successfully")
