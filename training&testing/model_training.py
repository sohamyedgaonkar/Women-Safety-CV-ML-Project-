from ultralytics import YOLO

# Load a model
model = YOLO(r"""runs/detect/train12/weights/best.pt""")  # build a new model from scratch
results = model.train(data=r"""c:\Users\DELL\Desktop\human\yolo\OIDv4_ToolKit\OID\yolo_model.yaml""", epochs=50,multi_scale =True)
