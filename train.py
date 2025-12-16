from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(data='data/dataset/data.yaml', epochs=50, imgsz=640, device='cpu', project='models', name='GD')
print("finished training")
print("Best model is saved at" + results.save_dir + "/weights/best.pt")