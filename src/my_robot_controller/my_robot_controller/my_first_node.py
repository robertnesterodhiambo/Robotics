#!/usr/bin/env pyhton3
import rclpy
from rclpy.node import Node


class Mynode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        self.get_logger().info("hello from ROS2")

def main(args = None):
    rclpy.init(args = args) # installing node with ros2 functionalities
    ## node goese in here
    ## we use oop 
    node  = Mynode()
    
    
    rclpy.shutdown()
if __name__ == '__main__':
    main()