import pyautogui # pip install pyautogui
import pyscreenshot as ImageGrab
from PIL import Image # pip install pillow
import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    for i in range(300, 415): #range values are system dependent
        for j in range(410, 563): #range values are system dependent
            if data[i, j] < 100:
                hit("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey, Mr. Engineer Dino game about to start in 3 seconds")
    time.sleep(3)
    hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        isCollide(data)
        
        