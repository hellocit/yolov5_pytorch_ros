#!/usr/bin/env python3
import rospy
from std_srvs.srv import SetBool
from yolov5_pytorch_ros.msg import BoundingBoxes, BoundingBox

filter_flag = True

def handle_detect_box(req):
    if req.data:
        # Do something when the service is called with True
        rospy.loginfo("Detect box service called with True")
        filter_flag = True
    else:
        # Do something when the service is called with False
        rospy.loginfo("Detect box service called with False")
        filter_flag = False
    return True, ""

def boundingBoxesCallback(data):
    rospy.Publisher('/filtered_detected_objects_in_image', BoundingBoxes, queue_size=1)

def detect_box_server():
    rospy.init_node('detect_box_server')
    s = rospy.Service('detect_box', SetBool, handle_detect_box)
    if filter_flag:
        rospy.Subscriber('/detections_image_topic', BoundingBoxes, boundingBoxesCallback)
    rospy.loginfo("Detect box service ready")
    rospy.spin()

if __name__ == "__main__":
    detect_box_server()