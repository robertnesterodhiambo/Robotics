#!/usr/bin/env pyhton3
import rclpy
from rclpy.node import Node


class Mynode(Node):
    
    def __init__(self):
        super().__init__("first_node")
        #self.get_logger().info("hello from ROS2 automatic build")
        self.counter_ = 0
        self.create_timer(1.0,self.timer_callback)
        
    def timer_callback (self):
        self.get_logger().info("ROS " + str(self.counter_))
        self.counter_ +=1       

def main(args = None):
    rclpy.init(args = args) # installing node with ros2 functionalities
    ## node goese in here
    ## we use oop 
    node  = Mynode()
    rclpy.spin(node)
    
    rclpy.shutdown()
if __name__ == '__main__':
    main()