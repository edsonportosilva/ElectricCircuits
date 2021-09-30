# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from utils import round_expr, symdisp, symplot
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
# -

from IPython.core.display import HTML
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")


# # *Circuitos Elétricos I - Semana 12*

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

# +
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


# -

# #### Definindo algumas variáveis simbólicas de interesse

s  = sp.symbols('s')
a, R, C  = sp.symbols('a, R, C', real=True, positive=True)
t, τ, omega = sp.symbols('t, τ, omega', real=True)

# ## Exemplos de cálculo da convolução utilizando o sympy
#
#
# ### Exemplo 1: convolução de dois pulsos retangulares

# +
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (0, (t>=2)))

symdisp('x(t) = ', round_expr(x,2))
# -

# plota função no domínio do tempo
intervalo = np.arange(-2, 5, 0.01)
symplot(t, x, intervalo, 'x(t)')

intervalo = np.arange(-5.5, 6.5, 0.1)
for delay in [-2.5, 1, 2.5, 4.5]:
    symplot(t, [espelhaDesloca(x, t, delay), x], intervalo, ['x(t-τ)', 'x(τ)'])

# +
y1 = 0 # 1º intervalo

y2 = sp.integrate(1, (τ, 0, t)) # 2º intervalo

y3 = sp.integrate(1, (τ, t-2, 2)) # 3º intervalo

y4 = 0 # 4º intervalo

y = sp.Piecewise((y1, t<0),
                 (y2, (t>=0)&(t<2)), 
                 (y3, (t>=2)&(t<4)),
                 (y4, (t>=4)))

symdisp('y(t) = ', y)
# -

# plota função no domínio do tempo
intervalo = np.arange(-4, 10, 0.05)
symplot(t, y, intervalo, 'y(t)')

# ### Exemplo 2: resposta de um circuito RC a um pulso

# +
R, C  = sp.symbols('R, C', real=True, positive=True)

τRC = R*C

# +
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (-1, (t>=2)&(t<3)),
                  (0, (t>=3)))


symdisp('x(t) = ', round_expr(x,2))
# -

# plota função no domínio do tempo
intervalo = np.arange(-2, 5, 0.01)
symplot(t, x, intervalo, 'x(t)')

# +
h = (1/τRC)*sp.exp(-t/τRC) # resposta ao impulso de um circuito RC

h = sp.Piecewise((0,t<0),(h, t>=0))

symdisp('h(t) = ', h)

# plota função no domínio do tempo
intervalo = np.arange(-4, 10, 0.05)
symplot(t, h.subs({R:1, C:1}), intervalo, 'h(t)')
# -

intervalo = np.arange(-8, 6, 0.1)
for delay in [-4, 1, 2.5, 3.5]:
    symplot(t, [espelhaDesloca(x, t, delay), h.subs({R:1, C:1})], intervalo, ['x(t-τ)', 'h(τ)'])

# +
x_tau = espelhaDesloca(x, t, τ)
h_tau = h.subs({t:τ})

symdisp('h(τ) = ', h_tau)
symdisp('x(t-τ) = ', round_expr(x_tau,2))
# -

h.args[1][0]

# +
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

# +
y = sp.Piecewise((y1, t<0),
                 (y2, (t>=0)&(t<2)), 
                 (y3, (t>=2)&(t<3)),
                 (y4, (t>=3)))

symdisp('y(t) = ', round_expr(y,2))

# +
C_circ = 100e-6
R_circ = 1e3

intervalo = np.arange(-4, 10, 0.05)

# plota resposta ao impulso 
symplot(t, h.subs({R:R_circ,C:C_circ}), intervalo, 'h(t)')

# plota função no domínio do tempo
symplot(t, [x, y.subs({R:R_circ,C:C_circ})], intervalo, ['x(t)', 'y(t)'])
