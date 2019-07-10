import rospy
from std_msgs.msg import String

def publisher():
    pub=rospy.Publisher('/imu', Imu, queue_size=1)
     rospy.init_node('work4', anonymous=True)
    rate=rospy.Rate(200)

