#!/usr/bin/env python

import rospy
from std_msgs.msg import Bool

class LedDemo(object):
  def __init__(self):
    rospy.init_node('led_demo')

    self.pub_red = rospy.Publisher('/led/red',   Bool, queue_size=1)
    self.pub_grn = rospy.Publisher('/led/green', Bool, queue_size=1)
    self.pub_blu = rospy.Publisher('/led/blue',  Bool, queue_size=1)

    rospy.Subscriber("/button", Bool, self.button_callback)

    self.rgb = 0

    rospy.loginfo(rospy.get_caller_id() + ": XPCC Rosserial Led Demo: Press the button to cycle red, green and blue LED.")

  def button_callback(self, data):
    rospy.loginfo(rospy.get_caller_id() + ": Button %s" % data.data)
    if data.data == True:
      self.rgb = self.rgb + 1
      if self.rgb == 3:
        self.rgb = 0
      rospy.loginfo(rospy.get_caller_id() + ": Setting %s" % ("red" if self.rgb == 0 else ("green" if self.rgb == 1 else "blue")))

    self.pub_red.publish(self.rgb == 0)
    self.pub_grn.publish(self.rgb == 1)
    self.pub_blu.publish(self.rgb == 2)

  def run(self):
    rospy.spin()

if __name__ == '__main__':
  led_demo = LedDemo()
  led_demo.run()
