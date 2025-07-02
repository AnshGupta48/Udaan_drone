import rclpy
from rclpy.node import Node

# Import modular sensor processors
from .lidar_module import LidarProcessor
from .imu_module import ImuProcessor
from .barometer_module import BarometerProcessor

class FuzzyDecisionEngine(Node):
    def __init__(self):
        super().__init__('fuzzy_decision_engine')

        # Initialize sensor modules
        self.lidar = LidarProcessor()
        self.imu = ImuProcessor()
        self.barometer = BarometerProcessor()

        # Evaluate fuzzy logic every 0.5 seconds
        self.create_timer(0.5, self.evaluate)

    def evaluate(self):
        # Get latest sensor readings
        lidar_data = self.lidar.get_distances()
        imu_data = self.imu.get_imu_data()
        altitude = self.barometer.get_altitude()

        # Validate availability of sensor input
        if (
            lidar_data is None or lidar_data['front'] is None or
            imu_data is None or imu_data['angular_vel'] is None or
            altitude is None
        ):
            self.get_logger().info('Waiting for valid sensor data...')
            return

        # Extract relevant sensor values
        front = lidar_data['front']
        roll = imu_data['angular_vel']['x']  # Adjust if needed
        alt = altitude

        # Apply simple fuzzy decision rules
        if front < 1.0:
            decision = "Obstacle ahead → Turn or ascend"
        elif alt < 0.5:
            decision = "Too low → Ascend"
        elif abs(roll) > 0.3:
            decision = "Too tilted → Stabilize"
        else:
            decision = "Path clear → Move forward"

        self.get_logger().info(f'Decision: {decision}')
