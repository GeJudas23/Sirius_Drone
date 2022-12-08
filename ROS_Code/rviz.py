import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospy.init_node('computer_vision_sample')
bridge = CvBridge()

def image_callback(data):
    cv_image = bridge.imgmsg_to_cv2(data, 'bgr8')  # OpenCV image
    image_pub.publish(bridge.cv2_to_imgmsg(cv_image, 'bgr8'))

image_sub = rospy.Subscriber('main_camera/image_raw', Image, image_callback)
image_pub = rospy.Publisher('~debug', Image, queue_size=1)
rospy.spin()