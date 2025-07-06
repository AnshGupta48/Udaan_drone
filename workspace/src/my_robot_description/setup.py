from setuptools import setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, package_name + '.fuzzy_logic'],
    data_files=[
        # Required for ROS 2 to recognize the package
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),

        # Install the package.xml
        ('share/' + package_name, ['package.xml']),

        # Install all launch files
        ('share/' + package_name + '/launch', [
            'launch/fuzzy_control.launch.py',
            'launch/spawn_drone_gazebo.launch.py',
            'launch/view_drone.launch.py',
            'launch/bridge_barometer.launch.py'
        ]),

        # Install config files
        ('share/' + package_name + '/config', [
            'config/fuzzy_controller.yaml',
            'config/gz_bridge.yaml'
        ])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Yesha',
    maintainer_email='pabariyesha@gmail.com',
    description='Multilayered fuzzy logic drone controller',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fuzzy_controller_node = my_robot_description.fuzzy_logic.fuzzy_controller_node:main',
            'barometer_node = my_robot_description.fuzzy_logic.barometer_module:main',
            'imu_node = my_robot_description.fuzzy_logic.imu_module:main',
            'lidar_node = my_robot_description.fuzzy_logic.lidar_node:main',
        ],
    },
)
