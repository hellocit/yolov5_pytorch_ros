#!/usr/bin/env python3

import rospy
from std_srvs.srv import SetBool

def handle_detect_box(req):
    if req.data:
        # Do something when the service is called with True
        rospy.loginfo("Detect box service called with True")
    else:
        # Do something when the service is called with False
        rospy.loginfo("Detect box service called with False")
    return True, ""

def detect_box_server():
    rospy.init_node('detect_box_server')
    s = rospy.Service('detect_box', SetBool, handle_detect_box)
    rospy.loginfo("Detect box service ready")
    rospy.spin()

if __name__ == "__main__":
    detect_box_server()