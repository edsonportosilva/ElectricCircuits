# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%2012.2%20-%20Integral%20de%20convolu%C3%A7%C3%A3o.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="dKURrKDYU5Fy" outputId="e42a00cf-3bae-472e-9210-2108e79bd748"
from IPython.core.display import HTML
from IPython.display import Image
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    # ! sudo apt update
    # ! sudo apt install imagemagick
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')

# + id="vV0TawY8U5Fv"
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from utils import round_expr, symdisp, symplot, genConvGIF, genGIF
from sympy import oo as inf

from sympy.polys.partfrac import apart

# temp workaround
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False


# + [markdown] id="LuoxcuTtU5Fz"
# # *Circuitos Elétricos I - Semana 12*

# + [markdown] id="4ld2F2UmU5F0"
# ### A integral de convolução
#
# Seja $x(t)$ uma função real definida no intervalo $0\leq t \leq \infty$, $h(t)$ a resposta o impulso de um sistema causal e $y(t)$ a saída do sistema quando $x(t)$ é aplicado na entrada, essas funções estão relacionadas pela integral de convolução
#
# $$\large
# \begin{aligned}
# y(t) &= h(t)\ast x(t) \\
#      &=\int_{-\infty}^{\infty} x(\tau) h(t-\tau) d\tau\\
#      &=\int_{-\infty}^{\infty} h(\tau) x(t-\tau) d\tau
# \end{aligned}
# $$

# + id="v9PKD8TLU5F0"
# transformada de Laplace
def L(f,t,s):
    return sp.laplace_transform(f, t, s, noconds=True)

# transformada inversa de Laplace
def invL(F,s,t):
    return sp.re(sp.inverse_laplace_transform(F, s, t, noconds=True))

# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    coeff = expr.as_numer_denom()
    c0 = sp.poly(coeff[1].cancel()).coeffs()[0]
    
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def partFrac(expr, Ndigits):
    expr = expr.cancel()
    expr = apart(adjustCoeff(expr), s, full=True).doit()
    
    return sp.N(expr, Ndigits)

sp.init_printing()

def espelhaDesloca(g, t, d):    
    return g.subs({t:-t+d})


# + [markdown] id="9H-ZghxAU5F1"
# #### Definindo algumas variáveis simbólicas de interesse

# + id="hlOMK5ljU5F1"
s  = sp.symbols('s')
a, R, C  = sp.symbols('a, R, C', real=True, positive=True)
t, τ, omega = sp.symbols('t, τ, omega', real=True)

# + id="V6UFQQVEU5F2"
generateGIFs = False

# + [markdown] id="zMbKugrhU5F2"
# ## Exemplos de cálculo da convolução utilizando o sympy
#
#
# ### Exemplo 1: convolução de dois pulsos retangulares

# + id="grfmL6eQU5F3" outputId="0ca70cd4-6eaf-4f4e-cd42-b81f7eb5e973"
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (0, (t>=2)))

symdisp('x(t) = ', round_expr(x,2))

# + id="mc5yRDrlU5F3" outputId="d1ddb3e3-b409-446d-a33a-9b29a03b780d"
# plota função no domínio do tempo
intervalo = np.arange(-10, 10, 0.01)
symplot(t, x, intervalo, 'x(t)')

# + id="DV3XnrKRU5F3" outputId="7675691a-136a-41a1-fe09-9f38283abb5a"
# plota função no domínio do tempo
intervalo = np.arange(-10, 10, 0.01)
symplot(t, [x, espelhaDesloca(x,t,0), espelhaDesloca(x,t,-6)], intervalo, ['x(τ)', 'x(-τ)', 'x(-6-τ)'])

# + [markdown] id="JaQAtJcsU5F4"
# **1º Intervalo:** $t<0$ s

