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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%2010%20-%20Exerc%C3%ADcio%20circuito%20RL%20equivalente.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="ILDj89ZbXcXp"
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')

# + [markdown] id="QyZiYz1zXbe0"
# # *Circuitos Elétricos I - Semana 10*

# + [markdown] id="1Xabg8wNXbe3"
# ### Problema 1
#   
# (Problema 7.19 - Nilsson) Para o circuito abaixo, pede-se:
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J13C1.png?raw=1" width="400">
#
# a) Determine a tensão $v_0(t)$ sobre o indutor de $48\;mH$ para $t\geq0$.\
# b) Determine a corrente $i_0(t)$ sobre o indutor de $48\;mH$ para $t\geq0$.\
# c) Determine a energia consumida pelo resistor de $2.5\;k\Omega$ no intervalo $0\leq t \leq\infty$.
#
# Link para a simulação do circuito: https://tinyurl.com/yj69udn8

# + id="Bx0x88LzXbe4"
# valores das indutâncias
L1 = 20e-3
L2 = 80e-3
L3 = 48e-3

# valores iniciais das correntes
i1_0 = 5e-3
i2_0 = 5e-3
i3_0 = 0

# + id="Z9cvnJvgXbe5" outputId="865c9c25-7f4f-44c3-cf06-11ce91719474"
# indutância equivalente
Leq1 = (L2*L3)/(L2+L3)
Leq  = L1 + Leq1

print('Leq = ', Leq/1e-3, ' mH')

# + id="RsYxzq9GXbe6" outputId="0e8da163-3749-4c5f-9746-c4c15f119117"
R = 2.5e3

# constante de tempo
τ = Leq/R

print('τ = ', τ, ' s')

# + id="90uaJsdUXbe6" outputId="0b1edbda-3e14-4b51-a814-75616fe48ab7"
import sympy as sp

iL_inf = 0
iL_0   = i1_0

# define as variável tempo 
t = sp.symbols('t')

# define i(t)
iL = iL_inf + (iL_0 - iL_inf)*sp.exp(-t/τ)

print('Corrente no indutor equivalente:')
print('iL(t) = ', iL/1e-3 , ' mA')

# + id="rZawDEuGXbe7" outputId="b6e5d52b-60b5-4f38-b601-553bd6d7bd42"
# calcula v0
v0 = Leq1*sp.diff(iL,t)

print('v0(t) = ', v0 , ' V')

# + id="XmBYMUAAXbe8" outputId="857b82bb-8887-44fc-adba-750dcce27781"
# correntes nos indutores em função da tensão aplicada aos terminais
i1 = iL
i2 = (1/L2)*sp.integrate(v0, (t, 0, t)) + i2_0
i3 = (1/L3)*sp.integrate(v0, (t, 0, t)) + i3_0

print('Correntes nos indutores:')
print('i1(t) = ', i1/1e-3 , ' mA')
print('i2(t) = ', i2/1e-3 , ' mA')
print('i3(t) = ', i3/1e-3 , ' mA')

# + id="kolNrBnMXbe8" outputId="597b194c-95f8-4e38-e929-e2cdf3c9abfa"
# calculando os valores de energia em t=0
E1_0 = (1/2)*L1*(i1.evalf(subs={t:0}))**2
E2_0 = (1/2)*L2*(i2.evalf(subs={t:0}))**2
E3_0 = (1/2)*L3*(i3.evalf(subs={t:0}))**2

print('Energia inicial armazenada nos indutores:')
print('E1(0) = %.2f μJ' %(E1_0/1e-6))
print('E2(0) = %.2f μJ' %(E2_0/1e-6))
print('E3(0) = %.2f μJ' %(E3_0/1e-6))

# + id="S68PuPBCXbe9" outputId="eee56f24-ac11-436e-ccef-21769b1adef7"
# calculando os valores de energia em t =oo
E1_inf = (1/2)*L1*(i1.evalf(subs={t:100}))**2
E2_inf = (1/2)*L2*(i2.evalf(subs={t:100}))**2
E3_inf = (1/2)*L3*(i3.evalf(subs={t:100}))**2

print('Energia final armazenada nos indutores:')
print('E1(oo) = %.2f μJ' %(E1_inf/1e-6))
print('E2(oo) = %.2f μJ' %(E2_inf/1e-6))
print('E3(oo) = %.2f μJ' %(E3_inf/1e-6))

# + id="xnTSuCgXXbe9" outputId="8900fc8f-d8b1-479b-b934-c92f7d93adab"
# calculando a variação de energia nos indutores

ΔE = (E1_inf-E1_0) + (E2_inf-E2_0) + (E3_inf-E3_0)

print('Variação da energia armazenada nos indutores:')
print('ΔE = %.2f μJ' %(ΔE/1e-6))

# + id="8meRIv05Xbe9" outputId="3bf96849-8a2b-46c7-d3fa-119fc8bf3265"
# define tensão sobre o resistor vR(t)
vR = R*i1 

# potência consumida pelo resistor
p = vR*i1

# energia consumida pelo resistor
E = sp.integrate(p, (t, 0, sp.oo))
print('Energia consumida pelo resistor:')
print('E = %.2f μJ' %(E/1e-6))
