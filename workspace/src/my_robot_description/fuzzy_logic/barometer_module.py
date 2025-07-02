import rclpy
from rclpy.node import Node
from gazebo_msgs.msg import Altimeter  # May require custom plugin import

class BarometerProcessor(Node):
    def __init__(self):
        super().__init__('barometer_processor')

        # Subscribe to the altimeter's output
        self.subscription = self.create_subscription(
            Altimeter,
            '/barometer/data',  
            self.barometer_callback,
            10
        )

        self.altitude = None  # Stores latest altitude reading

    def barometer_callback(self, msg):
        self.altitude = msg.altitude
        self.get_logger().info(f'Altitude: {self.altitude:.2f} m')

    def get_altitude(self):
        # Provides the latest altitude to the fuzzy logic controller
        return self.altitude
