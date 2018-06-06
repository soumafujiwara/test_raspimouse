#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist

class JoyTwist(object):
	def __init__(self):
		self._joy_sub = rospy.Subscriber('joy',Joy,self.joy_callback,queue_size=1)
		self._twist_pub = rospy.Publisher('cml_vel',Twist,queue_size=1)
		#self._twist_pub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel',Twist,queue_size=1)

	def joy_callback(self,joy_msg):
		if joy_msg.buttons[0] == 1:

			twist = Twist()
			twist.linear.x = joy_msg.axes[0] * 5
			twist.linear.x = joy_msg.axes[1] * 5
			twist.linear.x = joy_msg.axes[2] * 5
			twist.linear.x = joy_msg.axes[3] * 5
			twist.angular.z = joy_msg.buttons[0] * 10
			twist.angular.z = joy_msg.buttons[1] * 10
			self._twist_pub.publish(twist)
			print 'input'



if __name__ == '__main__':
	rospy.init_node('joy_twist')
	joy_twist = JoyTwist()

	#sub = rospy.Publisher('/raspimouse_on_gazebo/diff_drive_controller/cmd_vel', Twist, queue_size=1)

	rospy.spin()
