import time
import _thread
import keyboard
import pyautogui as auto
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

RELEASE = False

DRIFT = - 0.2
CAL_DELAY = 1

BID_BUTTON_PNG = "./img/bid-button.png"
CANCEL_BUTTON_PNG = './img/cancel-button.png'
CUSTOM_PRICE_INPUT_PNG = './img/custom-price-input.png'
PRICE_300_BUTTON_PNG = './img/price-300-button.png'
RISE_PRISE_BUTTON_PNG = './img/rise-prise-button.png'
SUBMIT_BUTTON_PNG = './img/submit-button.png'
VERIFICATION_CODE_INPUT_PNG = './img/verification-code-input.png'
CONFIRM_AFTER_BID_BUTTON_PNG = './img/confirm-after-bid-button.png'
SUBMIT_CANCEL_CONFIRM_BUTTON_PNG = "./img/submit-cancel-confirm-button.png"

bid_button_pos = (0, 0)
cancel_button_pos = (0, 0)
custom_price_input_pos = (0, 0)
price_300_button_pos = (0, 0)
rise_prise_button_pos = (0, 0)
submit_button_pos = (0, 0)
verification_code_input_pos = (0, 0)
confirm_after_bid_button_pos = (0, 0)

def get_pos(img):
    area = auto.locateOnScreen(img, region=(900, 300, 500, 400), confidence=0.9) 
    try:
        center = auto.center(area)
    except:
        center = 0

    return center

def calibration():
    global bid_button_pos
    global cancel_button_pos
    global custom_price_input_pos
    global price_300_button_pos
    global rise_prise_button_pos
    global submit_button_pos
    global verification_code_input_pos

    print("Get rise_prise_button_pos")
    rise_prise_button_pos = get_pos(RISE_PRISE_BUTTON_PNG)
    auto.click(rise_prise_button_pos)
    print(rise_prise_button_pos)
    time.sleep(CAL_DELAY)

    print("Get custom_price_input_pos")
    custom_price_input_pos = get_pos(CUSTOM_PRICE_INPUT_PNG)
    if custom_price_input_pos:
        auto.click(custom_price_input_pos)
        auto.typewrite(message='600',interval=0.2)
        auto.moveTo(custom_price_input_pos)
    else:
        custom_price_input_pos = (rise_prise_button_pos[0] - 100, rise_prise_button_pos[1])
        auto.moveTo(custom_price_input_pos)
    print(custom_price_input_pos)
    time.sleep(CAL_DELAY)

    print("Get price_300_button_pos")
    price_300_button_pos = get_pos(PRICE_300_BUTTON_PNG)
    auto.moveTo(price_300_button_pos)
    print(price_300_button_pos)
    time.sleep(CAL_DELAY)

    print("Get bid_button_pos")
    bid_button_pos = get_pos(BID_BUTTON_PNG)
    auto.moveTo(bid_button_pos)
    print(bid_button_pos)
    time.sleep(CAL_DELAY)

    # print("Get verification_code_input_pos")
    # verification_code_input_pos = get_pos(VERIFICATION_CODE_INPUT_PNG)
    # auto.moveTo(verification_code_input_pos)
    # print(verification_code_input_pos)
    # time.sleep(CAL_DELAY)

    # print("Get submit_button_pos")
    # submit_button_pos = get_pos(SUBMIT_BUTTON_PNG)
    # if not submit_button_pos:
    #     print("need manual calibration")
    #     auto.moveTo((10,10))
    #     keyboard.wait("enter")
    #     submit_button_pos = auto.position()
    # auto.moveTo(submit_button_pos)
    # print(submit_button_pos)
    # time.sleep(CAL_DELAY)

    # print("Get cancel_button_pos")
    # cancel_button_pos = get_pos(CANCEL_BUTTON_PNG)
    # if not cancel_button_pos:
    #     print("need manual calibration")
    #     auto.moveTo((10,10))
    #     keyboard.wait("enter")
    #     cancel_button_pos = auto.position()
    # auto.click(cancel_button_pos)
    # print(cancel_button_pos)
    # time.sleep(CAL_DELAY)

    # submit_cancel_areas = auto.locateAllOnScreen(SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=(900, 300, 500, 400), confidence=0.9)
    # cancel_button_area = (0, 0, 0, 0)
    # for pos in submit_cancel_areas:
    #     if (pos[0] >= cancel_button_area[0]):
    #         cancel_button_area = pos
    # cancel_button_pos = auto.center(cancel_button_area)            
    # auto.moveTo(cancel_button_pos)
    # time.sleep(CAL_DELAY)   
    # auto.click(cancel_button_pos)


