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

monitor = {"top": 180, "left": 315, "width": 1295, "height": 705}


with mss.mss() as sct:
    while True:
        time.sleep(10)
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

