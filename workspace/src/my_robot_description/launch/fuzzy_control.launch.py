from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Barometer Node
        Node(
            package='my_robot_description',
            executable='barometer_node',
            name='barometer',
            output='screen'
        ),

        # IMU Node
        Node(
            package='my_robot_description',
            executable='imu_node',
            name='imu',
            output='screen'
        ),

        # LiDAR Node
        Node(
            package='my_robot_description',
            executable='lidar_node',
            name='lidar',
            output='screen'
        ),

        # Fuzzy Logic Controller
        Node(
            package='my_robot_description',
            executable='fuzzy_controller_node',
            name='fuzzy_controller',
            output='screen',
            parameters=[{'altitude_threshold': 5.0}]
        )
    ])
