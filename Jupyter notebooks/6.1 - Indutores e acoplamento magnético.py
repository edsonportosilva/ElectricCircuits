# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%206.1%20-%20Indutores%20e%20acoplamento%20magn%C3%A9tico.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="rXANr_QORwkc"
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install -e .

# +
from IPython.core.display import HTML

import sympy as sp
from sympy import oo
from circuit.utils import symplot, symdisp, round_expr
import numpy as np

HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# + [markdown] id="d3FbA-ZURwkf"
# # *Circuitos Elétricos I - Semana 6*

# + [markdown] id="2As4VIMeRwkg"
# ### Problema 1
#   
# Para o circuito abaixo, tem-se que $v(t)=-1800te^{-20t}$ para $t\geq0$ e $i_1(0)=4\;A$ e $i_2(0)=-16\;A$
#
# a) Determine $i_1(t)$ e $i_2(t)$ para $t\geq0$.\
# b) Determine a energia fornecida à fonte de tensão no intervalo $0\leq t \leq\infty$.\
# c) Determine a energia inicial armazenada nos indutores.\
# d) Determine a energia final armazenada nos indutores.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J8C1.png?raw=1" width="500">

# + id="85hU0BSqRwkh"
# define as variáveis 
t = sp.symbols('t', real=True)

# expressão para a tensão v(t)
v = -1800*t*sp.exp(-20*t)

symdisp('v(t) = ', v, 'V')

# + id="0bPSEMtLRwkh"
tmax = 0.5
intervalo = np.linspace(0, tmax, num=1000)
symplot(t, v, intervalo, funLabel= 'v(t)')

# + id="vtNaD_KaRwki"
# valores das indutâncias
L1 = 10
L2 = 30

# valores iniciais das correntes nos indutores
i1_0 = 4
i2_0 = -16

#i1_0 = 1
#i2_0 = 2

# + id="PCkLBV16Rwki"
# correntes nos indutores em função da tensão aplicada aos terminais
i1 = -(1/L1)*sp.integrate(v, (t, 0, t)) + i1_0
i2 = -(1/L2)*sp.integrate(v, (t, 0, t)) + i2_0

print('Correntes nos indutores:')
symdisp('i_1(t) = ', round_expr(i1, 2) , ' A')
symdisp('i_2(t) = ', round_expr(i2, 2) , ' A')

# + id="zzVJVpy_Rwkj"
tmax = 0.5
intervalo = np.linspace(0, tmax, num=1000)
symplot(t, i1, intervalo, funLabel= '$i_1(t)$')

# + id="hFDmU0DGRwkj"
symplot(t, i2, intervalo, funLabel= '$i_2(t)$')

# + id="NHjcrYvIRwkk"
# LKC
i = i1 + i2

# potência desenvolvida pela fonte
p = v*i

symdisp('p(t) = ', round_expr(p.simplify(),2), 'W')

# + id="QlpzyWWsRwkk"
symplot(t, p, intervalo, funLabel= '$p(t)$')

# + id="CpLtgMhRRwkk"
# energia entrege à fonte
E = sp.integrate(p, (t, 0, oo))

print('Energia entrege à fonte quando t tende a infinito:')
symdisp('E = ', E, 'J')

# + id="zBEJ6L-3Rwkl"
# calculando os valores de energia em t=0

E1_0 = (1/2)*L1*(i1.evalf(subs={t:0}))**2
E2_0 = (1/2)*L2*(i2.evalf(subs={t:0}))**2

print('Energia inicial armazenada nos indutores:')
symdisp('E_1(0) = ', E1_0, 'J')
symdisp('E_2(0) = ', E2_0, 'J')

# + id="GuuXz0y-Rwkl"
# calculando os valores de energia em t =oo

E1_inf = (1/2)*L1*(i1.evalf(subs={t:100}))**2
E2_inf = (1/2)*L2*(i2.evalf(subs={t:100}))**2

print('Energia final armazenada nos indutores:')
symdisp('E_1(\infty) = ', round_expr(E1_inf, 2), 'J')
symdisp('E_2(\infty) = ', round_expr(E2_inf, 2), 'J')

# + id="0GiFsXn9Rwkl"
# calculando a variação de energia nos indutores

