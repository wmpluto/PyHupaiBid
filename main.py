import time
import keyboard
import pyautogui
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

RELEASE = False
PRICE_AREA = (732, 538, 141, 40)
print("Good Luck!")

pytesseract.pytesseract.tesseract_cmd = r'D:/tmp/hupai/tesseract-v5/tesseract.exe'

while True:
    if (RELEASE):
        ## Wait for 11:29:57
        while(time.time() % 60 < 57.2):
            time.sleep(0.1)
    else:
        print("Press enter when it's 11:29:10: ")
        keyboard.wait('enter')
        start_time = time.time()
        print("...")
        ## time.sleep(47-0.2)
        while(time.time() < (start_time + 47 - 0.2)):
            price_img = pyautogui.screenshot(region = PRICE_AREA)
            r = pytesseract.image_to_string(price_img, config='outputbase digits')
            print(r) 

    pyautogui.click()
    print(time.asctime(time.localtime(time.time())))
    time.sleep(0.6)
