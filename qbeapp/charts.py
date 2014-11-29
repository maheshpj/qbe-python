# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 2014

@author: Mahesh.Jadhav

"""
try:
    import matplotlib.pyplot as plt
except ImportError:
    import sys
    print("Matplotlib needed for drawing. Skipping")
    sys.exit(0)
import numpy as np
import qbeapp.errors as errs

def get_axis_from_report_data(report_data):
    x_ax = []
    y_ax = []
    try:    
        for data in report_data:
            if data['chart'] == 'X':
                x_ax.append(data['field'])
            elif data['chart'] == 'Y':
                y_ax.append(data['field'])
    except:
        raise
    if x_ax and y_ax:
        return {'X': x_ax, 'Y': y_ax}
    return None

def get_chart_data(header, results, x, y):
    x_data = [] 
    y_data = []
    try:
        for clm in header:
            if clm == x:            
                x_idx = header.index(clm)
                x_data = [x[x_idx] for x in results]
            elif clm == y:            
                y_idx = header.index(clm)
                y_data = [int(y[y_idx]) for y in results]
    except ValueError as ve:
        raise errs.QBEError("Y axis data should have numeric values.")
    except:
        raise
    if x_data and y_data:
        return {'X': x_data, 'Y': y_data}
    return None
    
def autolabel(rects, ax):
    """
    Attaches some text labels
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height, 
                '%d' % int(height),
                ha='center', va='bottom')

def dyna_chart(title, xlabel, ylabel, legend, x_data, y_data):    
    """
    Shows a bar chart with x and y axis values
    """
    N = len(y_data)
    means = y_data  # (20, 35, 30, 35, 27)
    std =   [2 for x in range(0, N)]

    ind = np.arange(N)  # the x locations for the groups
    width = 0.35       # the width of the bars

    fig, ax = plt.subplots()
    rects = ax.bar(ind, means, width, color='r', yerr=std)
    
    # add some text for labels, title and axes ticks
    ax.set_ylabel(ylabel)
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    ax.set_xticks(ind+width)
    ax.set_xticklabels(x_data) 

    ax.legend((rects), legend)
    autolabel(rects, ax)

    plt.show()

