import rclpy
from rclpy.executors import MultiThreadedExecutor

# Import the decision engine node
from .decision_engine import FuzzyDecisionEngine

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS 2 communication

    # Create the core fuzzy logic decision engine node
    decision_node = FuzzyDecisionEngine()

    # Use multi-threading to allow sensor callbacks in parallel
    executor = MultiThreadedExecutor()
    executor.add_node(decision_node)

    try:
        executor.spin()  # Spin until shutdown signal or exception
    except KeyboardInterrupt:
        pass
    finally:
        decision_node.destroy_node()
        rclpy.shutdown()
