import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarProcessor(Node):
    def __init__(self):
        super().__init__('lidar_processor')

        # Subscribe to LiDAR scan topic
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',               # Adjust if your LiDAR publishes elsewhere
            self.lidar_callback,
            10                     # Queue size (suitable for real-time)
        )

        # Initialize distance metrics
        self.closest_distance = None
        self.front_distance = None

    def lidar_callback(self, msg):
        # Filter out invalid readings (too close or too far)
        valid = [r for r in msg.ranges if 0.05 < r < 30.0]
        if not valid:
            return

        self.closest_distance = min(valid)                     # Closest obstacle
        self.front_distance = msg.ranges[len(msg.ranges)//2]  # Directly ahead

        # Optional: log distances for debugging
        self.get_logger().info(f'Closest: {self.closest_distance:.2f} m | Front: {self.front_distance:.2f} m')

    def get_distances(self):
        # Used by fuzzy logic system
        return {
            'closest': self.closest_distance,
            'front': self.front_distance
        }
