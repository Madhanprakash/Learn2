import pyautogui
import time

pyautogui.FAILSAFE = True
print("Move the mouse away from any screen corner. Moving to (100, 100) in 2 seconds...")
time.sleep(2)

pyautogui.moveTo(100, 100, duration=1)
print("Mouse moved successfully")

pyautogui.scroll(500)
print("Scroll performed successfully")

pyautogui.rightClick(100, 100)
print("Right-click performed successfully")

pyautogui.doubleClick(100, 100)
print("Double-click performed successfully")        

pyautogui.leftClick(100, 100)
print("Left-click performed successfully")  
