from itertools import count

import pyautogui
import  time
count = 1
time.sleep(3)
while True:
    pyautogui.hotkey('ctrl','r' )
    print(f"已刷新{count}次")
    count += 1
    time.sleep(10)