cmake_minimum_required(VERSION 3.8)
project(my_robot_description)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# If you have URDF/Xacro or other dependencies, include them here:
# find_package(urdf REQUIRED)

# Install launch and URDF files
install(
  DIRECTORY launch urdf
  DESTINATION share/${PROJECT_NAME}
)

# Install Python node(s)
install(PROGRAMS
  fuzzy_logic/fuzzy_controller_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# Optional: Lint and test support
if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_cpplint_FOUND TRUE)
  set(ament_cmake_copyright_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

