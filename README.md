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
- [Usage](#usage)
- [Contributors](#contributors)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)
- 
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
Discuss the results obtained from the project, including the performance of the inverse kinematics model and any insights gained.

## Future Work
Outline potential future enhancements or additions to the project.

## Usage
Provide instructions on how to use the project, including installation steps and examples.

## Contributors
List the contributors to the project, including their roles and contributions.

## License
Specify the license under which the project is released.

## Acknowledgements
Acknowledge any individuals, organizations, or resources that contributed to the project.

## Contact
Provide contact information for users to reach out for questions or feedback.
