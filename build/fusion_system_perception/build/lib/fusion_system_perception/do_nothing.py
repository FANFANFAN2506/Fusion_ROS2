import rclpy

from .perception import Perception


class DoNothingPerception(Perception):
    def __init__(self):
        super().__init__("do_nothing_perception")
        self.get_logger().info('Test perception!')


def main(args=None):
    rclpy.init(args=args)

    percept = DoNothingPerception()

    try:
        rclpy.spin(percept)
    finally:
        # Destroy the node explicitly
        # (optional - otherwise it will be done automatically
        # when the garbage collector destroys the node object)
        percept.destroy_node()
        rclpy.shutdown()
