
from ultralytics import YOLO

# Load a model
model = YOLO(r"""runs/detect/train13/weights/best.pt""")  # pretrained YOLOv8n model

# Run batched inference on a list of images
results = model([r"""c:\Users\DELL\Desktop\human\train\images\IMG_20240823_143544_jpg.rf.b1cde1d68883460ac4b982a8743d8f6a.jpg""", r"""c:\Users\DELL\Desktop\human\train\images\IMG_20240823_143721_jpg.rf.184efc65aab01ddfa01dfe2f1f66b92e.jpg"""])  # return a list of Results objects

# Process results list
for result in results:
    boxes = result.boxes  # Boxes object for bounding box outputs
    masks = result.masks  # Masks object for segmentation masks outputs
    keypoints = result.keypoints  # Keypoints object for pose outputs
    probs = result.probs  # Probs object for classification outputs
    obb = result.obb  # Oriented boxes object for OBB outputs      
    result.show()  # display to screen
    result.save(filename="result.jpg")  # save to disk
 