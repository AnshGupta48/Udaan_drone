from setuptools import setup

package_name = 'my_robot_description'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, package_name + '/fuzzy_logic'],
    data_files=[],
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
        ],
    },
)
