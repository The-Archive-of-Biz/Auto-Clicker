from ctypes import *
import time

x=input("(1) ai move mouse   or   (2) you move mouse\n")
windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 0)
time.sleep(5)
if x == "1":
    for i in range (10000):
        windll.user32.SetCursorPos(1000,300)
        windll.user32.mouse_event(2,0,0,0,0)
        windll.user32.mouse_event(4,0,0,0,0)
        time.sleep(.01)
    #exit()
if x == "2":
    for i in range (10000):
        windll.user32.mouse_event(2,0,0,0,0)
        windll.user32.mouse_event(4,0,0,0,0)
        time.sleep(.01)
    #exit()

