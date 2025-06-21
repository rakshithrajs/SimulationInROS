import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

PACKAGE_NAME = "view_bot"
PACKAGE_DIR = get_package_share_directory(PACKAGE_NAME)
URDF_FILE = os.path.join(PACKAGE_DIR, "urdf", "sample.urdf")


def generate_launch_description():

    # Start Gazebo
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("gazebo_ros"), "launch", "gazebo.launch.py"
            )
        ),
    )

    # Spawn Robot in Gazebo
    spawn_entity = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity",
            "chota_bot",
            "-file",
            URDF_FILE,
            "-x",
            "0",
            "-y",
            "0",
            "-z",
            "1.0",
        ],
        output="screen",
    )

    robot_state_publisher = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": open(URDF_FILE).read()}],
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher", executable="joint_state_publisher"
    )

    return LaunchDescription(
        [gazebo, spawn_entity, robot_state_publisher, joint_state_publisher_node]
    )
