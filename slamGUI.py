import subprocess
import tkinter as tk
from tkinter import messagebox

# Function to run terminal commands in a new terminal (Kubuntu/Konsole)
def run_command(command):
    try:
        subprocess.Popen( command, shell=True)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to execute: {command}\nError: {str(e)}")

# GUI setup
root = tk.Tk()
root.title("TurtleBot SLAM Demo")
root.geometry("400x300")

label = tk.Label(root, text="TurtleBot SLAM Launcher", font=("Helvetica", 16))
label.pack(pady=10)

# Buttons to run the commands
btn1 = tk.Button(root, text="1. Launch TurtleBot3 Simulation", command=lambda: run_command("ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py"), width=40)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="2. Nav2", command=lambda: run_command("ros2 launch nav2_bringup navigation_launch.py use_sim_time:=True"), width=40)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="3. SLAM toolbox", command=lambda: run_command("ros2 launch slam_toolbox online_async_launch.py use_sim_time:=True"), width=40)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="4. Launch RViz for Visualization", command=lambda: run_command("ros2 run rviz2 rviz2 -d /opt/ros/humble/share/nav2_bringup/rviz/nav2_default_view.rviz"), width=40)
btn4.pack(pady=5)

# Exit button
exit_btn = tk.Button(root, text="Exit", command=root.destroy, width=40, bg="red", fg="white")
exit_btn.pack(pady=10)

root.mainloop()
