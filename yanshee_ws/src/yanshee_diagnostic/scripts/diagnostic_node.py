#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import JointState, Imu, Image

class YansheeDiagnostic:
    def __init__(self):
        rospy.init_node('yanshee_diagnostic')
        rospy.Subscriber("/yanshee/joint_states", JointState, self.joint_cb)
        rospy.Subscriber("/yanshee/imu/data", Imu, self.imu_cb)
        rospy.Subscriber("/yanshee/camera/image_raw", Image, self.camera_cb)
        self.status = {"joint": False, "imu": False, "camera": False}

    def joint_cb(self, msg):
        self.status["joint"] = True

    def imu_cb(self, msg):
        self.status["imu"] = True

    def camera_cb(self, msg):
        self.status["camera"] = True

    def run(self):
        rate = rospy.Rate(0.5)
        while not rospy.is_shutdown():
            rospy.loginfo(f"Diagnostic status: {self.status}")
            rate.sleep()

if __name__ == "__main__":
    diag = YansheeDiagnostic()
    diag.run()
