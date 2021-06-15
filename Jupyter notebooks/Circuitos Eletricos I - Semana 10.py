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

# # *Circuitos Elétricos I - Semana 10*

# ### Problema 1
#   
# (Problema 7.19 - Nilsson) Para o circuito abaixo, pede-se:
#
# <img src="./figures/J13C1.png" width="400">
#
# a) Determine a tensão $v_0(t)$ sobre o indutor de $48\;mH$ para $t\geq0$.\
# b) Determine a corrente $i_0(t)$ sobre o indutor de $48\;mH$ para $t\geq0$.\
# c) Determine a energia comsumida pelo resistor de $2.5\;k\Omega$ no intervalo $0\leq t \leq\infty$.
#
# Link para a simulação do circuito: https://tinyurl.com/yj69udn8

# +
# valores das indutâncias
L1 = 20e-3
L2 = 80e-3
L3 = 48e-3

# valores iniciais das correntes
i1_0 = 5e-3
i2_0 = 5e-3
i3_0 = 0

# +
# indutância equivalente
Leq1 = (L2*L3)/(L2+L3)
Leq  = L1 + Leq1

print('Leq = ', Leq/1e-3, ' mH')

# +
R = 2.5e3

# constante de tempo
τ = Leq/R

print('τ = ', τ, ' s')

# +
import sympy as sp

iL_inf = 0
iL_0   = i1_0

# define as variável tempo 
t = sp.symbols('t')

# define i(t)
iL = iL_inf + (iL_0 - iL_inf)*sp.exp(-t/τ)

print('Corrente no indutor equivalente:')
print('iL(t) = ', iL/1e-3 , ' mA')

# +
# calcula v0
v0 = Leq1*sp.diff(iL,t)

print('v0(t) = ', v0 , ' V')

# +
# correntes nos indutores em função da tensão aplicada aos terminais
i1 = iL
i2 = (1/L2)*sp.integrate(v0, (t, 0, t)) + i2_0
i3 = (1/L3)*sp.integrate(v0, (t, 0, t)) + i3_0

print('Correntes nos indutores:')
print('i1(t) = ', i1/1e-3 , ' mA')
print('i2(t) = ', i2/1e-3 , ' mA')
print('i3(t) = ', i3/1e-3 , ' mA')

# +
# calculando os valores de energia em t=0
E1_0 = (1/2)*L1*(i1.evalf(subs={t:0}))**2
E2_0 = (1/2)*L2*(i2.evalf(subs={t:0}))**2
E3_0 = (1/2)*L3*(i3.evalf(subs={t:0}))**2

print('Energia inicial armazenada nos indutores:')
print('E1(0) = %.2f μJ' %(E1_0/1e-6))
print('E2(0) = %.2f μJ' %(E2_0/1e-6))
print('E3(0) = %.2f μJ' %(E3_0/1e-6))

# +
# calculando os valores de energia em t =oo
E1_inf = (1/2)*L1*(i1.evalf(subs={t:100}))**2
E2_inf = (1/2)*L2*(i2.evalf(subs={t:100}))**2
E3_inf = (1/2)*L3*(i3.evalf(subs={t:100}))**2

print('Energia final armazenada nos indutores:')
print('E1(oo) = %.2f μJ' %(E1_inf/1e-6))
print('E2(oo) = %.2f μJ' %(E2_inf/1e-6))
print('E3(oo) = %.2f μJ' %(E3_inf/1e-6))

# +
# calculando a variação de energia nos indutores

ΔE = (E1_inf-E1_0) + (E2_inf-E2_0) + (E3_inf-E3_0)

print('Variação da energia armazenada nos indutores:')
print('ΔE = %.2f μJ' %(ΔE/1e-6))

# +
# define tensão sobre o resistor vR(t)
vR = R*i1 

# potência comsumida pelo resistor
p = vR*i1

# energia comsumida pelo resistor
E = sp.integrate(p, (t, 0, sp.oo))
print('Energia consumida pelo resistor:')
print('E = %.2f μJ' %(E/1e-6))
