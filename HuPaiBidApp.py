from HuPaiBidGui import HuPaiBidGui
import tkinter as tk
import time
import threading
from Config import *
try:
    from PIL import Image
except ImportError:
    import Image
from BidPage import BidPage


class HuPaiBidApp(HuPaiBidGui):
    def __init__(self):
        HuPaiBidGui.__init__(self)

        self.debug = False
        self.first_bid_is_processed = False
        self.second_bid_is_processed = False
        self.is_screnn_calibration_process = False
        self.is_price_calibration_process = False

        self.bidpage = BidPage()

        self.current_price = 0
        self.current_time = 0

        self.event = threading.Event()
        self.update_time_t = threading.Thread(
            target=self.update_time, args=())
        self.update_time_t.setDaemon(True)
        self.update_time_t.start()
        self.update_price_display_t = threading.Thread(
            target=self.update_price_display, args=())
        self.update_price_display_t.setDaemon(True)
        self.update_price_display_t.start()
        self.refresh_verify_code_t = threading.Thread(
            target=self.refresh_verify_code, args=())
        self.refresh_verify_code_t.setDaemon(True)
        self.refresh_verify_code_t.start()

        self.mainloop()

    def update_time(self):
        while True:
            try:
                if self.debug:
                    self.current_time = time.time() - self.debug_start_time + DBG_TIMESTAMP + \
                        float(self.time_drift_entry.get())
                else:
                    self.current_time = time.time() + float(self.time_drift_entry.get())
                current_time_str = time.strftime(
                    "%H:%M:%S", time.localtime(self.current_time))
                self.current_time_text.set(current_time_str)

                if current_time_str == (f"11:29:{self.first_bid_time_entry_text.get()}"):
                    if not self.first_bid_is_processed:
                        self.first_bid_is_processed = True
                        self.first_bid_t = threading.Thread(
                            target=self.first_bid_handle, args=())
                        self.first_bid_t.setDaemon(True)
                        self.first_bid_t.start()

                if current_time_str == (f"11:29:{self.second_bid_time_entry_text.get()}"):
                    if not self.second_bid_is_processed:
                        self.second_bid_is_processed = True
                        self.second_bid_t = threading.Thread(
                            target=self.second_bid_handle, args=())
                        self.second_bid_t.setDaemon(True)
                        self.second_bid_t.start()

                time.sleep(0.05)
            except:
                pass

    def update_price_display(self):
        self.event.wait()

        while True:
            try:
                self.bidpage.before_get_price()
                self.current_price = self.bidpage.get_price(
                    self.bidpage.price_area)
                self.current_price_text.set(self.current_price)
                self.current_price_display_lbl.configure(foreground="black")
            except:
                self.current_price_display_lbl.configure(foreground="red")
                self.current_price = 0
                self.current_price_text.set("00000")

    def refresh_verify_code(self):
        while True:
            self.bidpage.refresh_verify_code('+')

    def first_bid_handle(self):
        self.my_target_price = self.current_price + \
            int(self.first_bid_price_entry_text.get())
        self.update_log_display(
            f"{time.strftime('%H:%M:%S', time.localtime(self.current_time))}: {self.my_target_price}")

        self.bidpage.rise_price(self.my_target_price)
        self.bidpage.before_bid()
        self.bidpage.wait_for_finish_verify_code()
        self.bidpage.bid()
        self.bidpage.after_bid()

    def second_bid_handle(self):
        self.my_target_price = self.current_price + \
            int(self.second_bid_price_entry_text.get())
        self.update_log_display(
            f"{time.strftime('%H:%M:%S', time.localtime(self.current_time))}: {self.my_target_price}")

        self.bidpage.rise_price(self.my_target_price)
        self.bidpage.before_bid()
        self.bidpage.wait_for_finish_verify_code()

        self.update_log_display("等待出价...")
        while True:
            if (self.current_price + 300 >= self.my_target_price) or (self.current_time % 60 >= float(self.force_submit_entry_text.get())):
                self.bidpage.bid()
                self.update_log_display(
                    f"触发时间:{self.current_time % 60:.2f} \n触发价格:{self.current_price}")
                break

        self.update_log_display("祝好运!")
        self.bidpage.after_bid()

    def debug_start(self):
        self.debug = True
        self.debug_start_time = time.time()
        self.first_bid_is_processed = False
        self.second_bid_is_processed = False

        self.clear_log_display()
        self.update_log_display("模拟竞标开始")

    def release_start(self):
        self.debug = False
        self.first_bid_is_processed = False
        self.second_bid_is_processed = False

        self.clear_log_display()
        self.update_log_display("实战竞标开始")

    def screnn_calibration_process(self):
        self.bidpage.wait_for_find_zero()
        self.bidpage.set_zero()
        self.bidpage.check_zero()

        self.is_screnn_calibration_process = False

    def screnn_coordinate_calibration(self):
        if not self.is_screnn_calibration_process:
            self.is_screnn_calibration_process = True
            HuPaiBidGui.screnn_coordinate_calibration(self)
            self.update_log_display("找寻屏幕零点...")

            threading.Thread(
                target=self.screnn_calibration_process, args=()).start()

    def price_calibration_process(self):
        self.bidpage.wait_for_find_zero()
        self.bidpage.set_price_zero()
        self.bidpage.check_price_zero()

        self.is_price_calibration_process = False

    def price_coordinate_calibration(self):
        if not self.is_price_calibration_process:
            self.is_price_calibration_process = True
            HuPaiBidGui.price_coordinate_calibration(self)
            self.update_log_display("找寻价格零点...")

            threading.Thread(
                target=self.price_calibration_process, args=()).start()

        self.event.set()

    def about(self):
        tk.messagebox.showinfo('关于', 'Python版拍牌小助手\nwmpluto@gmail.com')
