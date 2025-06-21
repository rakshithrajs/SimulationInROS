import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Header
import sensor_msgs_py.point_cloud2 as pc2
import numpy as np
import open3d as o3d
import subprocess
import threading


class PointCloudPublisher(Node):
    def __init__(self):
        super().__init__("pointcloud_publisher")
        self.publisher_ = self.create_publisher(PointCloud2, "pointcloud", 10)
        timer_period = 1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.pcd_file = "point_clouds/model.pcd"
        self.cloud = None
        self.load_pcd()

    def load_pcd(self):
        pcd = o3d.io.read_point_cloud(self.pcd_file)
        self.cloud = np.asarray(pcd.points)

    def timer_callback(self):
        self.get_logger().info("Publishing point cloud...")
        if self.cloud is not None:
            # Create header
            header = Header()
            header.stamp = self.get_clock().now().to_msg()
            header.frame_id = "map"
            msg = pc2.create_cloud_xyz32(header, self.cloud.tolist())
            self.publisher_.publish(msg)
            self.get_logger().info("Published point cloud")


def run_rviz():
    # Start RViz in a separate thread'
    print("Starting RViz...")
    subprocess.run(["rviz2"], check=True)


def main(args=None):
    threading.Thread(target=run_rviz).start()
    rclpy.init(args=args)
    pointcloud_publisher = PointCloudPublisher()
    pointcloud_publisher.get_logger().info("PointCloudPublisher node has been started.")
    rclpy.spin(pointcloud_publisher)
    pointcloud_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
