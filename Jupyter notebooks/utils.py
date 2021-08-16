import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def genGIF(x, y, figName, xlabel=[], ylabel=[], fram=200, inter=20):    
    
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
