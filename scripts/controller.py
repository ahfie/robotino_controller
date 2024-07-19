#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

def odometry_callback(data):
    """
    Callback function to process odometry data.
    """
    roll, pitch, yaw = euler_from_quaternion((data.pose.pose.orientation.x, data.pose.pose.orientation.y, data.pose.pose.orientation.z, data.pose.pose.orientation.w))
    rospy.loginfo("Received Odometry data:")
    rospy.loginfo("Position: x=%f, y=%f, z=%f", data.pose.pose.position.x, data.pose.pose.position.y, data.pose.pose.position.z)
    rospy.loginfo("Orientation: roll=%f, pitch=%f, yaw=%f", roll, pitch, yaw)
    rospy.loginfo("Linear Velocity: x=%f, y=%f, z=%f", data.twist.twist.linear.x, data.twist.twist.linear.y, data.twist.twist.linear.z)
    rospy.loginfo("Angular Velocity: x=%f, y=%f, z=%f", data.twist.twist.angular.x, data.twist.twist.angular.y, data.twist.twist.angular.z)
    
    pos_x = data.pose.pose.position.x
    pos_y = data.pose.pose.position.y

def listener():
    """
    Initializes the node and subscribes to the Odometry topic.
    """
    rospy.init_node('odometry_listener', anonymous=True)
    rospy.Subscriber('odom', Odometry, odometry_callback)  # Adjust topic name if necessary
    rospy.spin()

if __name__ == '__main__':
    listener()