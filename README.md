# MACHINE LEARNING INVERSE KINEMATICS PROJECT

## Overview
The project is written in Python and aims to determine the motion of a 3R robot using a neural network model. Inverse kinematics were developed through linear regression based on the TensorFlow library. The remaining scripts were used to develop forward kinematics and robot motion trajectories.

## Table of Contents
- [Detiled description](#Detiled-description)
- [Project Structure](#project-structure)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Implementation Details](#implementation-details)
- [Results](#results)
- [Future Work](#future-work)

  
## Detiled description
The aim of the project was to gain a better understanding of the principles of describing robot kinematics and their mathematical representation, enabling the determination of the end effector position of the robot arm and subsequently its inverse kinematics.

The stages of the project were:

- Development of the forward kinematics model for the 3R robotic arm.
- Creation of an application allowing for the control of the robot arm's position using sliders.
- Script creation to generate datasets for machine learning purposes.
- Implementation of a linear regression neural network model.
- Writing a script to generate trajectories for the XYZ position of the end effector and feeding them into the model.
- Utilizing predicted angular positions of the robotic joints to animate the robot's movement.
- 
## Project Structure
Under the directory named "whole_project," you will find all the necessary files to execute the linear regression model, as well as all the scripts required to animate the movement of the robot.

In the remaining folders, files are grouped for easy organization.

## Features
- Ready-to-use linear regression model for the 3R robot
- Animation script
- Script for testing forward kinematics using sliders

### Script for testing forward kinematics using sliders

<img src="https://github.com/majkel808/Machine_learing_inverse_kinematics_project/assets/163661382/195115ed-6ff4-4937-9419-265c6bbca88a" alt="git_1" width="400"/>

<img src="https://github.com/majkel808/Machine_learing_inverse_kinematics_project/assets/163661382/9254ef45-a381-4582-918f-5fc57fa88a0e" alt="git_2" width="400"/>


## Technologies Used
The entire project is written in Python, utilizing, among others:

- NumPy
- Matplotlib
- Pandas
- Scikit-learn
- TensorFlow

  
## Implementation Details
A script was used to generate the dataset, ensuring a large number of points in space with known angles and XYZ positions. This allowed the neural network model to predict the angular positions of the robot's joints in order to achieve the desired XYZ coordinates. TensorFlow library was employed for this purpose. The model requires further optimization and development.

## Results
The model's learning outcomes were evaluated based on two parameters: the loss function value (LOSS), expected to decrease, and the root mean square error (RMSE) for the model. Both metrics are illustrated below.

<img src="https://github.com/majkel808/Machine_learing_inverse_kinematics_project/assets/163661382/27698bb4-1457-4754-8b28-e89c6e2724b5" alt="git_1" width="400"><br/>

<img src="https://github.com/majkel808/Machine_learing_inverse_kinematics_project/assets/163661382/d1f7aedd-df32-4bbf-ad67-26f06c358195" alt="git_2" width="400"/>

You can watch the animated movement of the robot, with joint angles predicted by the neural network model on YouTube:
[![Click to watch](https://img.youtube.com/vi/qxhOquYd-xE/maxresdefault.jpg)](https://youtu.be/qxhOquYd-xE)

## Future Work
The plan includes the development of a new dataset to optimize the model learning algorithm. Next, existing scripts should be merged into one large project that allows for real-time trajectory determination and robot position generation based on obtained predictions. Finally, functionality should be expanded to include additional degrees of freedom up to 6DOF.



