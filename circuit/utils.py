# -*- coding: utf-8 -*-
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import rc
from IPython.display import Math, display
from sympy import lambdify

def set_preferences():
    """
    Set the preferences for matplotlib plots.
    This function sets various preferences for matplotlib plots, such as font family, figure size, label size, grid lines, and legend style.
    Returns:
        None
    """
    # code implementation here

    rc('font',**{'family':'serif','serif':['Times']})
    rc('text', usetex=True)

    plt.rcParams['axes.facecolor'] = 'whitesmoke'
    plt.rcParams['figure.dpi'] = 220
    plt.rcParams['figure.figsize'] = (16/5,9/5)

    plt.rcParams['axes.labelsize'] = 9
    plt.rcParams['xtick.labelsize'] = 9
    plt.rcParams['ytick.labelsize'] = 9
    plt.rcParams['legend.fontsize'] = 10
    plt.rcParams['font.size'] = 10

    plt.rcParams['axes.linewidth'] =  0.5
    plt.rcParams['grid.linewidth'] =  0.5
    plt.rcParams['lines.linewidth'] =  1
    plt.rcParams['lines.markersize'] =  2
                    
    # Grid lines
    plt.rcParams['axes.grid'] =   False
    plt.rcParams['axes.axisbelow'] =  False
    plt.rcParams['grid.linestyle'] =  'dashed'
    plt.rcParams['grid.color'] =   'k'
    plt.rcParams['grid.alpha'] =   0.25
    plt.rcParams['grid.linewidth'] =   0.25

    # Legend
    plt.rcParams['legend.frameon'] =   False
    plt.rcParams['legend.framealpha'] =   0.25
    plt.rcParams['legend.fancybox'] =   False
    plt.rcParams['legend.numpoints'] =   1

    return None

def symdisp(expr, var=None, unit=None):
    """
    Display sympy expressions in Latex style.

    Parameters
    ----------
    expr : str
        Expression in latex format.
    var : sympy.core.basic.Basic, optional
        Sympy variable, function, or expression. Default is None.
    unit : str, optional
        String indicating the unit of `var`. Default is None.

    Returns
    -------
    None
        
    """
    if unit is None:
        unit=" ";

    if var is None:
        display(Math(expr+ "\\mathrm{"+unit+"}"))
    else:
        display(Math(expr + sp.latex(var) + "\\;" + "\\mathrm{"+unit+"}"))


# função para arredondamento de floats em expressões simbólicas
def round_expr(expr, numDig):
    """
    Round numerical values in sympy expressions.

    Parameters
    ----------
    expr : sympy.core.basic.Basic
        Sympy expression.
    numDig : int
        Number of decimal places.
    
    Returns
    -------
    sympy.core.basic.Basic
        Expression with numerical values rounded to `numDig` decimal places.
        
    """
    return expr.xreplace({n: round(n, numDig) for n in expr.atoms(sp.Number)})


# Função para plot de funções do sympy
def symplot(t, F, interval, funLabel, xlabel=" tempo [s]", ylabel="", figsize=None, xfactor=None, yfactor=None):
    """
    Plot sympy expressions.

    Parameters
    ----------
    t : sympy.core.symbol.Symbol
        Time variable.
    F : sympy.core.basic.Basic
        Sympy expression.
    interval : np.array
        Time interval.
    funLabel : str
        Label for the function.
    xlabel : str, optional
        Label for the x-axis. Default is " tempo [s]".
    ylabel : str, optional
        Label for the y-axis. Default is "".
    figsize : tuple, optional
        Figure size. Default is None.
    xfactor : float, optional
        Factor to scale the x-axis. Default is None.
    yfactor : float, optional
        Factor to scale the y-axis. Default is None.

    Returns 
    -------
    matplotlib.figure.Figure
        Figure object.
    """
    if xfactor is None:
        xfactor = 1

    if yfactor is None:
        yfactor = 1

    if figsize is None:
        fig = plt.figure()
    else:
        fig = plt.figure(figsize=figsize)
    if type(F) == list:
        if type(yfactor) == list:
            for indLabel, f in enumerate(F):
                plotFunc(t, f, interval, funLabel[indLabel], xlabel, ylabel, xfactor, yfactor[indLabel])
        else:
            for indLabel, f in enumerate(F):
                plotFunc(t, f, interval, funLabel[indLabel], xlabel, ylabel, xfactor, yfactor)
    else:
        plotFunc(t, F, interval, funLabel, xlabel, ylabel, xfactor, yfactor)

    plt.grid()
    plt.close()
    return fig