# + id="ubWkgMQ0U5F4" outputId="439aaf5d-2543-4a69-d37f-8afaba0b3190"
if generateGIFs:
    ti = -5
    tf = 0

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/conv1-int1.gif'
    genConvGIF(x, x, t, atraso, ti, tf, figName, xlabel= 'τ[s]', ylabel=['x(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv1-int1.gif', width=500)

# + [markdown] id="7gLW3rtDU5F4"
# **2º Intervalo:** $0\leq t < 2$ s

# + id="IQz6VGEEU5F5" outputId="ba300b88-e5cd-453c-c080-def917100d51"
if generateGIFs:
    ti = 0
    tf = 2

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/conv1-int2.gif'
    genConvGIF(x, x, t, atraso, ti, tf, figName, xlabel= 'τ[s]', ylabel=['x(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv1-int2.gif', width=500)

# + [markdown] id="rJOjMd5PU5F5"
# **3º Intervalo:** $2 \leq t <4$ s

# + id="fy_YkRnJU5F5" outputId="cfa683d4-edaa-4519-9db5-d7ca0657a834"
if generateGIFs:
    ti = 2
    tf = 4

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/conv1-int3.gif'
    genConvGIF(x, x, t, atraso, ti, tf, figName, xlabel= 'τ[s]', ylabel=['x(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv1-int3.gif', width=500)

# + [markdown] id="weshSPJeU5F5"
# **4º Intervalo:** $t \geq 4$ s

# + id="CkG-ReMfU5F6" outputId="fd4dba58-d0e4-4631-9cd1-fe203107bae1"
if generateGIFs:
    ti = 4
    tf = 8

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/conv1-int4.gif'
    genConvGIF(x, x, t, atraso, ti, tf, figName, xlabel= 'τ[s]', ylabel=['x(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv1-int4.gif', width=500)

# + id="vl72vjKyU5F6" outputId="d2a52c86-a09a-41cc-d404-1e3ca2112899"
y1 = 0 # 1º intervalo

y2 = sp.integrate(1, (τ, 0, t)) # 2º intervalo

y3 = sp.integrate(1, (τ, t-2, 2)) # 3º intervalo

y4 = 0 # 4º intervalo

y = sp.Piecewise((y1, t<0),
                 (y2, (t>=0)&(t<2)), 
                 (y3, (t>=2)&(t<4)),
                 (y4, (t>=4)))

symdisp('y(t) = ', y)

# + id="Di6rVPc3U5F6" outputId="2e854f8f-ca10-4d79-f97c-d0a76015d59a"
# plota função no domínio do tempo
if generateGIFs:
    ti = -6
    tf = 6

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/fullConv1.gif'
    genConvGIF(x, x, t, atraso, ti, tf, figName, xlabel= 'τ[s]', ylabel=['x(τ)', 'x(t-τ)','y(t)'],\
               fram=200, inter=80, plotConv=True)

Image('./figures/fullConv1.gif', width=500)

# + [markdown] id="Qv9mdTzCU5F7"
# ### Exemplo 2: resposta de um circuito RC a uma sequência de pulsos de tensão

# + id="AdE5DxKWU5F7"
R, C  = sp.symbols('R, C', real=True, positive=True)

τRC = R*C

# + id="H8odujamU5F7" outputId="c1b31d65-a258-4dd5-b5bf-bc5953ac8d44"
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (-1, (t>=2)&(t<3)),
                  (0, (t>=3)))


symdisp('x(t) = ', round_expr(x,2))

# + id="Libsi5TkU5F7" outputId="14fe8c18-eea1-45e7-ccbd-74d2801218ad"
# plota função no domínio do tempo
intervalo = np.arange(-2, 5, 0.01)
symplot(t, x, intervalo, 'x(t)')

# + id="D95o6DEHU5F7" outputId="a526603b-2c82-4bc2-b44d-86eb585f0289"
# plota função no domínio do tempo
intervalo = np.arange(-10, 10, 0.01)
symplot(t, [x, espelhaDesloca(x,t,0), espelhaDesloca(x,t,6)], intervalo, ['x(τ)', 'x(-τ)', 'x(6-τ)'])

# + id="neWPg2KxU5F8" outputId="40402bf6-9d7b-49d1-fba1-b96be2149ce7"
h = (1/τRC)*sp.exp(-t/τRC) # resposta ao impulso da tensão sobre o capacitor num circuito RC

h = sp.Piecewise((0,t<0),(h, t>=0))

symdisp('h(t) = ', h)

# plota função no domínio do tempo
intervalo = np.arange(-4, 10, 0.05)
symplot(t, h.subs({R:1, C:1}), intervalo, 'h(t)')

# + [markdown] id="gVGZwnRbU5F8"
# **1º Intervalo:** $t < 0$ s

# + id="avMJM_dlU5F8" outputId="3dccbecf-4be2-43b7-d4c4-9bb351eccdd2"
if generateGIFs:
    ti = -5
    tf = 0

    atraso = np.arange(-8, 6, 0.01)    
    figName  = './figures/conv2-int1.gif'
    genConvGIF(x, h.subs({R:1, C:1}), t, atraso, ti, tf, figName,\
               xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv2-int1.gif', width=500)

# + [markdown] id="jlAc8t2jU5F8"
# **2º Intervalo:** $0 \leq t < 2$ s

# + id="ZAGHQAJ5U5F8" outputId="5946b988-9083-490f-f6a1-5dc90b6f7b2d"
if generateGIFs:
    ti = 0
    tf = 2

    atraso = np.arange(-8, 6, 0.01)    
    figName  = './figures/conv2-int2.gif'
    genConvGIF(x, h.subs({R:1, C:1}), t, atraso, ti, tf, figName,\
               xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv2-int2.gif', width=500)

# + [markdown] id="hn_J-vjfU5F8"
# **3º Intervalo:** $2\leq t < 3$ s

# + id="QMh0llQ0U5F8" outputId="d612c1b0-ab23-4ed1-c695-dac00f227a89"
if generateGIFs:
    ti = 2
    tf = 3

    atraso = np.arange(-8, 6, 0.01)    
    figName  = './figures/conv2-int3.gif'
    genConvGIF(x, h.subs({R:1, C:1}), t, atraso, ti, tf, figName,\
               xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv2-int3.gif', width=500)

# + [markdown] id="g3EOnwhbU5F9"
# **4º Intervalo:** $t \geq 3$ s

# + id="pF0zfTI4U5F9" outputId="e329f8ee-9154-401f-a58b-247968927497"
if generateGIFs:
    ti = 3
    tf = 6

    atraso = np.arange(-8, 6, 0.01)    
    figName  = './figures/conv2-int4.gif'
    genConvGIF(x, h.subs({R:1, C:1}), t, atraso, ti, tf, figName,\
               xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)'], fram=200, inter=80)

Image('./figures/conv2-int4.gif', width=500)

# + id="TJ7c058RU5F9" outputId="265e8801-a98e-41b3-eee8-7d5b7beeabc6"
x_tau = espelhaDesloca(x, t, τ)
h_tau = h.subs({t:τ})

symdisp('h(τ) = ', h_tau)
symdisp('x(t-τ) = ', round_expr(x_tau,2))

# + id="yKxfdZurU5F-" outputId="8727ed9d-a9f3-4f23-f302-1d83dd3c019a"
h.args[1][0]

# + id="HhMVfl_fU5F-" outputId="abde189e-b1ec-436d-8862-3f6e6abe9653"
h_tau = (h.args[1][0]).subs({t:τ})

y1 = 0 # 1º intervalo: t < 0

print('Para t<0:')
symdisp('y(t)= ', y1)

y2 = sp.integrate(1*h_tau, (τ, 0, t)) # 2º intervalo: t >= 0 e t < 2

print('Para t>=0 e t<2:')
symdisp('y(t)= ', y2)

y3 = sp.integrate(1*h_tau, (τ, t-2, t)) + sp.integrate(-1*h_tau, (τ, 0, t-2)) # 3º intervalo: t >= 2 e t < 3

print('Para t>=2 e t<3:')
symdisp('y(t)= ', round_expr(y3,2))

y4 = sp.integrate(1*h_tau, (τ, t-2, t)) + sp.integrate(-1*h_tau, (τ, t-3, t-2)) # 4º intervalo: t >= 3 

print('Para t>=3:')
symdisp('y(t)= ', round_expr(y4,2))

# + id="oBIlo3qmU5F-" outputId="bfc8f35a-76aa-4463-d4a9-4d5ae7bad008"
y = sp.Piecewise((y1, t<0),
                 (y2, (t>=0)&(t<2)), 
                 (y3, (t>=2)&(t<3)),
                 (y4, (t>=3)))

symdisp('y(t) = ', round_expr(y,2))

# + id="hR3xbxrbU5F_" outputId="1fd1d75f-c90f-481a-f444-58458900b58c"
C_circ = 100e-6
R_circ = 1e3

if generateGIFs:
    ti = -8
    tf = 6

    atraso = np.arange(-6, 6, 0.01)    
    figName  = './figures/fullConv2.gif'
    genConvGIF(x, h.subs({R:R_circ,C:C_circ}), t, atraso, ti, tf,\
               figName, xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)','y(t)'],\
               fram=200, inter=80, plotConv=True)

Image('./figures/fullConv2.gif', width=500)

# + id="dGl-GuzeU5F_" outputId="654e04fb-1431-4f9d-a070-6195a7a266e7"
C_circ = 100e-6
R_circ = 1e3

intervalo = np.arange(-4, 10, 0.05)

# plota resposta ao impulso 
symplot(t, h.subs({R:R_circ,C:C_circ}), intervalo, 'h(t)')

# plota função no domínio do tempo
symplot(t, [x, y.subs({R:R_circ,C:C_circ})], intervalo, ['x(t)', 'y(t)'])

# + id="wGA9X0dzU5F_" outputId="585dba48-49c3-46e7-c90c-18696c4bab48"
print(R_circ*C_circ)
