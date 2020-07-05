from Config import *
import pyautogui as auto
import keyboard
import time

class BidPage():
    def __init__(self):
        self.zero = (0, 0)

        self.custom_price_input_pos = (0, 0)
        self.rise_prise_button_pos = (0, 0)
        self.price_300_button_pos = (0, 0)
        self.bid_button_pos = (0, 0)

    def set_zero(self):
        x, y = auto.position()
        self.zero = (x, y)
        print(self.zero)
        self.custom_price_input_pos = (CUSTOM_PRICE_INPUT_POS_DELTA[0] + x, CUSTOM_PRICE_INPUT_POS_DELTA[1] + y)
        self.rise_prise_button_pos = (RISE_PRISE_BUTTON_POS_DELTA[0] + x, RISE_PRISE_BUTTON_POS_DELTA[1] + y)
        self.price_300_button_pos = (PRICE_300_BUTTON_POS_DELTA[0] + x, PRICE_300_BUTTON_POS_DELTA[1] + y)
        self.bid_button_pos = (BID_BUTTON_POS_DELTA[0] + x, BID_BUTTON_POS_DELTA[1] + y)    
        self.ver_code_input_pos = (VER_CODE_INPUT_POS_DELTA[0] + x, VER_CODE_INPUT_POS_DELTA[1] + y)    
        self.ver_code_display_pos = (VER_CODE_DISPLAY_POS_DELTA[0] + x, VER_CODE_DISPLAY_POS_DELTA[1] + y)
        self.confirm_after_bid_button_pos = (CONFIRM_AFTER_BID_BUTTON_POS_DELTA[0] + x, CONFIRM_AFTER_BID_BUTTON_POS_DELTA[1] + y)

    def check_zero(self):
        auto.moveTo(self.custom_price_input_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.rise_prise_button_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.price_300_button_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.bid_button_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.ver_code_input_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.ver_code_display_pos)
        time.sleep(CAL_DELAY)
        auto.moveTo(self.confirm_after_bid_button_pos)
        time.sleep(CAL_DELAY)


def first_bid():
    bidpage = BidPage()
    print("seting zero")
    keyboard.wait('enter')
    bidpage.set_zero()
    bidpage.check_zero()

    print("30s 出价")
    auto.click(bidpage.price_300_button_pos)
    time.sleep(0.5)
    auto.click(bidpage.bid_button_pos)

    time.sleep(0.1)
    auto.click(bidpage.ver_code_input_pos) 
    print("等验证码")
    keyboard.wait('enter')

    submit_cancel_areas = auto.locateAllOnScreen(SUBMIT_CANCEL_CONFIRM_BUTTON_PNG, region=(900, 300, 500, 400), confidence=0.9)
    submit_button_area = (1980, 0, 0, 0)
    for pos in submit_cancel_areas:
        if (pos[0] <= submit_button_area[0]):
            submit_button_area = pos
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


def main():
    bidpage = BidPage()
    while True:
        print("seting zero")
        keyboard.wait('enter')
        bidpage.set_zero()
        bidpage.check_zero()

if __name__ == "__main__":
    first_bid()