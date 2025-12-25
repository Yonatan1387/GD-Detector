import mss
import cv2
import numpy
import keyboard
from ultralytics import YOLO

try:
    model = YOLO("models/BestWIthBlocksV2.pt")
except Exception as e:
    print("Error: Could not load model")
    exit()

monitor = {"top": 85, "left": 1020, "width": 850, "height": 490}

JumpDis = 150
BlockJumpDis = 170

print("Starting the bot...")
print("Press q to exit")

cv2.namedWindow("GD-Detector")
cv2.moveWindow("GD-Detector", 100, 85)

with mss.mss() as sct:
    while True:
        img = numpy.array(sct.grab(monitor))
        only_rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = model(only_rgb_img, conf=0.2, verbose=False)

        player_box = None
        closest_object_dis = 100000
        objectType = "none"
        blocks_conf = 0.2
        spike_conf = 0.6
        block_Y_Filter = 200

        if results[0].boxes:
            boxes = results[0].boxes.xyxy.cpu().numpy()
            classes = results[0].boxes.cls.cpu().numpy()
            confs = results[0].boxes.conf.cpu().numpy()

            for box, cls in zip(boxes, classes):
                if model.names[int(cls)] == "player":
                    player_box = box

            if player_box is not None:
                player_box_x_right = player_box[2]
                player_box_y_center = (player_box[1] + player_box[3]) / 2

                for box, cls, conf in zip(boxes, classes, confs):
                    valid = False

                    if model.names[int(cls)] == "spike":
                        if conf > spike_conf and box[3] > player_box[1]:
                            valid = True

                    if model.names[int(cls)] == "block":
                            if conf > blocks_conf and min(abs(player_box_y_center - box[1]),
                                                          abs(player_box_y_center - box[3])) < block_Y_Filter:
                                valid = True

                    if valid:
                        if box[0] > player_box_x_right:
                            dis = box[0] - player_box_x_right
                            if dis < closest_object_dis:
                                closest_object_dis = dis
                                objectType = model.names[int(cls)]

        if closest_object_dis < 100000 and player_box_x_right > 0:
            limit = 0
            if objectType == "spike":
                limit = JumpDis
            elif objectType == "block":
                limit = BlockJumpDis
            if closest_object_dis < limit:
                keyboard.press("space")
                print("jumping")
            else:
                keyboard.release("space")

        frame = results[0].plot()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        cv2.putText(frame, f"dis: {closest_object_dis}", (50, 50),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255, 0), 2)
        cv2.imshow("GD-Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

cv2.destroyAllWindows()
