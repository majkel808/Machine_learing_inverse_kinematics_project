import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf



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

thet1 = -28
thet2 = 38
thet3 = 19

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
print(T_rel_0)
    
print(" ----------") 
#============================================/
#============================================/
#============================================/
#VISUALIZATION OF FORWARD KINEMATICKS
#we need to compuer the forword kinematica for every frame relativ to the frame 0
fig = plt.figure(figsize=(12,10))

ax = fig.add_subplot(111, projection = "3d")
#ax_slide = plt.axes([0.25, 0.1, .65 , 0.03])
#s_theta_1 = Slider(ax_slide, 'THETA 1', valmin = 0, valmax= 2 * np.pi, valinit= np.pi / 2 , valstep= np.pi / 90. )

#updating
#def update(val):
    #current_theta = s_theta_1
    
#tworze vectory oznaczajce pozycje x,y,z poszczególnych Framów
frame_0 = [0, 0, 0] #the refrance ponit of the whole robot, sholud be at the 

def extract_me_some_vector(T, k):
    V = []
    for i in range(3):
        V.append(T[i][k])   
    return V

def frame_vectors(T):
    vx = []
    vy = []
    vz = []
    vx.append(extract_me_some_vector(T, 0))
    vy.append(extract_me_some_vector(T, 1))
    vz.append(extract_me_some_vector(T, 2))
    print(f" vx = {vx}")
    print(f" yx = {vy}")
    print(f" vz = {vz}")
    return vx, vy, vz
    
    
    
def give_me_some_vector(v_start, v_end, color_g, arrow_length_ratio_g):
    ax.quiver(v_start[0],v_start[1],v_start[2], v_end[0], v_end[1], v_end[2], color = color_g, arrow_length_ratio = arrow_length_ratio_g)
    
print(" ----------") 
print(" ----------")  
#give_me_some_vector(Frame_0,  v2, 'red', 0.1)

#tworze vetory od wyznaczonych list macierzy Ta i T rel
vector_T_rel = []
vector_Ta = []

for i in range(Frame_num):
    vector_T_rel.append(extract_me_some_vector(T_rel_0[i], 3))
   
def subrtract_me_some_vector(T, frame0, frame_number):
    V_rel = []
    V_rel.append(T[0])
    for i in range(frame_number - 1):
        V_rel.append(np.subtract(T[i + 1], T[i]))
    return V_rel

V_link = subrtract_me_some_vector(vector_T_rel, frame_0, Frame_num)
print(" ----------") 
print(" ----------") 
print(" ----------") 
print(" ----------") 
for i in range(Frame_num):
    print(V_link[i])
print(" ----------") 
print(" ----------") 
print(" ----------") 
print(" ----------") 
for i in range(Frame_num):
    print(V_link[i])

give_me_some_vector(frame_0, V_link[0], 'red', 0.1)
give_me_some_vector(vector_T_rel[0], V_link[1], 'blue', 0.1)
give_me_some_vector(vector_T_rel[1], V_link[2], 'red', 0.1)
give_me_some_vector(vector_T_rel[2], V_link[3], 'blue', 0.1)

Xv10, Yv10, Zv10 = frame_vectors(T_rel_0[0])


#give_me_some_vector(vector_T_rel[0], Xv10, 'green' , 0.1)
#give_me_some_vector(vector_T_rel[0], Yv10, 'green' , 0.1)
#give_me_some_vector(vector_T_rel[0], Zv10, 'green' , 0.1)
    

ax.set_xlim([-1 * figure_X_lim, figure_X_lim])
ax.set_ylim([-1 * figure_Y_lim, figure_Y_lim])
ax.set_zlim([0 , figure_Z_lim])

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

last_matrix = T_rel_0[-1]
vector_xyz = last_matrix[:3, -1]
print(vector_xyz)
    
print('to jest moj venotr xyz', vector_xyz)
plt.show()
    
    

