import pyautogui
import time

time.sleep(1)
pyautogui.press("win")
pyautogui.write("league")
pyautogui.press("enter")
time.sleep(30)
pyautogui.moveTo(319,98) # Play Button
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(1126,349) # TFT Button
pyautogui.leftClick()
time.sleep(2)
pyautogui.moveTo(1035,746) # Ranked Button
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

