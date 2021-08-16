import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def genGIF(x, y, figName, xlabel=[], ylabel=[], fram=200, inter=20):    
    '''
    :param x: x-axis values [np array]
    :param y: y-axis values [np array]
    :param figName: figure file name w/ folder path [string]
    :param xlabel: xlabel [string]
    :param ylabel: ylabel [string]
    :param fram: number of frames [int]
    :param inter: time interval between frames [milliseconds]
    
    '''
    figAnin = plt.figure()
    ax      = plt.axes(xlim=(np.min(x), np.max(x)),\
                       ylim=(np.min(y)-0.1*np.max(np.abs(y)), np.max(y)+0.1*np.max(np.abs(y))))
    line,   = ax.plot([], [], lw=2)
    ax.grid()  
    
    if len(xlabel): 
           plt.xlabel(xlabel)
            
    if len(ylabel): 
           plt.ylabel(ylabel)
        
    def init():        
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(x[0:i], y[0:i])
        return line,

    anim = FuncAnimation(figAnin, animate, init_func=init, frames=fram, interval=inter, blit=True)

    anim.save(figName, dpi=100, writer='imagemagick')
    plt.close()