def plotFunc(t, F, interval, funLabel, xlabel, ylabel, xfactor, yfactor):
    """
    Plots a given function F over a specified interval.

    Parameters
    ----------

    t : sympy.Symbol
        The symbolic variable used in the function F.
    F : sympy.Expr
        The symbolic expression representing the function to be plotted.
    interval : numpy.ndarray
        The range of values over which to evaluate and plot the function.
    funLabel : str
        The label for the function to be used in the plot legend.
    xlabel : str
        The label for the x-axis of the plot.
    ylabel : str
        The label for the y-axis of the plot.
    xfactor : float
        The factor by which to scale the x-axis values.
    yfactor : float
        The factor by which to scale the y-axis values.
    
    Returns
    -------
    None

    """    
    func = lambdify(
        t, F, modules=["numpy", {"Heaviside": lambda t: np.heaviside(t, 0)}]
    )
    f_num = func(interval)

    plt.plot(interval/xfactor, f_num/yfactor, label=funLabel)
    plt.legend()
    plt.xlim([min(interval/xfactor), max(interval/xfactor)])
    plt.xlabel(f'${xlabel}$')
    plt.ylabel(ylabel)

def genGIF(x, y, figName, xlabel=[], ylabel=[], title=[], plotcols=[], centralAxes=False, squareAxes=False, fram=200, inter=20):    
    """
    Create and save a plot animation as GIF.

    Parameters
    ----------
    x : np.array
        x-axis values.
    y : np.array
        y-axis values.
    figName : str
        Figure file name with folder path.
    xlabel : str, optional
        Label for the x-axis. Defaults to an empty list.
    ylabel : str, optional
        Label for the y-axis. Defaults to an empty list.
    title : str, optional
        Title of the plot. Defaults to an empty list.
    plotcols : list, optional
        List of colors for the plot lines. Defaults to an empty list.
    centralAxes : bool, optional
        If True, moves the axes to the center. Defaults to False.
    squareAxes : bool, optional
        If True, sets the axes to be square. Defaults to False.
    fram : int, optional
        Number of frames in the animation. Defaults to 200.
    inter : int, optional
        Time interval between frames in milliseconds. Defaults to 20.

    Returns
    -------
    None

    """
    figAnin = plt.figure()
    
    #if squareAxes:
    #plt.axis('square')

    May = np.max(np.abs(y))
    min_y = np.min(y)
    max_y = np.max(y)

    Max = np.max(np.abs(x))
    min_x = np.min(x)
    max_x = np.max(x)


    Max_xy = np.max([np.abs(x), np.abs(y)])
    min_xy = np.min([x, y])
    max_xy = np.max([x, y])

    if squareAxes:
        #plt.axis('equal')
        ax = plt.axes(            
            ylim=(
                 min_xy - 0.1 * Max_xy,
                 max_xy + 0.1 * Max_xy,
            ),
            xlim=(
                 min_xy - 0.1 * Max_xy,
                 max_xy + 0.1 * Max_xy,
            ),
        )
    else:
        ax = plt.axes(
            xlim=(min_x, max_x),
            ylim=(
                min_y - 0.1 * May,
                max_y + 0.1 * May,
            ),
        )

    if not len(plotcols):
        prop_cycle = plt.rcParams['axes.prop_cycle']
        colors = prop_cycle.by_key()['color']
        plotcols= colors[:2]
    #print(colors)

    lines = []
    for index in range(2):
        if index == 0:
            lobj = ax.plot([],[],lw=2,color=plotcols[index])[0]
        else:
            lobj = ax.plot([],[],'o',lw=2,color=plotcols[index])[0]
        lines.append(lobj)

   # (line,) = ax.plot([], [])
    ax.grid()

    plt.axhline(color='black', lw=1)
    plt.axvline(color='black', lw=1)

    if centralAxes:
        # Move left y-axis and bottom x-axis to centre, passing through (0,0)
        ax.spines['left'].set_position('center')
        ax.spines['bottom'].set_position('center')

        # Eliminate upper and right axes
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')

        # Show ticks in the left and lower axes only
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

    indx = np.arange(0, len(x), int(len(x) / fram))

    if len(xlabel):
        plt.xlabel(xlabel)

    if len(ylabel):
        plt.ylabel(ylabel)

    if len(title):
        plt.title(title)

    def init():
        for line in lines:
            line.set_data([], [])
        return lines

    def animate(i):
        for idx, line in enumerate(lines):
            if idx == 0:
                line.set_data(x[:indx[i]], y[:indx[i]])
            else:
                line.set_data(x[indx[i]], y[indx[i]])

        return lines

    anim = FuncAnimation(
        figAnin,
        animate,
        init_func=init,
        frames=fram,
        interval=inter,
        blit=True,
    )

    anim.save(figName, dpi=200, writer="imagemagick")
    plt.close()

