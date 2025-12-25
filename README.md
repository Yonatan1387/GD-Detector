# GD-Detector
GD Detector is a bot for the game Geometry Dash that uses computer vision and artificial intelligence to detect obstacles in real time and make movement decisions in milliseconds.

### Model Performance
The latest model (BestWithBlocksV2.pt) achieves the following accuracy:
* **player** - 91%
* **spikes** - 94%
* **blocks** - 61%

## Project Goal
The goal of this project was to create software capable of playing a game without accessing the game's internal code or memory. Instead, the bot relies entirely on visual data captured from the screen in real time.
## Tools
* **python 3.10** - programming language.
* **YOLOv8** (Ultralytics) - custom trained object detection AI model.
* **OpenCV** - real time image processing.
* **MSS** - fast screen capture library.
* **RoboFlow** - used for data management, and labeling.
* **Google Colab** - used cloud GPUs for fast training.

## How It Works
* **Capture** - the mss library captures a specific area of the screen
* **Processing** - converts the image from BGRA to RGB
* **Detecting** - the YOLO model detects 3 types of objects: player, spike and block
* **Logic** - calculating the distance from the player to the nearest object (a spike or a block), while ignoring objects that are too high or too low.
* **Action** - pressing space using keyboard library if the distance is below the matching jump distance of the nearest obstacle.

 ## Folder Structure
 ```text
data/                        # training data
models/                      # trained models
├── best.pt
├── BestWithBlocks.pt
└── BestWithBlocksV2.pt
screenshots/
├── data/                    # raw images captured for training
└── capture.py               # data collection script
train.py                     # training script
bot.py                       # main bot logic
detect.py                    # detecting objects
requirements.txt
README.md
```
