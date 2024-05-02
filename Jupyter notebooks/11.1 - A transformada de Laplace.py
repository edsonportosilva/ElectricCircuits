# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.5
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] colab_type="text" id="view-in-github"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/11.1%20-%20A%20transformada%20de%20Laplace.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="vJ8NIW-RWasq" outputId="765ec4bf-59fc-4929-fed8-2a5332bb42c2"
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

if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install -e .

# + [markdown] id="qbT6MNGLWast"
# # *Circuitos Elétricos I - Semana 11*

# + [markdown] id="fKzZKU2XWasu"
# ### A integral de Laplace
#
# Seja $f(t)$ uma função definida no intervalo $0\leq t \leq \infty$, com $t$ e $f(t)$ reais, então a função $F(s)$, definida pela integral de Laplace
#
# $$\large
# \begin{equation}
# F(s)=\mathcal{L}\{f(t)\}=\int_{0}^{\infty} f(t) e^{-s t} dt,\;\; s \in \mathbb{C},
# \end{equation}
# $$
#
# é conhecida como a transformada de Laplace de $f(t)$.
#
# #### A exponencial complexa
#
# Temos que $s = \sigma + j\omega$, logo
#
# $$ 
# e^{-s t} = e^{-(\sigma + j\omega) t} = e^{-\sigma t}e^{-j\omega t} = e^{-\sigma t} [\cos(\omega t) + j\sin(\omega t)]
# $$
#
# $$ 
# \begin{align}
# \mathcal{L}\{f(t)\}&=\int_{0}^{\infty} f(t) e^{-\sigma t} [\cos(\omega t) + j\sin(\omega t)] dt\\
# \mathcal{L}\{f(t)\}&=\int_{0}^{\infty} f(t) e^{-\sigma t} \cos(\omega t) dt + j\int_{0}^{\infty} f(t) e^{-\sigma t}\sin(\omega t) dt\\
# \mathcal{L}\{f(t)\}&=\int_{0}^{\infty} \left[\frac{f(t)}{e^{\sigma t}}\right] \cos(\omega t) dt + j\int_{0}^{\infty} \left[\frac{f(t)}{e^{\sigma t}}\right]\sin(\omega t) dt
# \end{align}
# $$
#
# **Teorema da existência:** se $f(t)$ é uma função contínua por pedaços para $t$ no intervalo $[a,\infty)$ e é exponencial de ordem $\sigma_0$, então a integral de Laplace converge para $\Re{(s)}>a$.

# + hide_input=false id="glp_L3YXWasv"
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from circuit.utils import round_expr, symdisp, symplot
from circuit.laplace import laplaceT as L
from circuit.laplace import invLaplaceT as invL

# temp workaround
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

# + hide_input=false id="8HcpowpRWasw"
sp.init_printing()

plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False

# + [markdown] id="xmQXq2nvWasw"
# #### Definindo algumas variáveis simbólicas de interesse

# + id="9cGPSDWNWasw"
t     = sp.symbols('t', real=True)
s     = sp.symbols('s')
a     = sp.symbols('a', real=True, positive=True)
omega = sp.symbols('omega', real=True, positive=True)

# + [markdown] id="8pUxtsHyWasx"
# ## Transformada de Laplace no Sympy

# + id="9F_xzy6TWasy" outputId="1fc41908-c91b-431a-c174-16a69c52d38a"
help(sp.laplace_transform)

# + [markdown] id="NUtSb0ooWasy"
# ## Função degrau unitário
#
# #### Domínio do tempo

# + id="gNwe8rgtWasz" outputId="3536513e-9ecf-47d4-b6ed-0546c1df45ec"
f = sp.Heaviside(t) # função degrau unitário

symdisp('f(t) =', f)

# + id="FHFNhJo_Wasz" outputId="33544c32-0a4b-4ee1-b560-0467dcde631d"
# plota função no domínio do tempo
intervalo = np.arange(-4, 4, 0.01)
symplot(t, f, intervalo, 'u(t)')

# + [markdown] id="rGclV7fvWasz"
# #### Domínio de Laplace

# + id="Ypj1IR0SWasz" outputId="fcb63d94-19d1-46df-a867-2866e29d1ed1"
# calcula a transformada de Laplace de u(t)
F = L(f,t,s)

symdisp('F(s) =', F)

# + id="hPHs-TrWWas0" outputId="b3ad5e95-a757-4781-b731-f4e9fae55a95"
f = sp.Heaviside(t-2) # função degrau unitário em t=2

symdisp('f(t) =', f)

# + id="mRmp-9odWas0" outputId="aa4571f5-e566-4331-da8b-17f7c310a41b"
# plota função no domínio do tempo
intervalo = np.arange(-4, 4, 0.01)
symplot(t, f, intervalo, 'u(t-2)')

# + id="DZtaN8CWWas0" outputId="63315eb1-44c5-4dc1-f9d4-70c421511598"
F = L(f,t,s)

symdisp('F(s) =', F)

