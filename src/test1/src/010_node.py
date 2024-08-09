#!/usr/bin/python3

import rospy
from nav_msgs.msg import Odometry

# Definition of the class
class mySub:
    def __init__(self):
        # Define the subscriber
        self.sub = rospy.Subscriber('/mobile_base_controller/odom', Odometry, self.callback, queue_size=1)

    # Definition of the function called by the subscriber
    def callback(self, msg):
        # self.counterValue = msg.data
        print(msg.pose)

# Main program
if __name__ == '__main__':
    # Define the node
    rospy.init_node('TIAGo_odometry_node')
    # Create an object of class mySub and run the init function
    subObj = mySub()
    # While ROS is running
    rospy.spin()
