import pyautogui
import cv2
import numpy as np
import time
import pyscreenshot
import webbrowser as w

CACTUS_OUTER = range(800, 800)
CACTUS_INNER = range(300, 300)

BIRD_OUTER = range(800, 760)
BIRD_INNER = range(250, 0)

pyautogui.PAUSE = 0.50
pyautogui.FAILSAFE = True


def perform_action(data):

    # Identify a point in front of the dino and verify the
    # the pixel colour.

    # For Cactus
    for i in range(890, 840, -1):
        for j in range(370, 330, -1):
            if data[i, j][0] != 247:
                print(i, " ", j, " : ", data[i, j][0])
                pyautogui.press("up")
                return

    # ToDo: For Bird
    # The pixel range has to be extended for identifying Bird obstacles
    return


def screen_grab(i):
    image = pyscreenshot.grab()
    # image = cv2.cvtColor(np.array(image),
    #                      cv2.COLOR_RGB2BGR)
    # cv2.imwrite("images/image{}.png".format(str(i)), image)
    #
    # image = Image.open("images/image{}.png".format(str(i)))
    image = image.convert('RGB')
    data = image.load()

    perform_action(data)


def start_game():
    i = 0
    w.open("https://chromedino.com/")
    time.sleep(5)
    pyautogui.press("up")
    while True:
        screen_grab(i)
        i = i+1


start_game()
