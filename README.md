# DHRNet + MP-PC

This repository contains the implementation of the MP-PC system and experimental code 


### Setup

**Hardware:**

This code is designed around a Franka Emika Panda robot using an Intel Realsense D435 camera mounted on the wrist.  A 3D-printalbe camera mount is available in the `cad` folder. DYMO M10 scales are used to detect grasp success (*Optional*.  See the scales_interface directry for more information).

**The following external packages are required to run everything completely:**
* [ROS Kinetic](http://wiki.ros.org/kinetic/Installation)
* [Franka ROS 0.5.0](https://github.com/frankaemika/franka_ros/tree/0.5.0)
* [Realsense ROS](https://github.com/IntelRealSense/realsense-ros#installation-instructions)


Due to the conflict between Nvidia graphics cards and the Ubuntu realtime kernel, it is recommended to install the project on two computers, computer I (Ubuntu realtime kernel) only needs to install the package, and the following is the installation method for computer II (NVIDIA graphics card)

### Installation(Computer I):

```bash

# Preparing the ROS workspace
mkdir -p catkin_ws/src
cd catkin_ws/src

# Pay attention to the version when downloading
git clone https://github.com/USTCzzl/DHRNet-MP-PC/tree/master
git clone  https://github.com/frankaemika/franka_ros.git
cd ..

# Automatically installing dependencies
rosdep install --from-paths src --ignore-src --rosdistro=<your_rosdistro> -y

# Compiling, X depend on your machine
catkin_make (catkin build ) -j X
```


### Installation(Computer II):

```bash

# Preparing the ROS workspace
mkdir -p catkin_ws/src
cd catkin_ws/src

# Pay attention to the version when downloading
git clone https://github.com/USTCzzl/DHRNet-MP-PC/tree/master
git clone  https://github.com/frankaemika/franka_ros.git
git clone https://github.com/IntelRealSense/realsense-ros#installation-instructions
cd ..

# Automatically installing dependencies
rosdep install --from-paths src --ignore-src --rosdistro=<your_rosdistro> -y

# Compiling, X depend on your machine
catkin_make (catkin build ) -j X
```
Installation [tutorial](https://blog.csdn.net/sinat_25068035/article/details/112537399?spm=1001.2014.3001.5501) for librealsense and realsense_ros 
**Local python requirements can be installed by:**

```
pip install -r requirements.txt


## Running

To run grasping experiments:

```bash
# Start the robot and required extras. (Computer I terminal)
roslaunch mvp_grasping robot_bringup.launch

# Start the camera, depth conversion and static transform (Computer II terminal)
roslaunch mvp_grasping wrist_realsense.launch


# Start the MP-PC backend (Computer II terminal)
roslaunch mvp_grasping grasp_entropy_service.launch
 
## Execute Grasping Experiment

# For Multi-View Picking (Computer II terminal)
rosrun mvp_grasping panda_mvp_grasp.py

# For visualization (Computer II terminal)
rviz
```

### Experiment
Our original reason for proposing this work is that current grasping methods cannot effectively cope with thin and stacked objects, and the following is a comparison between our method and other grasping methods for these two tasks:


[![Grasp thin object](https://res.cloudinary.com/marcomontalbano/image/upload/v1694372343/video_to_markdown/images/youtube--cfLAdKWo4u8-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/cfLAdKWo4u8 "Grasp thin object")




[![stacking objects](https://res.cloudinary.com/marcomontalbano/image/upload/v1694372522/video_to_markdown/images/youtube--biuGoTSoupU-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/biuGoTSoupU "stacking objects")




