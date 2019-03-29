# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 10:09:04 2019

@author: Zha_Jiajia
"""

import numpy as np

''' Read data from originalfile and obtain the maxium number for each column
and print them to targetfile '''

f1 = open('originalfile_name', 'r')
f2 = open('targetfile_name', 'w')
numlist = []
for line in f1:
    numlist.append([float(x) for x in line.split(' ')])
f1.close()
numlist = np.array(numlist)
row, column = numlist.shape
for i in range(1, column):
    print(-50+2.5*(i-1), max(numlist[:, i]), file=f2)

f2.close()
