import tkinter.messagebox
from tkinter import ttk
import tkinter as tk
import tkinter.scrolledtext as tkst


class HuPaiBidGui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("中标")
        self.root.wm_attributes('-topmost', 1)
        self.root.resizable(0, 0)
        self.create_menu()
        self.creat_widgets()

    def mainloop(self):
        self.root.mainloop()

    def create_menu(self):
        menu_bar = tk.Menu(self.root)
        menu_bar.add_command(label="关于", command=self.about)
        self.root['menu'] = menu_bar

    def creat_widgets(self):
        self.frame_one = tk.Frame(self.root)

        self.debug_start_btn = ttk.Button(
            self.frame_one, text="模拟", width=5, command=self.debug_start)
        self.debug_start_btn.pack(side=tk.LEFT, padx=1, pady=1)
        self.release_start_btn = ttk.Button(
            self.frame_one, text="实战", width=5, command=self.release_start)
        self.release_start_btn.pack(side=tk.LEFT, padx=1, pady=1)
        self.time_drift_lbl = ttk.Label(self.frame_one, text="时间微调:")
        self.time_drift_lbl.pack(side=tk.LEFT, padx=1, pady=1)
        self.time_drift_entry = ttk.Entry(
            self.frame_one, width=5, justify=tk.RIGHT)
        self.time_drift_entry.pack(side=tk.LEFT, padx=1, pady=1)
        self.time_drift_entry.insert(tk.END, '0')
        self.drift_unit_lbl = ttk.Label(self.frame_one, text="秒")
        self.drift_unit_lbl.pack(side=tk.LEFT, padx=1, pady=1)

        self.frame_one.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)

        self.frame_two = tk.Frame(self.root)

        self.current_time_lbl = ttk.Label(self.frame_two, text="当前时间:")
        self.current_time_lbl.pack(side=tk.LEFT, padx=1, pady=1)
        self.current_time_text = tk.StringVar()
        self.current_time_display_lbl = ttk.Label(
            self.frame_two, relief="groove", textvariable=self.current_time_text)
        self.current_time_text.set("11:29:00")
        self.current_time_display_lbl.pack(side=tk.LEFT, padx=1, pady=1)
        self.current_price_lbl = ttk.Label(self.frame_two, text="当前价格:")
        self.current_price_lbl.pack(side=tk.LEFT, padx=1, pady=1)
        self.current_price_text = tk.StringVar()
        self.current_price_display_lbl = ttk.Label(
            self.frame_two, relief="groove", textvariable=self.current_price_text)
        self.current_price_text.set("00000")
        self.current_price_display_lbl.pack(side=tk.LEFT, padx=1, pady=1)

        self.frame_two.pack(side=tk.TOP)
        self.frame_two.update()

        self.frame_three = tk.Frame(self.root)

        self.screnn_coordinate_calibration_btn = ttk.Button(
            self.frame_three, text="屏幕校准(N)", command=self.screnn_coordinate_calibration)
        self.screnn_coordinate_calibration_btn.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=1, pady=1)
        self.price_coordinate_calibration_btn = ttk.Button(
            self.frame_three, text="价格校准(N)", command=self.price_coordinate_calibration)
        self.price_coordinate_calibration_btn.pack(
            side=tk.LEFT, expand=tk.YES, fill=tk.X, padx=1, pady=1)

        self.frame_three.pack(side=tk.TOP, expand=tk.YES, fill=tk.X)

        self.frame_four = tk.Frame(self.root)

        self.frame_four_time_icon_lbl = ttk.Label(self.frame_four, text="预定时间")
        self.frame_four_time_icon_lbl.grid(
            row=0, column=1, columnspan=2, padx=1, pady=1)
        self.frame_four_price_icon_lbl = ttk.Label(
            self.frame_four, text="自定义加价")
        self.frame_four_price_icon_lbl.grid(row=0, column=3, padx=1, pady=1)

        self.first_bid_lbl = ttk.Label(self.frame_four, text="第一次出价: ")
        self.first_bid_lbl.grid(row=1, column=0, padx=1, pady=1)
        self.first_bid_time_prefix_lbl = ttk.Label(
            self.frame_four, text="11:29:")
        self.first_bid_time_prefix_lbl.grid(row=1, column=1, padx=1, pady=1)
        self.first_bid_time_entry_text = tk.StringVar()
        self.first_bid_time_entry = ttk.Entry(
            self.frame_four, width=3, justify=tk.LEFT, textvariable=self.first_bid_time_entry_text)
        self.first_bid_time_entry_text.set("30")
        self.first_bid_time_entry.grid(row=1, column=2, padx=1, pady=1)
        self.first_bid_price_entry_text = tk.StringVar()
        self.first_bid_price_entry_text.set("300")
        self.first_bid_price_entry = ttk.Entry(
            self.frame_four, width=5, justify=tk.RIGHT, state='readonly', textvariable=self.first_bid_price_entry_text)
        self.first_bid_price_entry.grid(row=1, column=3, padx=1, pady=1)

        self.second_bid_lbl = ttk.Label(self.frame_four, text="第二次出价: ")
        self.second_bid_lbl.grid(row=2, column=0, padx=1, pady=1)
        self.second_bid_time_prefix_lbl = ttk.Label(
            self.frame_four, text="11:29:")
        self.second_bid_time_prefix_lbl.grid(row=2, column=1, padx=1, pady=1)
        self.second_bid_time_entry_text = tk.StringVar()
        self.second_bid_time_entry = ttk.Entry(
            self.frame_four, width=3, justify=tk.LEFT, textvariable=self.second_bid_time_entry_text)
        self.second_bid_time_entry_text.set("48")
        self.second_bid_time_entry.grid(row=2, column=2, padx=1, pady=1)
        self.second_bid_price_entry_text = tk.StringVar()
        self.second_bid_price_entry_text.set("600")
        self.second_bid_price_entry = ttk.Entry(
            self.frame_four, width=5, justify=tk.RIGHT, textvariable=self.second_bid_price_entry_text)
        self.second_bid_price_entry.grid(row=2, column=3, padx=1, pady=1)

        self.force_submit_time_lbl = ttk.Label(self.frame_four, text="强制提交: ")
        self.force_submit_time_lbl.grid(row=3, column=0, padx=1, pady=1, sticky=tk.E)
        self.second_bid_time_prefix_lbl = ttk.Label(
            self.frame_four, text="11:29:")
        self.second_bid_time_prefix_lbl.grid(row=3, column=1, padx=1, pady=1)
        self.force_submit_entry_text = tk.StringVar()
        self.force_submit_entry_text.set("57")
        self.force_submit_entry = ttk.Entry(
            self.frame_four, width=5, justify=tk.RIGHT, textvariable=self.force_submit_entry_text)
        self.force_submit_entry.grid(row=3, column=2, padx=1, pady=1, columnspan=2, sticky=tk.W)
        
        self.frame_four.pack(side=tk.TOP)

        self.frame_five = tk.Frame(
            self.root, width=self.frame_two.winfo_width(), height=90)
        self.frame_five.pack_propagate(0)

        self.log_display_text = tkst.ScrolledText(
            self.frame_five, wrap=tk.WORD)
        self.log_display_text.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH, padx=0, pady=1)

        self.frame_five.pack(side=tk.TOP)
 

    def screnn_coordinate_calibration(self):
        self.screnn_coordinate_calibration_btn['text'] = '屏幕校准(Y)'

    def price_coordinate_calibration(self):
        self.price_coordinate_calibration_btn['text'] = '价格校准(Y)'

    def debug_start(self):
        pass

    def release_start(self):
        pass

    def about(self):
        pass
