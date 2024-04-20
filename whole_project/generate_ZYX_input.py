# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 16:43:46 2024

@author: 1mich
"""
import numpy as np
import pandas as pd

def generate_array(x1,y1,z1,x2,y2,z2, iteration):  
    
    x_collumn = np.linspace(x1,x2,iteration)
    y_collumn = np.linspace(y1,y2,iteration)   
    z_collumn = np.linspace(z1,z2,iteration) 

    output_array = np.column_stack((x_collumn,y_collumn, z_collumn))
    
    df = pd.DataFrame({"X": x_collumn, "Y": y_collumn, "Z": z_collumn})
    
    return output_array, df

#XYZ_start = [0, -5, 9] #best point
XYZ_start = [-5, 0, 9]
XYZ_end = [-5, 0, 4]
interation = 100

xyz_input, xyz_dataframe = generate_array(XYZ_start[0], XYZ_start[1], XYZ_start[2], XYZ_end[0], XYZ_end[1], XYZ_end[2], interation)
xyz_dataframe.head(10)
xyz_dataframe.to_csv("xyz_input_2.csv", index=False)