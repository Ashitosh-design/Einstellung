#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.25.1
#  in conjunction with Tcl version 8.6
#    Nov 21, 2019 01:42:51 PM IST  platform: Windows NT

import sys
import RPi.GPIO as GPIO
import time
import tkinter.messagebox as Messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def gpio():
    print('Nitin_support.gpio')
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, 1) #On initially
    time.sleep(5)
    GPIO.output(17, 0) #Off initially
    Messagebox.showinfo("GPIO Status", "OFF")
    time.sleep(1)
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Nitin
    Nitin.vp_start_gui()