# + id="12dNcrMzWas0" outputId="9240ea19-49b8-4bf4-e97c-897a877af81c"
u1 = sp.Heaviside(t)   # função degrau unitário em t=0
u2 = sp.Heaviside(t-2) # função degrau unitário em t=2

# plota função no domínio do tempo
intervalo = np.arange(-4, 4, 0.01)
symplot(t, u1-u2, intervalo, 'u(t)-u(t-2)')

# + id="KO0N9IYtWas1" outputId="8d177702-6d1f-406b-cc56-f8005d2cbff0"
G = L(u1-u2,t,s)

symdisp('G(s) =', G)

# + [markdown] id="3ta-wA84Was1"
# ## Função impulso unitário
#
# #### Domínio do tempo

# + id="61e4vLXTWas1" outputId="4e4bcc69-2971-49c3-cb49-9fe96e84409b"
f = sp.DiracDelta(t)

symdisp('f(t) =', f)

# + [markdown] id="JNMFbm2oWas1"
# #### Domínio de Laplace

# + id="htsr9cCtWas2" outputId="a17fea3b-0011-4f5d-aef5-eaec65350415"
# calcula a transformada de Laplace de δ(t)
F = L(f,t,s)

symdisp('F(s) =', F)

# + [markdown] id="w3c-CupKWas2"
# ## Função exponencial
#
# #### Domínio do tempo

# + id="970FNoirWas2" outputId="71931533-98ac-4516-ba65-a7879b94110f"
f = sp.exp(-a*t)

symdisp('f(t) =', f)

# + id="_qwprbkTWas2" outputId="49c07152-755a-4168-c0fd-b3f02908278c"
# plota função no domínio do tempo
intervalo = np.arange(-1, 4, 0.01)
symplot(t, f.subs({a:2}), intervalo, 'f(t)')

# + [markdown] id="qDh36kASWas2"
# #### Domínio de Laplace

# + id="v41paa5PWas2" outputId="fcef2926-1cb1-4fef-c3ba-aa92311d9127"
# calcula a transformada de Laplace de f(t)
F = L(f,t,s)

symdisp('F(s) =', F)

# + [markdown] id="-YxTYCPJWas3"
# ## Função cosseno amortecido
#
# #### Domínio do tempo

# + id="43zMvZoWWas3" outputId="ada178e0-abc9-416f-af29-c9e2e670450b"
g = sp.exp(-a*t)*sp.cos(omega*t)

symdisp('g(t) =', g)

# + id="y7REV06qWas3" outputId="a0287e18-be7c-4512-d219-aabb0c77658c"
# plota função no domínio do tempo
intervalo = np.arange(-1, 4, 0.01)
symplot(t, g.subs({a:2, omega:10}), intervalo, 'g(t)')

# + id="DbiQFOxOWas3" outputId="4a6aa068-6004-4cd3-da92-c844631fb791"
G = L(g,t,s)

symdisp('G(s) =', G)

# + [markdown] id="iacmcxJhWas3"
# ## Resposta subamortecida de um circuito de segunda ordem

# + [markdown] id="ziAYUqWjWas3"
# #### Domínio do tempo

# + id="x_SVsk0lWas3" outputId="66d950ca-d169-499c-af07-677298eca379"
B1, B2 = sp.symbols('B1, B2', real=True)

h = sp.exp(-a*t)*(B1*sp.cos(omega*t) + B2*sp.sin(omega*t))

symdisp('h(t) =', h)

# + [markdown] id="l8VH1LVKWas4"
# #### Domínio de Laplace

# + id="CBvHTpl6Was4" outputId="f2e5587e-d043-4b99-9e0e-cea7076c7e61"
H = L(h,t,s)

symdisp('H(s) =', H.simplify())

# + id="8oh9mcHKWas4" outputId="a981425a-e17e-44e5-de8e-45a9d50fbcc1"
h1 = invL(H,s,t)

symdisp('h_1(t) =', h1)

# + [markdown] id="I_mcP5xIWas4"
# ## Gere sua tabela de transformadas

# + id="xcPOtY3cWas4" outputId="7720c667-e418-4a41-a427-cd2f0ff9f8ef"
func = [1,
         t,
         sp.exp(-a*t),
         t*sp.exp(-a*t),
         t**2*sp.exp(-a*t),
         sp.sin(omega*t),
         sp.cos(omega*t),
         1 - sp.exp(-a*t),
         sp.exp(-a*t)*sp.sin(omega*t),
         sp.exp(-a*t)*sp.cos(omega*t),
         ]
func

symdisp('f(t) =', func)

# + id="5rHST8jcWas4" outputId="1c306715-df3a-43b2-f3af-70cad67be79d"
Fs = [L(f,t,s) for f in func]

symdisp('F(s) =', Fs)
# -

# ## Proprieadades da transformada de Laplace

# +
# from circuit.laplace import laplaceT

# +
f = sp.Function('f', real=True)(t)
g = sp.Function('g', real=True)(t)

a, b = sp.symbols('a, b', real=True, positive=True)
n = sp.symbols('n', integer=True, positive=True)
# -

