import time

DRIFT = - 0.2
CAL_DELAY = 0.5
OPERATION_DELAY = 0.2

DBG_TIME = "2020-6-21 11:29:10"
DBG_TIMESTAMP = int(time.mktime(time.strptime(DBG_TIME, "%Y-%m-%d %H:%M:%S")))

LEFT_AREA_DELTA = (0, 190, 400, 200)
RIGHT_AREA_DELTA = (400, 100, 500, 400)

BID_BUTTON_PNG = "./img/bid-button.png"
CANCEL_BUTTON_PNG = './img/cancel-button.png'
CUSTOM_PRICE_INPUT_PNG = './img/custom-price-input.png'
PRICE_300_BUTTON_PNG = './img/price-300-button.png'
RISE_PRISE_BUTTON_PNG = './img/rise-prise-button.png'
SUBMIT_BUTTON_PNG = './img/submit-button.png'
VERIFICATION_CODE_INPUT_PNG = './img/verification-code-input.png'
CONFIRM_AFTER_BID_BUTTON_PNG = './img/confirm-after-bid-button.png'
SUBMIT_CANCEL_CONFIRM_BUTTON_PNG = "./img/submit-cancel-confirm-button.png"
RMB_ICON_PNG = "./img/rmb.png"


CUSTOM_ADD_PRICE_INPUT_POS_DELTA = (652, 148)
RISE_PRICE_BUTTON_POS_DELTA = (767, 148)
PRICE_300_BUTTON_POS_DELTA = (614, 218)
CUSTOM_PRICE_INPUT_POS_DELTA = (614, 255)
BID_BUTTON_POS_DELTA = (767, 255)
VER_CODE_DISPLAY_POS_DELTA = (532, 255)
VER_CODE_INPUT_POS_DELTA = (708, 257)
CONFIRM_AFTER_BID_BUTTON_POS_DELTA = (635, 322)