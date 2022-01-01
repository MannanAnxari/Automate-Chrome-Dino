import pyautogui
import time
import PIL
from PIL import Image, ImageGrab

def hit(key):
    press = pyautogui.keyDown(key)
    return press

def jump():
    for x in range(370, 410):
        for y in range(413, 490):
            if data[x, y] > 100:
                hit("up")
                return
    # return

    for x in range(280, 340):
        for y in range(360, 380):
            if data[x, y] > 100:
                hit("down")
                return
    return

if __name__ =='__main__':
    print("Dino Automation Start's in Next 3 Sec")
    time.sleep(2)
    while True:
        img = ImageGrab.grab().convert('L')
        data = img.load()
        jump()
        # for x in range(340, 360):
        #     for y in range(413, 490):
        #         data[x, y] = 255
        # for x in range(280, 340):
        #     for y in range(360, 380):
        #         data[x, y] = 255
        # img.show()
        # break