# ### 1. Linearidade

# + hide_input=false
H = L(a*f + b*g, t, s)

symdisp('\\mathcal{L}_t[af(t) + bg(t)](s) = ', H)

print('Exemplo:')
x = sp.exp(-10*t)

y = sp.exp(-2*t)

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = ', y)

symdisp('X(s) = ', X)
symdisp('Y(s) = ', Y)

symdisp('\\mathcal{L}_t[2x(t) + 3y(t)](s) = ', L(2*x + 3*y,t,s))
# -

# ### 2. Deslocamento (atraso) no tempo

# + hide_input=true
a = sp.symbols('a', real=True, positive=True)

H = L(f.subs({t:t-a})*sp.Heaviside(t-a),t,s)

symdisp('\\mathcal{L}_t\\left[f(t-a)\\right](s) = ', H)
symdisp('a>',0)

print('Exemplo:')
u = sp.Heaviside(t)
x = sp.exp(-2*t)*u

y = x.subs({t:t-4})

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = x(t-4) = ', y)

symdisp('X(s) = ', X)
symdisp('Y(s) = ', Y)

intervalo = np.arange(-1,8, 0.001)
symplot(t,[x, y], intervalo, ['$x(t)$','$y(t)=x(t-4)u(t-4)$'])
# -

# ### 3. Amortecimento no tempo

# + hide_input=true
H = L(sp.exp(-a*t)*f,t,s)

symdisp('\\mathcal{L}_t\\left[e^{-at}f(t)\\right](s) = ', H)
symdisp('a >',0)

print('Exemplo:')
u = sp.Heaviside(t)
x = sp.cos(20*t)*u

y = sp.exp(-t)*x

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = e^{-2t}x(t) = ', y)

symdisp('X(s) = ', X.simplify())
symdisp('Y(s) = ', Y.simplify())

intervalo = np.arange(-1,8, 0.001)
symplot(t,[x, y], intervalo, ['$x(t)$','$y(t)=e^{-t}x(t)$'])
# -

# ### 4. Derivada primeira no tempo

# + hide_input=true
H = L(sp.diff(f,t,1),t,s)

symdisp('\\mathcal{L}_t\\left[\\frac{df(t)}{dt}\\right](s) = ', H)

print('Exemplo:')
u = sp.Heaviside(t)
x = sp.cos(2*t)

y = sp.diff(x,t)

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = \\frac{dx(t)}{dt} = ', y)

symdisp('X(s) = ', X.simplify())
symdisp('Y(s) = ', Y.simplify())

intervalo = np.arange(-1,8, 0.001)
symplot(t,[x, y], intervalo, ['$x(t)$','$y(t)=\\frac{dx(t)}{dt}$'])
# -

# ### 5. Derivada segunda no tempo

# + hide_input=true
H = L(sp.diff(f,t,2),t,s)

symdisp('\\mathcal{L}_t\\left[\\frac{df^{2}(t)}{dt^{2}}\\right](s) = ', H)

print('Exemplo:')
u = sp.Heaviside(t)
x = sp.cos(2*t)

y = sp.diff(x,t,2)

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = \\frac{d^2x(t)}{dt^2} = ', y)

symdisp('X(s) = ', X.simplify())
symdisp('Y(s) = ', Y.simplify())

intervalo = np.arange(-1,8, 0.001)
symplot(t,[x, y], intervalo, ['$x(t)$','$y(t)=\\frac{d^2x(t)}{dt^2}$'])
# -

# ### 6. Mudança de escala no tempo

# + hide_input=true
a = sp.symbols('a', real=True, positive=True)

H = L(f.subs({t:a*t}),t,s)

symdisp('\\mathcal{L}_t\\left[f(at)\\right](s) = ', H)
symdisp('a >',0)

print('Exemplo:')
u = sp.Heaviside(t)
x = sp.cos(2*t)

y = x.subs({t:5*t})

X = L(x,t,s)
Y = L(y,t,s)

symdisp('x(t) = ', x)
symdisp('y(t) = x(5t) = ', y)

symdisp('X(s) = ', X.simplify())
symdisp('Y(s) = ', Y.simplify())

intervalo = np.arange(-1,8, 0.001)
symplot(t,[x, y], intervalo, ['$x(t)$','$y(t)=x(5t)$'])
# -

# ### Expansão em frações parciais

# +
from circuit.laplace import partFrac

t = sp.symbols('t', real=True, positive=True)

# +
F = (s+6)/(s*(s + 1)**2*(s + 3))

symdisp('F(s) = ', F)

symdisp('F(s) = ', round_expr(partFrac(F), 2))

f = invL(F, s, t, partialFractions = False).simplify()

symdisp('f(t) = ', round_expr(f,2))

# +
F = 10*(s+5)/((s+5)**2 + 100)

symdisp('F(s) = ', F)

symdisp('F(s) = ', round_expr(partFrac(F), 2))

f = invL(F, s, t, partialFractions = True).simplify()

symdisp('f(t) = ', round_expr(f,2))
