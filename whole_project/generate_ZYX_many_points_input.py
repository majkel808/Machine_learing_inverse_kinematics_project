# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 12:37:20 2024

@author: 1mich
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:43:46 2024

@author: 1mich
"""
import numpy as np
import pandas as pd

def generate_array(positions, iteration):  

    for i in range(len(positions)-1):
        x_collumn = np.linspace(positions[i][0],positions[i+1][0],iteration)
        y_collumn = np.linspace(positions[i][1],positions[i+1][1],iteration)  
        z_collumn = np.linspace(positions[i][2],positions[i+1][2],iteration)
        
        output_array_temp = np.column_stack((x_collumn,y_collumn, z_collumn))
        
        if i == 0:
            output_array = output_array_temp 
        else:
            output_array = np.concatenate((output_array, output_array_temp), axis=0)

    #print(output_array)
    
    df = pd.DataFrame(output_array,columns=['X', 'Y', 'Z'])
    
    return output_array, df
positions = [[-5, 0, 8],[0, -5, 8],[0, -5, 4],[-5, 0, 4],[-5, 0, 8]]
XYZ_start = [0, -5, 9]
XYZ_end = [-5, 0, 9]

interation = 50

xyz_input, xyz_dataframe = generate_array(positions, interation)
xyz_dataframe.head(10)
xyz_dataframe.to_csv("xyz_many_input_2.csv", index=False)