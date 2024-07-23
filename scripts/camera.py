#!/usr/bin/env python

import cv2
import argparse
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

cap  = ''
stream_url = "http://131.159.213.47:8080/video"

rospy.init_node('camera_publisher', anonymous=True)
image_pub = rospy.Publisher('camera/image', Image, queue_size=1)  # Adjust topic name if necessary
bridge = CvBridge()

def spin():
    rate = rospy.Rate(15)

    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if not ret:
            rospy.loginfo("Error: Could not read frame")
            break

        try:
            ros_image = bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        except Exception as e:
            rospy.logerr(f"Error converting image: {e}")
            continue

        image_pub.publish(ros_image)
        rate.sleep()
    
    cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Command-line argument parsing to get ip and port of camera streaming.")

    parser.add_argument('--ip', type=str, default="131.159.213.47")
    parser.add_argument('--port', type=str, default="8080")

    args = parser.parse_args()

    # URL of the video stream
    stream_url = 'http://' + args.ip + ':' + args.port + '/video'
    # cap = cv2.VideoCapture(stream_url)
    
    cap = cv2.VideoCapture(0)
    # Check if the stream is opened
    if not cap.isOpened():
        rospy.loginfo("Error: Could not open video stream")
        exit()

    try:
        spin()
    except rospy.ROSInterruptException:
        cap.release()
        rospy.loginfo("error: rospy.ROSInterruptException from camera.py")