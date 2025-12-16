import mss
import cv2
import numpy
import os
import keyboard
import time
from datetime import datetime

path = os.path.join("data", "screenshots")
if not os.path.exists(path):
    os.makedirs(path)

monitor = {"top": 85, "left": 1020, "width": 850, "height": 490}


with mss.mss() as sct:
    while True:
        time.sleep(5)
        img = numpy.array(sct.grab(monitor))
        cv2.imshow("", img)
        if keyboard.is_pressed('p'):
            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            filename = os.path.join(path, "img-" + timestamp + ".jpg")
            cv2.imwrite(filename, img)
            print("Captured: " + filename)
            time.sleep(0.2)
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break

