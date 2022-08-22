from imageai.Detection import ObjectDetection
import os
# je n'arrive pas à installer imageai


execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.srtModelPath(os.path.join(
    execution_path, "resent50_coco_best_v2.1.0.h5"))
detector.loadModel()


for eachObject in detection:
    print(eachObject["name"], " : ", eachObject["percentage_probability"])
