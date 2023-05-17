from pynput.keyboard import Key, Controller
import time
import tkinter as tk

trueCont = True
keyboard = Controller()
counterFix = 0


def startAuto():
    global counterFix
    print(counterFix)
    if counterFix == 0:
        counterFix += 1
        return
    while trueCont == True:
        keyboard.press(Key.f5)
        keyboard.release(Key.f5)
        time.sleep(5)

def restartAuto():
    print("RESTART")
    trueCont = True

def stopAuto():
    print("STOP")
    trueCont = False


def main():
    #global counterFix
    global window
    window = tk.Tk()
    window.geometry('250x150')
    startButton = tk.Button(window, text = "START AUTOSAVER", command = startAuto)
    startButton.pack()

    stopButton = tk.Button(window, text = "RESTART AUTOSAVER", command = stopAuto)
    stopButton.pack()

    restartButton = tk.Button(window, text = "STOP AUTOSAVER", command = restartAuto)
    restartButton.pack()

    window.mainloop()

main()
