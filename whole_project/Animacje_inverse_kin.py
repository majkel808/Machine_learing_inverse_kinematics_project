# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:45:48 2024

@author: 1mich
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def Trans_matrix(DH_par, row):
    alfa = DH_par[row][0]
    a = DH_par[row][1]
    d = DH_par[row][2]
    theta = DH_par[row][3]
    T = np.array([[np.cos(theta), -1 * np.sin(theta), 0, a],
                  [np.sin(theta) * np.cos(alfa), np.cos(theta) * np.cos(alfa), -1 * np.sin(alfa),
                   -1 * np.sin(alfa) * d],
                  [np.sin(theta) * np.sin(alfa), np.cos(theta) * np.sin(alfa), np.cos(alfa), np.cos(alfa) * d],
                  [0, 0, 0, 1]])
    return T

def matrix_mul_more(lista, frame_num):
    temp = lista[0]
    T = lista[0]
    for i in range(frame_num - 1):
        T = np.matmul(temp, lista[i + 1])
        temp = T
    return T

def extract_me_some_vector(T):
    V = []
    for i in range(3):
        V.append(T[i][3])
    return V

def give_me_some_vector(v_start, v_end, color_g, arrow_length_ratio_g):
    ax.quiver(v_start[0], v_start[1], v_start[2], v_end[0], v_end[1], v_end[2], color=color_g,
               arrow_length_ratio=arrow_length_ratio_g)

def subtract_me_some_vector(T, frame0, frame_number):
    V_rel = []
    V_rel.append(T[0])
    for i in range(frame_number - 1):
        V_rel.append(np.subtract(T[i + 1], T[i]))
    return V_rel

# Constants and initial values for the forward kinematics
L1 = 4
L2 = 5
L3 = 5
Frame_num = 4
figure_X_lim = 10
figure_Y_lim = 10
figure_Z_lim = 15

thet1 = 45
thet2 = 16.31
thet3 = 96.82

# DH parameters
DH_p_basic = np.array([
    [0, np.pi / 2, 0, 0],
    [0, 0, L2, L3],
    [L1, 0, 0, 0],
    [np.deg2rad(thet1), np.deg2rad(thet2), np.deg2rad(thet3), 0]
])
DH_p = np.transpose(DH_p_basic)

fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")

# Function to update the forward kinematics based on theta values
def update_forward_kinematics(theta1, theta2, theta3):
    frame_0 = [0, 0, 0]
    DH_p[:, 3] = np.deg2rad([theta1, theta2, theta3, 0])
    Ta = [Trans_matrix(DH_p, i) for i in range(Frame_num)]
    T_rel_0 = [matrix_mul_more(Ta, i + 1) for i in range(Frame_num)]
    vector_T_rel = [extract_me_some_vector(T) for T in T_rel_0]
    V_link = subtract_me_some_vector(vector_T_rel, frame_0, Frame_num)

    ax.clear()
    give_me_some_vector(frame_0, V_link[0], 'red', 0.1)
    give_me_some_vector(vector_T_rel[0], V_link[1], 'blue', 0.1)
    give_me_some_vector(vector_T_rel[1], V_link[2], 'red', 0.1)
    give_me_some_vector(vector_T_rel[2], V_link[3], 'blue', 0.1)
    ax.set_xlim([-1 * figure_X_lim, figure_X_lim])
    ax.set_ylim([-1 * figure_Y_lim, figure_Y_lim])
    ax.set_zlim([0, figure_Z_lim])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.draw()

# Input for range of theta values

#defying fuctiong for creating a posint on the trajectory


#starting position 
statring_point = np.array([7.0197861, 3.27338002, 9.94331352])
end_point =np.array( [7.0197861, 3.27338002, 5.94331352])
step = .5

import pandas as pd
import numpy as np
'''
def load_data_from_csv(file_path):
    # Wczytanie danych z pliku CSV do obiektu DataFrame
    df = pd.read_csv(file_path)
    
    # Konwersja danych do tablicy numpy
    data_array = df.to_numpy()
    
    # Długość kolumny (ilość wierszy)
    num_rows = len(df)
    
    return data_array, num_rows

theta_input, frames = load_data_from_csv("predicted_thetas_2.csv")


# Animation function
def animate(i):
    update_forward_kinematics(theta_input[0][i], theta_input[1][i],theta_input[2][i])
    print(theta_input[0][i])
# Number of frames


# Create animation
ani = FuncAnimation(fig, animate, frames=frames, interval=500)
plt.show()
'''

def load_data_from_csv(file_path):
    # Wczytanie danych z pliku CSV do obiektu DataFrame
    df = pd.read_csv(file_path)
    
    # Konwersja danych do tablicy numpy
    data_array = df.to_numpy()
    
    # Długość kolumny (ilość wierszy)
    num_rows = len(df)
    
    return data_array, num_rows

# Definicja funkcji animate z argumentami theta_input
def animate(i, theta_input):
    update_forward_kinematics(theta_input[i][0], theta_input[i][1], theta_input[i][2])

# Wczytanie danych z pliku CSV
theta_input, frames = load_data_from_csv("predicted_thetas_PC_many_points.csv")

# Tworzenie figury i osi 3D
fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(111, projection="3d")

# Reszta kodu (definicje funkcji, parametry, itp.)...

# Tworzenie animacji
ani = FuncAnimation(fig, animate, frames=frames, fargs=(theta_input,), interval=1)
plt.show()