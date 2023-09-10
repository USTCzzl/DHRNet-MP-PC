# DHRNet + MP-PC

This repository contains the implementation of the MP-PC system and experimental code 

```
## Setup

**Hardware:**

This code is designed around a Franka Emika Panda robot using an Intel Realsense D435 camera mounted on the wrist.  A 3D-printalbe camera mount is available in the `cad` folder. DYMO M10 scales are used to detect grasp success (*Optional*.  See the scales_interface directry for more information).

**The following external packages are required to run everything completely:**
* [ROS Kinetic](http://wiki.ros.org/kinetic/Installation)
* [Franka ROS 0.5.0](https://github.com/frankaemika/franka_ros/tree/0.5.0)
* [Realsense ROS](https://github.com/IntelRealSense/realsense-ros#installation-instructions)

**Installation:**
'''bash
mkdir -p catkin_ws/src
cd catkin_ws/src
git clone https://github.com/USTCzzl/DHRNet-MP-PC/tree/master
git clone -b checkout 0.5.0 https://github.com/frankaemika/franka_ros.git
git clone https://github.com/IntelRealSense/realsense-ros#installation-instructions
cd ..
rosdep install --from-paths src --ignore-src --rosdistro=<your_rosdistro> -y
catkin_make
'''

**Local python requirements can be installed by:**

```bash
pip install -r requirements.txt
```


## Running

To run grasping experiments:

```bash
# Start the robot and required extras.
roslaunch mvp_grasping robot_bringup.launch

# Start the camera, depth conversion and static transform
roslaunch mvp_grasping wrist_realsense.launch


# Start the Multi-View Picking backend
roslaunch mvp_grasping grasp_entropy_service.launch
 
## Execute Grasping Experiment

# For Multi-View Picking
rosrun mvp_grasping panda_mvp_grasp.py



```
