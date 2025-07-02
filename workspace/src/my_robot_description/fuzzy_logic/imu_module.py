import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuProcessor(Node):
    def __init__(self):
        super().__init__('imu_processor')

        # Subscribe to IMU sensor topic
        self.subscription = self.create_subscription(
            Imu,
            '/imu/data',          # Topic (adjust if remapped)
            self.imu_callback,
            10
        )

        # Initialize IMU data storage
        self.linear_acc = None    # m/s²
        self.angular_vel = None   # rad/s

    def imu_callback(self, msg):
        # Store linear acceleration
        self.linear_acc = {
            'x': msg.linear_acceleration.x,
            'y': msg.linear_acceleration.y,
            'z': msg.linear_acceleration.z
        }

        # Store angular velocity
        self.angular_vel = {
            'x': msg.angular_velocity.x,
            'y': msg.angular_velocity.y,
            'z': msg.angular_velocity.z
        }

        # Log data for debugging (optional)
        self.get_logger().info(
            f"IMU | Acc: x={self.linear_acc['x']:.2f}, z={self.linear_acc['z']:.2f} | "
            f"Ang Vel: z={self.angular_vel['z']:.2f}"
        )

    def get_imu_data(self):
        # Used by fuzzy logic controller
        return {
            'linear_acc': self.linear_acc,
            'angular_vel': self.angular_vel
        }