def genConvGIF(    
    x,
    h,
    t,
    totalTime,
    ti,
    tf,
    figName,
    xlabel=[],
    ylabel=[],
    fram=200,
    inter=20,
    plotConv=False,
):
    """
    Generate a GIF animation of the convolution of two functions.

    Parameters
    ----------
    x : sympy.Expr
        The first function to be convolved.
    h : sympy.Expr
        The second function to be convolved.
    t : sympy.Symbol
        The time variable.
    totalTime : numpy.ndarray
        Array of time values over which the functions are evaluated.
    ti : float
        Initial time for the animation.
    tf : float
        Final time for the animation.
    figName : str
        The name of the output GIF file.
    xlabel : list, optional
        List of labels for the x-axis (default is []).
    ylabel : list, optional
        List of labels for the y-axis (default is []).
    fram : int, optional
        Number of frames in the animation (default is 200).
    inter : int, optional
        Interval between frames in milliseconds (default is 20).
    plotConv : bool, optional
        Whether to plot the convolution result (default is False).
    
    Returns
    -------
    None
    
    """
    x_func = lambdify(
        t, x, modules=["numpy", {"Heaviside": lambda t: np.heaviside(t, 0)}]
    )
    h_func = lambdify(
        t, h, modules=["numpy", {"Heaviside": lambda t: np.heaviside(t, 0)}]
    )

    x_num = x_func(totalTime)
    h_num = h_func(totalTime)
    dt = totalTime[1] - totalTime[0]

    if plotConv:
        y_num = np.convolve(h_num, x_num, "same") * dt
        ymax = np.max([x_num, h_num, y_num])
        ymin = np.min([x_num, h_num, y_num])
    else:
        ymax = np.max([x_num, h_num])
        ymin = np.min([x_num, h_num])

    figAnim = plt.figure()
    ax = plt.axes(
        xlim=(totalTime.min(), totalTime.max()),
        ylim=(ymin - 0.1 * np.abs(ymax), ymax + 0.1 * np.abs(ymax)),
    )
    line1, line2, line3 = ax.plot([], [], [], [], [], [])
    line1.set_label(ylabel[0])
    line2.set_label(ylabel[1])

    if plotConv:
        line3.set_label(ylabel[2])

    ax.grid()
    ax.legend(loc="upper right")

    # plot static function
    figh = symplot(t, h, totalTime, "h(t)")

    if len(xlabel):
        plt.xlabel(xlabel)

    def init():
        line1.set_data(figh.get_axes()[0].lines[0].get_data())
        return (line1,)

    plt.close(figh)

    delays = totalTime[:: int(len(totalTime) / fram)]
    ind = np.arange(0, len(totalTime), int(len(totalTime) / fram))

    ind = ind[delays > ti]
    delays = delays[delays > ti]

    ind = ind[delays < tf]
    delays = delays[delays < tf]

    totalFrames = len(delays)

    def animate(i):
        figx = symplot(t, x.subs({t: delays[i] - t}), totalTime, "x(t-τ)")
        line2.set_data(figx.get_axes()[0].lines[0].get_data())

        if plotConv:
            line3.set_data(totalTime[:ind[i]], y_num[:ind[i]])

        plt.close(figx)
        return line2, line3

    anim = FuncAnimation(
        figAnim,
        animate,
        init_func=init,
        frames=totalFrames,
        interval=inter,
        blit=True,
    )

    anim.save(figName, dpi=200, writer="imagemagick")
    plt.close()

