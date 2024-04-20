# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:37:10 2024

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

#paramtery data collection


min_angle = 0
max_angle = 10 
step = 1  # Przykładowa wartość kroku zmiennoprzecinkowego

def generate_collected_data(min_angle, max_angle, step):
    num_angles = int((max_angle - min_angle) / step)
    data_list = []

    for i, theta1 in enumerate(np.linspace(min_angle, max_angle, num_angles)):
        for j, theta2 in enumerate(np.linspace(min_angle, max_angle, num_angles)):
            for k, theta3 in enumerate(np.linspace(min_angle, max_angle, num_angles)):
                theta_input = [theta1, theta2, theta3]
                output_xyz = calculate_forward_kin(theta_input)  # Tu należy zdefiniować funkcję calculate_forward_kin
                data_list.append(np.concatenate((theta_input, output_xyz), axis=0))

    return np.array(data_list).reshape((num_angles, num_angles, num_angles, 6))

def display_collected_data(collected_data, min_angle, max_angle, step):
    num_angles = collected_data.shape[0]
    for i in range(num_angles):
        theta1 = min_angle + i * step
        for j in range(num_angles):
            theta2 = min_angle + j * step
            for k in range(num_angles):
                theta3 = min_angle + k * step
                # Wyświetlanie rzeczywistych wartości kątów i odpowiadających im współrzędnych XYZ
                print(f"Theta: ({theta1}, {theta2}, {theta3})")
                print("Input angles:", collected_data[i, j, k, :3])
                print("Output XYZ:", collected_data[i, j, k, 3:])
                print()


import pandas as pd

def create_and_save_dataframe(collected_data, csv_filename):
    # Tworzenie listy słowników zawierających dane
    data_list = []

    # Pętla przez wszystkie elementy tablicy
    for i in range(collected_data.shape[0]):
        for j in range(collected_data.shape[1]):
            for k in range(collected_data.shape[2]):
                # Dodawanie danych do listy słowników
                theta1, theta2, theta3 = collected_data[i, j, k, :3]
                x, y, z = collected_data[i, j, k, 3:]
                data_list.append({'Theta1': theta1, 'Theta2': theta2, 'Theta3': theta3,
                                  'X': x, 'Y': y, 'Z': z})

    # Tworzenie DataFrame z listy słowników
    df = pd.DataFrame(data_list)

    # Zapis DataFrame do pliku CSV
    df.to_csv(csv_filename, index=False)
    print(f"DataFrame został zapisany do pliku {csv_filename}")

# Wywołanie funkcji z tablicą collected_data i nazwą pliku CSV

collected_data = generate_collected_data(min_angle, max_angle, step)

# Wywołanie funkcji do wyświetlania danych
display_collected_data(collected_data, min_angle, max_angle, step)
#create_and_save_dataframe(collected_data, "collected_data_10_step_05.csv")
















 







