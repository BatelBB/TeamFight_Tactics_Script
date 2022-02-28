import pyautogui
import time

time.sleep(1)
pyautogui.moveTo(39,400) # Launcher
pyautogui.doubleClick()
time.sleep(30)
pyautogui.moveTo(319,98) # Play Button
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(954,345) # TFT Button
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(912,701) # Normal Button
pyautogui.leftClick()
time.sleep(1)
pyautogui.moveTo(794,910) # Confirm Button
pyautogui.leftClick()
time.sleep(4)
pyautogui.moveTo(870,910) # Find Match Button
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(977,764) # Accept Match Button
timeout = time.time() + 60
while True: # Because the queue for the match is random, I put an interval up to a minute
    pyautogui.leftClick()
    time.sleep(4)
    time.time() > timeout