def responseRL(i_t0, i_inf, t0, R, L):    
    """
    Calculate the current and voltage response of an RL circuit.

    Parameters
    ----------
    i_t0 : float
        Initial current through the inductor at time t0.
    i_inf : float
        Steady-state current through the inductor as time approaches infinity.
    t0 : float
        Initial time.
    R : float
        Resistance in ohms.
    L : float
        Inductance in henrys.

    Returns
    ------- 
    iL : sympy.Expr
        Current through the inductor as a function of time.
    vL : sympy.Expr
        Voltage across the the inductor as a function of time.
    τ : float
        Time constant of the RL circuit.
    t : sympy.Symbol
        Symbolic time variable.
    """    
    t = sp.symbols("t", real=True)
    τ = L / R

    iL = i_inf + (i_t0 - i_inf) * sp.exp(-t / τ)

    vL = L * sp.diff(iL, t)

    iL = iL.subs(t, sp.UnevaluatedExpr(t - t0))
    vL = vL.subs(t, sp.UnevaluatedExpr(t - t0))

    iL = sp.Piecewise((i_t0, t < t0), (iL, True))
    vL = sp.Piecewise((0, t < t0), (vL, True))

    return iL, vL, τ, t


def responseRC(v_t0, v_inf, t0, R, C):
    """
    Symbolically solves the transient response of an RC circuit.

    Parameters
    ----------
    v_t0 : float
        Initial voltage across the capacitor.
    v_inf : float
        Final voltage across the capacitor.
    t0 : float
        Initial time instant.
    R : float
        Resistance.
    C : float
        Capacitance.

    Returns
    -------
    vC : sympy.Expr
        Voltage across the capacitor as a function of time.
    iC : sympy.Expr
        Current through the capacitor as a function of time.
    τ : float
        Time constant of the RC circuit.
    t : sympy.Symbol
        Symbolic time variable.
    """
    t = sp.symbols("t", real=True)
    τ = R * C

    vC = v_inf + (v_t0 - v_inf) * sp.exp(-t / τ)

    iC = C * sp.diff(vC, t)

    iC = iC.subs(t, sp.UnevaluatedExpr(t - t0))
    vC = vC.subs(t, sp.UnevaluatedExpr(t - t0))

    iC = sp.Piecewise((0, t < t0), (iC, True))
    vC = sp.Piecewise((v_t0, t < t0), (vC, True))

    return vC, iC, τ, t


def responseRLCpar(vC_t0, iL_t0, iL_inf, t0, R, L, C):
    """
    Symbolically solves the transient response of a parallel RLC circuit
  
    Parameters
    ----------
    vC_t0 : float
        Capacitor's voltage value at t0.
    iL_t0 : float
        Inductor's current value at t0.
    iL_inf : float
        Inductor's current final value.
    t0 : float
        Initial time instant.
    R : float
        Resistance.
    L : float
        Inductance.
    C : float
        Capacitance.

    Returns
    -------
    α : float
        Neper's frequency.
    ω0 : float
        Resonant frequency.
    iL(t) : sympy.Expr
        Inductor's current.
    vC(t) : sympy.Expr
        Capacitor's voltage.
    resp : str
        Type of response.
    t : sympy.Symbol
        Symbolic time variable.
    """
    α = 1 / (2 * R * C)
    ω0 = 1 / np.sqrt(L * C)

    t = sp.symbols("t", real=True)

    if np.isclose(α, ω0, rtol=1e-05, atol=1e-4):
        resp = "resp. critic. amortecida"
    elif α > ω0:
        resp = "resp. superamortecida"
    else:
        resp = "resp. subamortecida"

    if not np.isclose(α, ω0, rtol=1e-05, atol=1e-4):
        if α > ω0:
            s1 = -α + np.sqrt(α ** 2 - ω0 ** 2)
            s2 = -α - np.sqrt(α ** 2 - ω0 ** 2)
        elif α < ω0:
            s1 = -α + 1j * np.sqrt(ω0 ** 2 - α ** 2)
            s2 = -α - 1j * np.sqrt(ω0 ** 2 - α ** 2)

        A1, A2 = sp.symbols("A1, A2")

        # define os sistema de equações com as condições iniciais
        eq1 = sp.Eq(A1 + A2 + iL_inf, iL_t0)
        eq2 = sp.Eq(s1 * A1 + s2 * A2, vC_t0 / L)

        # resolve o sistema
        soluc = sp.solve((eq1, eq2), dict=True)
        A1 = np.array([sol[A1] for sol in soluc])
        A2 = np.array([sol[A2] for sol in soluc])

        A1 = A1[0]
        A2 = A2[0]

        iL = A1 * sp.exp(s1 * t) + A2 * sp.exp(s2 * t)
        iL = sp.re(iL)
    else:
        s1 = -α
        s2 = -α

        D1, D2 = sp.symbols("D1, D2")

        # define os sistema de equações com as condições iniciais
        eq1 = sp.Eq(D1 + iL_inf, iL_t0)
        eq2 = sp.Eq(-α * D1 + D2, vC_t0 / L)

        # resolve o sistema
        soluc = sp.solve((eq1, eq2), dict=True)
        D1 = np.array([sol[D1] for sol in soluc])
        D2 = np.array([sol[D2] for sol in soluc])

        D1 = D1[0]
        D2 = D2[0]

        iL = D1 * sp.exp(s1 * t) + D2 * t * sp.exp(s2 * t)
    iL = sp.simplify(iL) + iL_inf
    vC = L * sp.diff(iL, t)
    vC = sp.simplify(vC)

    iL = iL.subs(t, sp.UnevaluatedExpr(t - t0))
    vC = vC.subs(t, sp.UnevaluatedExpr(t - t0))

    iL = sp.Piecewise((iL_t0, t < t0), (iL, True))
    vC = sp.Piecewise((vC_t0, t < t0), (vC, True))

    return α, ω0, iL, vC, resp, t


