from ultralytics import YOLO

yolov8 = YOLO('models/yolov8n.pt')
results = yolov8('testimages/leonardo.jpg')
results[0].save('saves/leonardo-inference.jpg')