def first_bid():
    print("30s 出价")
    auto.click(price_300_button_pos)
    time.sleep(0.5)
    auto.click(bid_button_pos)
    
    print("等验证码")
    keyboard.wait('enter')

    submit_cancel_areas = auto.locateAllOnScreen(SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=(900, 300, 500, 400), confidence=0.9)
    submit_button_area = (1980, 0, 0, 0)
    for pos in submit_cancel_areas:
        if (pos[0] <= submit_button_area[0]):
            submit_button_area = pos
    global submit_button_pos
    submit_button_pos = auto.center(submit_button_area)
    print("出价")
    auto.click(submit_button_pos)

    time.sleep(1)
    confirm_after_bid_button_area = (0, 0, 0, 0)
    submit_cancel_areas = auto.locateAllOnScreen(SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=(900, 300, 500, 400), confidence=0.9)
    for pos in submit_cancel_areas:
        confirm_after_bid_button_area = pos
        break
    confirm_after_bid_button_pos = auto.center(confirm_after_bid_button_area)
    print("确认")
    auto.click(confirm_after_bid_button_pos)

def second_bid():
    print("50s出价")
    auto.click(rise_prise_button_pos)
    time.sleep(0.2)
    auto.click(bid_button_pos)
    
    print("等验证码")
    keyboard.wait('enter')

    submit_cancel_areas = auto.locateAllOnScreen(SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=(900, 300, 500, 400), confidence=0.9)
    submit_button_area = (1980, 0, 0, 0)
    for pos in submit_cancel_areas:
        if (pos[0] <= submit_button_area[0]):
            submit_button_area = pos
    global submit_button_pos
    submit_button_pos = auto.center(submit_button_area)
    print("鼠标定位")
    auto.moveTo(submit_button_pos)

def thread_ocr(name):
    LEFT_AREA = (500, 500, 400, 200)
    RMB_ICON_PNG = "./img/rmb.png"

    RMB_AREA = auto.locateOnScreen('./img/rmb.png', region = LEFT_AREA, confidence=0.9, grayscale=True)

    #PRICE_AREA = (RMB_AREA.left + RMB_AREA.width - 10, RMB_AREA.top - 10, 140, 50)
    #PRICE_AREA = (RMB_AREA.left + RMB_AREA.width, RMB_AREA.top, 140, 40)
    PRICE_AREA = (RMB_AREA.left  + RMB_AREA.width, RMB_AREA.top, 140 , RMB_AREA.height)

    pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'
    while True:
        try:
            price_img = auto.screenshot(region = PRICE_AREA)

            new_img = Image.new(mode='RGB',size=(140*2, 40*2),color=(255,255,255))
            new_img.paste(price_img, (int(140/2), int(40/2)))
            new_img.save("tmp.png")
            r = pytesseract.image_to_string(new_img)
            print(int("".join(list(filter(str.isdigit,r)))))
        except:
            print("OCR Wrong!")

def main():
    print("Good Luck!")

    while True:
        if (RELEASE):
            ## Wait for 11:29:57
            while(time.time() % 60 < 57.2):
                time.sleep(0.1)
        else:
            print("Press enter when it's 11:29:10: ")

            keyboard.wait('enter')
            start_time = time.time()   
            _thread.start_new_thread( thread_ocr, ("price", ))
       
            calibration()
            
            # Wait for 11:29:30
            while(time.time() < (start_time + 20 + DRIFT)):
                time.sleep(0.1)
            first_bid()

            # Wait for 11:29:50
            while(time.time() < (start_time + 40 + DRIFT)):
                time.sleep(0.1)
            second_bid()

            # Wait for 11:29:57
            while(time.time() < (start_time + 47 + DRIFT)):
                time.sleep(0.1)  
            auto.click()          

if __name__ == "__main__":
    main()