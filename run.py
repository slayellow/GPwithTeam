from Object_detection_demo import ObjectDetection
from Lane_Detection_V2 import LaneDetection


class Run(object):


    def __init__(self):
        self.lane = LaneDetection()


    def load_path(self):
        while(1):
            object = int(input('Select Image(1) or Video(2) : '))
            if object == 1:
                path = input('Input Image Path+Filename : ')
                return object, path
            elif object == 2:
                path = input('Input Video Path+Filename : ')
                return object, path
            else:
                print('Number Error. Please Retry to select number')


    def run_model(self, object, path):
        output_name = input('Select Output Filename : ')
        object_class = ObjectDetection(path)
        if object == 1:
            object_class.image_detection(self.lane, output_name)
        else:
            object_class.video_detection(self.lane, output_name)