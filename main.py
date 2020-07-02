import time
import keyboard
import pyautogui

RELEASE = False

print("Good Luck!")

while True:
    if (RELEASE):
        ## Wait for 11:29:57
        while(time.time() % 60 < 57.2):
            time.sleep(0.1)
    else:
        print("Press enter when it's 11:29:10: ")
        keyboard.wait('enter')
        print("...")
        ## Wait for 47 seconds
        time.sleep(47-0.2)

    pyautogui.click()
    print(time.asctime(time.localtime(time.time())))
    time.sleep(0.6)