def responseRLCser(vC_t0, iL_t0, vC_inf, t0, R, L, C):
    """
    Symbolically solves the transient response of a series RLC circuit

    Parameters
    ----------
    vC_t0 : float
        Capacitor's voltage value at t0.
    iL_t0 : float
        Inductor's current value at t0.
    vC_inf : float
        Capacitor's voltage final value.
    t0 : float
        Initial time instant.
    R : float
        Resistance.
    L : float
        Inductance.
    C : float
        Capacitance.

    Returns
    -------
    α : float
        Neper's frequency.
    ω0 : float
        Resonant frequency.
    iL(t) : sympy.Expr
        Inductor's current.
    vC(t) : sympy.Expr
        Capacitor's voltage.
    resp : str
        Type of response.
    t : sympy.Symbol
        Symbolic time variable.
    
    """
    α = R / (2 * L)
    ω0 = 1 / np.sqrt(L * C)

    t = sp.symbols("t", real=True)

    if np.isclose(α, ω0, rtol=1e-05, atol=1e-4):
        resp = "resp. critic. amortecida"
    elif α > ω0:
        resp = "resp. superamortecida"
    else:
        resp = "resp. subamortecida"

    if not np.isclose(α, ω0, rtol=1e-05, atol=1e-4):
        if α > ω0:
            s1 = -α + np.sqrt(α ** 2 - ω0 ** 2)
            s2 = -α - np.sqrt(α ** 2 - ω0 ** 2)
        elif α < ω0:
            s1 = -α + 1j * np.sqrt(ω0 ** 2 - α ** 2)
            s2 = -α - 1j * np.sqrt(ω0 ** 2 - α ** 2)

        A1, A2 = sp.symbols("A1, A2")

        # define os sistema de equações com as condições iniciais
        eq1 = sp.Eq(A1 + A2 + vC_inf, vC_t0)
        eq2 = sp.Eq(s1 * A1 + s2 * A2, iL_t0 / C)

        # resolve o sistema
        soluc = sp.solve((eq1, eq2), dict=True)
        A1 = np.array([sol[A1] for sol in soluc])
        A2 = np.array([sol[A2] for sol in soluc])

        A1 = A1[0]
        A2 = A2[0]

        vC = A1 * sp.exp(s1 * t) + A2 * sp.exp(s2 * t)
        vC = sp.re(vC)
    else:
        s1 = -α
        s2 = -α

        D1, D2 = sp.symbols("D1, D2")

        # define os sistema de equações com as condições iniciais
        eq1 = sp.Eq(D1 + vC_inf, vC_t0)
        eq2 = sp.Eq(-α * D1 + D2, iL_t0 / C)

        # resolve o sistema
        soluc = sp.solve((eq1, eq2), dict=True)
        D1 = np.array([sol[D1] for sol in soluc])
        D2 = np.array([sol[D2] for sol in soluc])

        D1 = D1[0]
        D2 = D2[0]

        vC = D1 * sp.exp(s1 * t) + D2 * t * sp.exp(s2 * t)
    vC = sp.simplify(vC) + vC_inf
    iL = C * sp.diff(vC, t)
    iL = sp.simplify(iL)

    iL = iL.subs(t, sp.UnevaluatedExpr(t - t0))
    vC = vC.subs(t, sp.UnevaluatedExpr(t - t0))

    iL = sp.Piecewise((iL_t0, t < t0), (iL, True))
    vC = sp.Piecewise((vC_t0, t < t0), (vC, True))

    return α, ω0, iL, vC, resp, t


