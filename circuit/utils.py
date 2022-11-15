import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import Math, display
from sympy import lambdify

def genGIF(x, y, figName, xlabel=[], ylabel=[], fram=200, inter=20):    
    '''
    Create and save a plot animation as GIF
     
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
    line,   = ax.plot([], [])
    ax.grid()  

    indx = np.arange(0, len(x), int(len(x)/fram))
    
    if len(xlabel): 
           plt.xlabel(xlabel)
            
    if len(ylabel): 
           plt.ylabel(ylabel)
        
    def init():        
        line.set_data([], [])
        return line,

    def animate(i):
        line.set_data(x[0:indx[i]], y[0:indx[i]])
        return line,

    anim = FuncAnimation(figAnin, animate, init_func=init, frames=fram, interval=inter, blit=True)

    anim.save(figName, dpi=200, writer='imagemagick')
    plt.close()

# função para arredondamento de floats em expressões simbólicas
def round_expr(expr, numDig):
    '''
    Rounds numerical values in sympy expressions
    
    :param expr: sympy symbolic expression
    :param numDig: number of rounding decimals

    :return: rounded expression    
    '''
    return expr.xreplace({n : round(n, numDig) for n in expr.atoms(sp.Number)})

# função para print de expressões simbólicas
def symdisp(expr, var, unit=' '):
    '''
    Latex style display of sympy expressions
    
    :param expr: expression in latex [string]
    :param var: sympy variable, function, expression.
    :param unit: string indicating unit of var [string]
    '''
    display(Math(expr+sp.latex(var)+'\;'+unit))
    
# Função para plot de funções do sympy
def symplot(t, F, interval, funLabel, yLabel=''):
    '''
    Create plots of sympy symbolic functions
    
    :param t: sympy variable
    :param F: sympy function F(t)
    :param interval: array of values of t where F should be evaluated [np.array]
    :param funLabel: curve label be displayed in the plot [string]
    :param yLabel: scale of the plot    
    '''
    fig = plt.figure()
    if type(F) == list:
        indLabel = 0
        for f in F:
            func  = lambdify(t, f, modules=['numpy', {'Heaviside': lambda t:np.heaviside(t,0)}])
            f_num = func(interval)
            
            plt.plot(interval, f_num, label=funLabel[indLabel])
            plt.legend();
            plt.xlim([min(interval), max(interval)]);
            plt.xlabel('tempo [s]');
            plt.ylabel(yLabel)
            indLabel += 1
    else:        
        func  = lambdify(t, F, modules=['numpy', {'Heaviside': lambda t:np.heaviside(t,0)}])
        f_num = func(interval)           
                    
        plt.plot(interval, f_num, label=funLabel)
        plt.legend(loc="upper right");
        plt.xlim([min(interval), max(interval)]);
        plt.xlabel('tempo [s]');  
        plt.ylabel(yLabel)          
    
    plt.grid();
    plt.close();
    return fig


def genConvGIF(x, h, t, totalTime, ti, tf, figName, xlabel=[], ylabel=[], fram=200, inter=20, plotConv=False):    
    '''
    Create and save a convolution plot animation as GIF
     
    :param x: x(t) function [sympy expr]
    :param h: h(t) function [sympy expr]
    :param t: t time variable [sympy variable]
    :param totalTime: array of time instants where the functions will be evaluated [nparray]
    :param ti: time when animation starts [scalar]
    :param tf: time when animation stops [scalar]
    :param figName: figure file name w/ folder path [string]
    :param xlabel: xlabel [string]
    :param ylabel: ylabel [string]
    :param fram: number of frames [int]
    :param inter: time interval between frames [milliseconds]
    
    '''
    x_func = lambdify(t, x, modules=['numpy', {'Heaviside': lambda t:np.heaviside(t,0)}])
    h_func = lambdify(t, h, modules=['numpy', {'Heaviside': lambda t:np.heaviside(t,0)}])
    
    x_num  = x_func(totalTime)
    h_num  = h_func(totalTime)    
    dt = totalTime[1]-totalTime[0]
    
    if plotConv:
        y_num  = np.convolve(h_num, x_num, 'same')*dt
        ymax = np.max([x_num, h_num, y_num])
        ymin = np.min([x_num, h_num, y_num])
    else:
        ymax = np.max([x_num, h_num])
        ymin = np.min([x_num, h_num])
    
    figAnim = plt.figure()
    ax      = plt.axes(xlim=(totalTime.min(), totalTime.max()),ylim=(ymin-0.1*np.abs(ymax), ymax+0.1*np.abs(ymax)))
    line1, line2, line3 = ax.plot([], [], [], [], [], [])
    line1.set_label(ylabel[0])
    line2.set_label(ylabel[1])
    
    if plotConv:
        line3.set_label(ylabel[2])
        
    ax.grid()
    ax.legend(loc="upper right");

    # plot static function
    figh = symplot(t, h, totalTime, 'h(t)')

    if len(xlabel): 
           plt.xlabel(xlabel)            
        
    def init():        
        line1.set_data(figh.get_axes()[0].lines[0].get_data())
        return line1,

    plt.close(figh)
    
    delays = totalTime[::int(len(totalTime)/fram)]
    ind    = np.arange(0, len(totalTime), int(len(totalTime)/fram))
    
    ind    = ind[delays > ti]
    delays = delays[delays > ti]
    
    ind    = ind[delays < tf]   
    delays = delays[delays < tf]
    
    totalFrames = len(delays)
    
    def animate(i):
        figx = symplot(t, x.subs({t:delays[i]-t}), totalTime, 'x(t-τ)')
        line2.set_data(figx.get_axes()[0].lines[0].get_data())
        
        if plotConv:
            line3.set_data(totalTime[0:ind[i]], y_num[0:ind[i]])
            
        plt.close(figx)
        return line2, line3

    anim = FuncAnimation(figAnim, animate, init_func=init, frames=totalFrames, interval=inter, blit=True)

    anim.save(figName, dpi=200, writer='imagemagick')
    plt.close()
