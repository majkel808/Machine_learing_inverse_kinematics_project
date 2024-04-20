# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 17:33:20 2024

@author: 1mich
"""

import numpy as np
import matplotlib.pyplot as plt


#definig slider

#constant values
L1 = 4
L2 = 5
L3 = 5
Frame_num = 4
figure_X_lim = 10
figure_Y_lim = 10
figure_Z_lim = 15


#variable values


d2 = 15

thet1 = 90
thet2 = 90
thet3 = 90 

theta1 = np.deg2rad(thet1)

theta2 = np.deg2rad(thet2)
theta3 = np.deg2rad(thet3)

#DH_alfa = np.array([0, np.pi / 2, 0, 0])
#DH_a = np.array([0, 0 , 0, 0])
#DH_d =np.array([L1, d2, L2, L3])
#DH_theta = np.array([theta1, 0, theta2, 0])

#DH paramteres for RPR robotic maniupulator[kazdyw wiersz to inne zmienna DH]
#tak łatwiej wpisywac ale klasyczeni jest to transponowane
#DH_p_basic = np.array([[0,      np.pi/2,   0,      0],
#                       [0,      0 ,        0,      0],
#                      [L1,     d2,        L2,     L3],
#                      [theta1, 0,         theta3, 0]])
DH_p_basic = np.array([[0,      np.pi  /2,         0,      0],
                       [0,      0 ,        L2,            L3],
                       [L1,     0,         0,              0],
                       [theta1, theta2,    theta3,         0]])
DH_p = np.transpose(DH_p_basic)
print(DH_p)

#Genrating tranformation matrix for relation of frame i to frame i-1:
    
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
#monozenie macierzy o wiekszej liczbie matruixow niz 3

def matrix_mul_more(lista, frame_num):
    temp = lista[0]
    T = lista[0]
    for i in range(frame_num - 1):
        T = np.matmul(temp, lista[i+1])
        temp = T
    return T 
    
#trans matrix for i frame in relation to fram i - 1 
Ta = []
for  i in range(Frame_num):
    Ta.append(Trans_matrix(DH_p, i))
    
for i in range(Frame_num):
    print(Ta[i])
    
print(" ----------")

#trans matrix for every frame in relation to frame 0, the last frame is calucaltion for For_kiu for this robot
T_rel_0 = []
for i in range(Frame_num):
    T_rel_0.append(matrix_mul_more(Ta, i+1))

for i in range(Frame_num):
    print('cos',T_rel_0[i])
print(" ----------")   
print(" macierz koncowa") 
print(" ----------") 
last_matrix = T_rel_0[-1]
vector_xyz = last_matrix[:3, -1]
print(vector_xyz)
    