def responseRLCser_num(R, L, C, vC_t0, iL_t0, Vs, t):
    """
    Numerically solves the transient response of a series RLC circuit.

    Parameters
    ----------
    R : float
        Resistance value.
    L : float
        Inductance value.
    C : float
        Capacitance value.
    vC_t0 : float
        Initial voltage across the capacitor.
    iL_t0 : float
        Initial current through the inductor.
    Vs : np.array
        Source voltage as a function of time.
    t : np.array
        Time array.

    Returns
    -------
    i : np.array
        Current through the circuit.
    vR : np.array
        Voltage across the resistor.
    vL : np.array
        Voltage across the inductor.
    vC : np.array
        Voltage across the capacitor.
    """
    vC = np.zeros(t.shape)
    x = np.zeros(t.shape)

    # EDO da tensão sobre o capacitor: vc''(t)+(R/L)vc'(t)+vc(t)/LC = vs(t)/LC

    # Solução numérica:
    vC[0] = vC_t0  # condição incial de vc
    x[0] = iL_t0 / C  # condição inicial da derivada vc'(t)

    # Integração numérica via método de Euler:
    deltaT = t[1] - t[0]  # passo de integração

    for kk in range(len(t) - 1):
        vC[kk + 1] = vC[kk] + x[kk] * deltaT  # calcula vc(t+deltaT)
        x[kk + 1] = (
            x[kk] + (-R / L * x[kk] - 1 / (L * C) * (vC[kk] - Vs[kk])) * deltaT
        )  # calcula vc'(t+deltaT)

    # cálculo das tensões e da corrente partir de vc(t):
    i = np.append(iL_t0, C * np.diff(vC) / np.diff(t))  # corrente no circuito
    vR = R * i  # tensão sobre o resistor
    vL = Vs - vR - vC  # tensão sobre o indutor(LKT)

    return i, vR, vL, vC


def YΔ(R1, R2, R3):
    """
    Convert a Y network to a Δ network.

    Parameters
    ----------
    R1 : float
        Resistance of the first branch.
    R2 : float
        Resistance of the second branch.
    R3 : float
        Resistance of the third branch.

    Returns
    -------
    Ra : float
        Resistance of the first branch in the Δ network.
    Rb : float
        Resistance of the second branch in the Δ network.
    Rc : float
        Resistance of the third branch in the Δ network.
    """
    x = R1 * R2 + R2 * R3 + R3 * R1
    Ra = x / R1
    Rb = x / R2
    Rc = x / R3

    return Ra, Rb, Rc


def ΔY(Ra, Rb, Rc):
    """
    Convert a Δ network to a Y network.

    Parameters
    ----------
    Ra : float
        Resistance of the first branch in the Δ network.
    Rb : float
        Resistance of the second branch in the Δ network.
    Rc : float
        Resistance of the third branch in the Δ network.

    Returns
    -------
    R1 : float
        Resistance of the first branch.
    R2 : float
        Resistance of the second branch.
    R3 : float
        Resistance of the third branch.
    """
    x = Ra + Rb + Rc
    R1 = (Rb * Rc) / x
    R2 = (Ra * Rc) / x
    R3 = (Rb * Ra) / x

    return R1, R2, R3

def par(*R):
    """
    Calculate the equivalent resistance of resistors in parallel.

    Parameters
    ----------
    R : float
        Resistances in parallel.
    
    Returns
    -------
    float
        Equivalent resistance.
    """
    r = sum(1/u for u in R)
    return 1/r
