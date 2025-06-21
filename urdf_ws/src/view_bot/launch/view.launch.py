import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

PACKAGE_NAME = "view_bot"
PACKAGE_DIR = get_package_share_directory(PACKAGE_NAME)

URDF_FILE = os.path.join(PACKAGE_DIR, "urdf", "sample.urdf")
RVIZ_CONFIG_FILE = os.path.join(PACKAGE_DIR, "rviz", "my_bot.rviz")


def generate_launch_description():

    # Declare Launch Arguments
    urdf_arg = DeclareLaunchArgument(
        name="robot_description",
        default_value=open(URDF_FILE).read(),
        description="URDF file content",
    )

    jsp_gui_arg = DeclareLaunchArgument(
        name="jsp_gui",
        default_value="true",
        choices=["true", "false"],
        description="Flag to enable joint_state_publisher_gui",
    )

    rviz_config_arg = DeclareLaunchArgument(
        name="rviz_config",
        default_value=RVIZ_CONFIG_FILE,
        description="Absolute path to rviz config file",
    )

    # Nodes
    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        output="screen",
        parameters=[{"robot_description": LaunchConfiguration("robot_description")}],
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher",
        executable="joint_state_publisher",
        condition=UnlessCondition(LaunchConfiguration("jsp_gui")),
    )

    joint_state_publisher_gui_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        condition=IfCondition(LaunchConfiguration("jsp_gui")),
    )

    rviz_node = Node(
        package="rviz2",
        executable="rviz2",
        output="screen",
        # arguments=["-d", LaunchConfiguration("rviz_config")],
    )

    # Launch Description
    return LaunchDescription(
        [
            urdf_arg,
            jsp_gui_arg,
            # rviz_config_arg,
            robot_state_publisher_node,
            joint_state_publisher_node,
            joint_state_publisher_gui_node,
            rviz_node,
        ]
    )
