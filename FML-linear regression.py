# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 12:54:20 2021

@author: Zahid Ur Rahman
"""

x = [] # Square size
y = [] # Housing Price
with open('House DS.csv', 'r') as file:
# read header
    file.readline()
    # loop over the file, filling the lists with x and y vectors
    for line in file:
        row = line.split(',') 
        x.append(float(row[0]))
        y.append(float(row[1]))
def average(x):
    return sum(x) / len(x)
#Using this function obtain the average of each variable of the problem:
avg_x = average(x)
avg_y = average(y)
a1_num = sum([(xi-avg_x)*(yi-avg_y) for(xi,yi) in zip(x,y)])
a1_den = sum([(xi-avg_x)**2 for xi in x])
a1 = a1_num/a1_den
a0 = avg_y - a1*avg_x
print('Parameter a0 = ', a0)
print('Parameter a1 = ', a1)
sqres = sum([(yi - (a1*xi+a0))**2 for(xi, yi) in zip(x, y)])
sqtot = sum([(yi - avg_y)**2 for yi in y])
R2 = 1 - sqres/sqtot
print('Coefficient of Determination R2 = ',R2)
J = sqres
print('Final Cost J = {:.3e}'.format(J))