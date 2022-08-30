from imageai.Detection import ObjectDetection
import os
# je n'arrive pas à installer imageai

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath(os.path.join(
    execution_path, "resent50_coco_best_v2.1.0.h5"))
detector.loadModel()

detections = detector.detectOjectsFromImage(
    input_image=os.path.join(execution_path, "image.jpg"),
    output_image_path=os.path.join(execution_path, "imagenew.jpg")
)

for eachObject in detection:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
