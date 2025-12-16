import mss
import cv2
import numpy
import keyboard
from ultralytics import YOLO

try:
    model = YOLO("models/best.pt")
except Exception as e:
    print("Error: Could not load model")
    exit()

monitor = {"top": 85, "left": 1020, "width": 850, "height": 490}

print("Starting the detector...")
print("Press q to exit")

with mss.mss() as sct:
    while True:
        img = numpy.array(sct.grab(monitor))
        only_rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = model(only_rgb_img, conf=0.3, verbose=False)
        cv2.imshow("GD-Detector", results[0].plot())
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
