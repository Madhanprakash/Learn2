import pyautogui
import time

pyautogui.typewrite("Hello, this is an automated message!", interval=0.1)
time.sleep(1)

screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")   
print("Screenshot saved successfully")
