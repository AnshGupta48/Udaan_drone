from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_robot_description',
            executable='fuzzy_controller_node.py',
            name='fuzzy_controller',
            output='screen'
        )
    ])
