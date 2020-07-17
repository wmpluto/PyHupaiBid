from Config import *
import pyautogui as auto
import keyboard
import time
import pytesseract
try:
    from PIL import Image
except ImportError:
    import Image


class BidPage():
    def __init__(self):
        self.zero = (0, 0)
        self.left_area = LEFT_AREA_DELTA
        self.right_area = RIGHT_AREA_DELTA
        self.custom_price_input_pos = (0, 0)
        self.rise_prise_button_pos = (0, 0)
        self.price_300_button_pos = (0, 0)
        self.bid_button_pos = (0, 0)

    def set_zero(self):
        x, y = auto.position()
        self.zero = (x, y)
        self.left_area = (
            LEFT_AREA_DELTA[0] + x, LEFT_AREA_DELTA[1] + y, LEFT_AREA_DELTA[2], LEFT_AREA_DELTA[3])
        self.right_area = (
            RIGHT_AREA_DELTA[0] + x, RIGHT_AREA_DELTA[1] + y, RIGHT_AREA_DELTA[2], RIGHT_AREA_DELTA[3])

        self.custom_add_price_input_pos = (
            CUSTOM_ADD_PRICE_INPUT_POS_DELTA[0] + x, CUSTOM_ADD_PRICE_INPUT_POS_DELTA[1] + y)
        self.rise_price_button_pos = (
            RISE_PRICE_BUTTON_POS_DELTA[0] + x, RISE_PRICE_BUTTON_POS_DELTA[1] + y)
        self.price_300_button_pos = (
            PRICE_300_BUTTON_POS_DELTA[0] + x, PRICE_300_BUTTON_POS_DELTA[1] + y)
        self.custom_price_input_pos = (
            CUSTOM_PRICE_INPUT_POS_DELTA[0] + x, CUSTOM_PRICE_INPUT_POS_DELTA[1] + y)
        self.bid_button_pos = (
            BID_BUTTON_POS_DELTA[0] + x, BID_BUTTON_POS_DELTA[1] + y)
        self.ver_code_input_pos = (
            VER_CODE_INPUT_POS_DELTA[0] + x, VER_CODE_INPUT_POS_DELTA[1] + y)
        self.ver_code_display_pos = (
            VER_CODE_DISPLAY_POS_DELTA[0] + x, VER_CODE_DISPLAY_POS_DELTA[1] + y)
        self.confirm_after_bid_button_pos = (
            CONFIRM_AFTER_BID_BUTTON_POS_DELTA[0] + x, CONFIRM_AFTER_BID_BUTTON_POS_DELTA[1] + y)

    def check_zero(self):
        auto.moveTo(self.custom_add_price_input_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.rise_price_button_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.price_300_button_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.custom_price_input_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.bid_button_pos)
        time.sleep(CAL_DELAY)

    def set_price_zero(self):
        x, y = auto.position()
        self.zero = (x, y)
        self.price_area = (x, y, PRICE_AREA_DELTA[2], PRICE_AREA_DELTA[3])

    def wait_for_finish_verify_code(self):
        keyboard.wait('enter')

    def wait_for_find_zero(self):
        keyboard.wait('enter')

    def rise_price(self, target_price):
        # Input Target Price
        auto.click(self.custom_price_input_pos)
        auto.hotkey('ctrl', 'a')
        auto.press("backspace", interval=0.01)
        auto.typewrite(message=str(target_price), interval=0.01)
        time.sleep(OPERATION_DELAY)

        # Submit
        auto.click(self.bid_button_pos)
        time.sleep(OPERATION_DELAY)

    def before_bid(self):
        auto.click(self.ver_code_input_pos)

        submit_cancel_areas = auto.locateAllOnScreen(
            SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=self.right_area, confidence=0.9)
        submit_button_area = (1980, 0, 0, 0)
        for pos in submit_cancel_areas:
            if (pos[0] <= submit_button_area[0]):
                submit_button_area = pos
        self.submit_button_pos = auto.center(submit_button_area)
        auto.moveTo(self.submit_button_pos)

    def bid(self):
        auto.click(self.submit_button_pos)

    def after_bid(self):
        keyboard.wait('enter')
        confirm_after_bid_button_area = (0, 0, 0, 0)
        submit_cancel_areas = auto.locateAllOnScreen(
            SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=self.right_area, confidence=0.9)
        for pos in submit_cancel_areas:
            confirm_after_bid_button_area = pos
            break
        confirm_after_bid_button_pos = auto.center(
            confirm_after_bid_button_area)
        auto.click(confirm_after_bid_button_pos)

    def before_get_price(self):
        pytesseract.pytesseract.tesseract_cmd = r'./tesseract/tesseract.exe'

        # RMB_AREA = auto.locateOnScreen(
        #     './img/rmb.png', region=self.left_area, confidence=0.9, grayscale=True)
        # return (RMB_AREA.left + RMB_AREA.width, RMB_AREA.top, 140, RMB_AREA.height)

    def get_price(self, price_region):
        price_img = auto.screenshot(region=price_region)

        new_img = Image.new(mode='RGB', size=(
            140*2, 40*2), color=(255, 255, 255))
        new_img.paste(price_img, (int(140/2), int(40/2)))
        # new_img.save("tmp.png")
        r = pytesseract.image_to_string(new_img)
        return int("".join(list(filter(str.isdigit, r.split('\n')[0]))))

    def refresh_verify_code(self, hk):
        keyboard.wait(hk)
        auto.click(self.ver_code_display_pos)
        time.sleep(OPERATION_DELAY)
        auto.click(self.ver_code_input_pos)
        time.sleep(OPERATION_DELAY)
