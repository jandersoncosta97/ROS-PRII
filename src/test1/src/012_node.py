1 #! /usr/bin/ python3
2
3 import rospy
4 from sensor_msgs . msg import LaserScan
5
6 class mySub () :
7
8 def __init__ ( self ) :
9 self . sub = rospy . Subscriber (’/ scan_raw ’, LaserScan ,
self . callback , queue_size =1)
10
11 # Definition of the function called by the subscriber
12 def callback ( self , msg ) :
13 # self . counterValue = msg. data
14 print ( msg . ranges )
Robot Operating System 83 / 144

1 # Main program
2 if __name__ == ’__main__ ’:
3 # Define the node
4 rospy . init_node (’ TIAGo_laser_node ’)
5 # Creaete an object of class mySub and run the init
function
6 subObj = mySub ()
7 # While ROS is running
8 rospy . spin ()
