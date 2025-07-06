from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    config_path = os.path.join(
        os.getenv('HOME'),
        'Udaan_drone/Udaan_drone/src/my_robot_description/config/gz_bridge.yaml'
    )

    return LaunchDescription([
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='barometer_bridge',
            output='screen',
            arguments=['--config', config_path]
        )
    ])
