# Simulation in ROS

```bash
Folder structure
└── 📁Session
    └── 📁config
        └── session.rviz -> config file Rvix
    └── 📁images
        └── udacity-av-subsystems.png  
    └── 📁point_clouds -> This folder containes sample pcd files
        └── five_people.pcd
        └── ism_test_cat.pcd
        └── model.pcd
        └── office1.pcd
    └── 📁urdf_ws -> The main URDF workspace, dont forget to build it before running, and source as well
        └── 📁src
            └── 📁view_bot
                └── CMakeLists.txt
                └── 📁launch
                    └── view_gazebo.launch.py
                    └── view.launch.py
                └── package.xml
                └── 📁urdf
                    └── sample.urdf
    └── 📁urdf2_ws -> sample one
        └── 📁src
            └── 📁botbot
                └── CMakeLists.txt
                └── 📁launch
                    └── view.launch.py
                └── package.xml
                └── 📁urdf
                    └── chota.urdf
    └── .gitignore -> a github config file
    └── notes.ipynb -> all the notes of the session are here
    └── pcd.py -> the file that runs the pcd in rviz
    └── slamGUI.py - the file the has the gui run SLAM and NAV2 on turtlebot3
```

Any queries please DM anyone of us. 
Thank you. 
