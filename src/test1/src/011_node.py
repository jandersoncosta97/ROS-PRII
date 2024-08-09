#!/usr/bin/python3

import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

class mySub:
    def __init__(self):
        self.sub = rospy.Subscriber('/mobile_base_controller/odom', Odometry, self.callback, queue_size=1)

    def callback(self, msg):
        qtn = msg.pose.pose.orientation
        qtn_list = [qtn.x, qtn.y, qtn.z, qtn.w]
        (roll, pitch, yaw) = euler_from_quaternion(qtn_list)
        print(roll, pitch, yaw)

# Main program
if __name__ == '__main__':
    rospy.init_node('TIAGo_odometry_node')
    subObj = mySub()
    rospy.spin()
