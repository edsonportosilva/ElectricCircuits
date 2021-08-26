import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import Math, display

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
    
    :param expr: symbolic in Latex [string]
    :param var: sympy expression
    :param unit: string indicating unit of var [string]
    '''
    display(Math(expr+sp.latex(var)+'\;'+unit))
    
# Função para plot de funções do sympy
def symplot(t, F, interval, funLabel):
    '''
    Create plots of sympy symbolic functions
    
    :param t: sympy variable
    :param F: sympy function F(t)
    :param interval: array of values of t where F should be evaluated [np.array]
    :funLabel: curve label be displayed in the plot [string].    
    '''
    plt.figure()
    if type(F) == list:
        indLabel = 0
        for f in F:
            f_num = np.zeros(interval.shape)
 
            for indT in range(0,interval.size):
                f_num[indT] = sp.re(f.doit().evalf(subs={t:interval[indT]}))
            
            plt.plot(interval, f_num, label=funLabel[indLabel])
            plt.legend();
            plt.xlim([min(interval), max(interval)]);
            plt.xlabel('tempo [s]');
            indLabel += 1
    else:
        f_num = np.zeros(interval.shape)
 
        for indT in range(0,interval.size):
            f_num[indT] = sp.re(F.doit().evalf(subs={t:interval[indT]}))
            
        plt.plot(interval, f_num, label=funLabel)
        plt.legend();
        plt.xlim([min(interval), max(interval)]);
        plt.xlabel('tempo [s]');            
    
    plt.grid();
