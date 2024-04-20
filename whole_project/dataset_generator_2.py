# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:08:17 2024

@author: 1mich
"""

import numpy as np
import matplotlib.pyplot as plt

def Trans_matrix(DH_par, row):
    alfa = DH_par[row][0]
    a = DH_par[row][1]
    d = DH_par[row][2]
    theta = DH_par[row][3]
    T =np.array([[np.cos(theta),                     -1 * np.sin(theta),                   0,                                      a],
                 [np.sin(theta) * np.cos(alfa),      np.cos(theta) * np.cos(alfa) ,        -1*np.sin(alfa),      -1*np.sin(alfa) * d],
                 [np.sin(theta) * np.sin(alfa),      np.cos(theta) * np.sin(alfa),         np.cos(alfa),            np.cos(alfa) * d],
                 [0,                                 0,                                    0,                                      1]])
    return T

def matrix_mul_more(lista, frame_num):
    temp = lista[0]
    T = lista[0]
    for i in range(frame_num - 1):
        T = np.matmul(temp, lista[i+1])
        temp = T
    return T 



#defining constanst
L1 = 4.
L2 = 5.
L3 = 5.

Frame_num = 4

#DH paramiters for this robotic arm
#ta werja ma podane initial theta, robię nowa gdzie nie ma tej potrzeby
"""
DH_p_basic = np.array([
    [0, np.pi/2, 0, 0],
    [0, 0, L2, L3],
    [L1, 0, 0, 0],
    [np.deg2rad(thet1), np.deg2rad(thet2), np.deg2rad(thet3), 0]
])
"""
DH_p_basic = np.array([
    [0, np.pi/2, 0, 0],
    [0, 0, L2, L3],
    [L1, 0, 0, 0],
    [0, 0, 0, 0]
])
DH_p = np.transpose(DH_p_basic)

theta_deg_input = [30,60,120]

def calculate_forward_kin(theta_deg):
    T_rel_0 = []
    Ta = []
    #udpdate DH_paramiters by the new angles
    DH_p[:, 3] = np.deg2rad([theta_deg[0], theta_deg[1], theta_deg[2], 0])#zmiana wartosci 3 kolumny nowymi
    for  i in range(Frame_num):
        Ta.append(Trans_matrix(DH_p, i))
    Ta = [Trans_matrix(DH_p, i) for i in range(Frame_num)]
    for i in range(Frame_num):
        T_rel_0.append(matrix_mul_more(Ta, i+1))
    last_matrix = T_rel_0[-1]
    vector_xyz = last_matrix[:3, -1]
    return vector_xyz

new_XYZ = calculate_forward_kin(theta_deg_input)

print(new_XYZ)

import numpy as np

min_angle = 0
max_angle = 180
step = 1 # Przykładowa wartość kroku zmiennoprzecinkowego

# Generowanie wszystkich kombinacji kątów theta w podanym zakresie i kroku
theta1_values, theta2_values, theta3_values = np.meshgrid(np.arange(min_angle, max_angle, step),
                                                           np.arange(min_angle, max_angle, step),
                                                           np.arange(min_angle, max_angle, step),
                                                           indexing='ij')

# Łączenie wszystkich kombinacji kątów w jedną tablicę
theta_values = np.column_stack((theta1_values.ravel(), theta2_values.ravel(), theta3_values.ravel()))

# Generowanie danych XYZ dla każdej kombinacji kątów theta
data_list = []
for theta_input in theta_values:
    output_xyz = calculate_forward_kin(theta_input)  # Tu należy zdefiniować funkcję calculate_forward_kin
    data_list.append(np.concatenate((theta_input, output_xyz), axis=0))

# Konwertowanie listy danych na tablicę NumPy
collected_data = np.array(data_list)

# Wyświetlanie danych
#for i, row in enumerate(collected_data):
    #theta1, theta2, theta3, x, y, z = row
    #print(f"Entry {i+1}:")
    #print(f"Theta: ({theta1}, {theta2}, {theta3})")
    #print(f"Output XYZ: ({x}, {y}, {z})")
    #print()


import pandas as pd

df = pd.DataFrame(collected_data, columns=['Theta1', 'Theta2', 'Theta3', 'X', 'Y', 'Z'])


df.to_csv('collected_data_180_step_1.csv', index=False)