ΔE = (E1_inf-E1_0) + (E2_inf-E2_0)

print('Variação da energia armazenada nos indutores:')
symdisp('ΔE = ', round_expr(ΔE,2), 'J')
# + [markdown] id="AJ3NrYU4Rwkm"
# ### Problema 2
#
# Obtendo expressões para as indutâncias equivalentes em circuitos com acoplamento magnético
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J8C2.png?raw=1" width="700">

# + [markdown] id="iKxpvGRLRwkm"
# #### Associação em paralelo

# + [markdown] id="lEGqx1ORRwkn"
# $$
# \begin{aligned}
# &v_L = L_{1} \frac{d i_{1}}{d t}+M \frac{d i_{2}}{d t}\\
# &v_L = L_{2} \frac{d i_{2}}{d t}+M \frac{d i_{1}}{d t}
# \end{aligned}
# $$

# + [markdown] id="dCsvGYK1Rwkn"
# #### Definindo as equações do circuito na forma matricial

# + hide_input=true id="-BEJ-4ENRwkn"
L1, L2, M, vL, t = sp.symbols('L_1, L_2, M, v_L, t', real=True)


# + hide_input=false id="51b2wiSBRwkn" outputId="ffb884a1-b09b-485c-c2d9-4b5ac6e52363"
# define a variável tempo 
t = sp.symbols('t', real=True)

# define as indutâncias
L1, L2, M = sp.symbols('L_1, L_2, M', real=True, positive=True)

# define as correntes i1 e i2
i1 = sp.Function('i_1')(t)
i2 = sp.Function('i_2')(t)

# define a tensão vL
vL = sp.Function('v_L')(t)

# define as equações do circuito no formato matricial
A  = sp.Matrix([[L1, -M],[-M, L2]])
V  = sp.Matrix([[vL],[vL]])

I  = sp.Matrix([[i1],[i2]])
dI = sp.diff(I, t)

symdisp('A = ', A)
symdisp('V = ', V)
symdisp(r'\frac{dI}{dt} = ', dI)

# + [markdown] id="Vj7tXsKxRwko"
# #### Equação da tensão em função das correntes na forma matricial

# + hide_input=false id="do_451ITRwko" outputId="d4d4de8b-e939-4d4c-d1d2-90472c65e298"
sp.Eq(V, A*dI)

# + [markdown] hide_input=true id="DPwstDMNRwko"
# #### Determinado a inversa da matriz de indutâncias $A$

# + hide_input=false id="zOj_322MRwko" outputId="43208b89-c6f3-4aad-b535-f59de8de759b"
# matriz inversa de A
symdisp('A^{-1} = ' , A**-1)

# + [markdown] id="m2Vs8NrnRwkp"
# #### Determinando o vetor de derivadas das correntes

# + hide_input=false id="KGK-9aOaRwkp" outputId="e3c3eae3-8f15-4eb2-efd3-3c2d6c8002c4"
# calcula o vetor de derivadas das correntes
dI = (A**-1)*V

dI.simplify()

symdisp(r'\frac{dI}{dt} = ', dI)

# + [markdown] id="igLuCkLvRwkp"
# #### LKC

# + hide_input=false id="i_9hw3TrRwkp" outputId="773f7ca0-4400-46bc-ed54-dcdcdf3d9cba"
# di0/dt = di1/dt + di2/dt
dI0 = dI[0] + dI[1]

symdisp(r'\frac{di_0}{dt} = \frac{di_1}{dt} + \frac{di_2}{dt} =  ', dI0)

# + [markdown] id="bupkpGp4Rwkp"
# #### Obtendo a expressão para a indutância equivalente

# + hide_input=false id="s3rRPZH6Rwkp" outputId="c279eff9-db05-4ba0-e3d9-9cc801c1d8a2"
# indutância equivalente: vL = Leq*di0/dt -> Leq = vL/di0/dt
Leq = vL/dI0

symdisp('L_{eq} = ', Leq.simplify())

# + [markdown] id="aZenH-aERwkq"
# Exemplos de circuitos com indutância mútua:
#
# Em paralelo: https://tinyurl.com/y9zo85wm \
# Em série: https://tinyurl.com/y7jrvv2y
