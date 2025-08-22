import cv2
from ultralytics import YOLO

# Load YOLOv8n model
modelv8n = YOLO("yolov8n.pt")

# List of image paths
image_files = [f"images/Screenshots/Screenshot ({i}).png" for i in range(1, 6)]
results = modelv8n(image_files)

# Process results and draw green rectangles only for cars
for idx, result in enumerate(results):
    img = cv2.imread(image_files[idx])  # Load original image
    for box in result.boxes:
        cls_id = int(box.cls[0])  # Get class ID
        if cls_id == 2:  # Class ID for 'car' in COCO
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # Get box coordinates
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)  # Green rectangle
    # cv2.imshow(f"Detected Cars {idx}", img)
    cv2.imwrite(f"outputs/hw2_ait_gate_{idx}.jpg", img)
    # cv2.waitKey(0)

cv2.destroyAllWindows()

