# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 21:21:44 2020

@author: Edson Porto da Silva
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import signal

# Resolução numérica de um circuito RLC série alimentado por uma onda quadrada
# de tensão.

# parâmetros do circuito:
R  = 500              # resistência [ohms]
L  = 100e-3           # indutância  [henrys]
C  = 0.25e-6          # capacitância [farads]
V0 = 0                # tensão inicial no capacitor [volts]
I0 = 0                # corrente inicial no indutor [ampères]
fq = 80               # frequência da onda quadrada [hertz]
Vq = 15               # amplitude da onda quadrada [volts]
w0 = 1/np.sqrt(L*C)   # frequência angular de ressonância [rad/segundo]

t = np.linspace(0,100,10e4)*2/w0       # discretização do intervalo de tempo [segundos]

Vs = Vq*signal.square(2*np.pi*fq*t)    # onda quadrada na entrada do circuito

vC    = np.zeros(len(t))
x     = np.zeros(len(t))

# EDO da tensão sobre o capacitor: vc''(t)+(R/L)vc'(t)+vc(t)/LC = vs/LC

# Solução numérica:
vC[0] = V0       # condição incial de vc
x[0]  = I0/C     # condição inicial da derivada vc'(t)
#
# Integração numérica via método de Euler:
deltaT    = t[1]-t[0] # passo de integração
numPoints = len(t)-1

for kk in range(0, numPoints):
    vC[kk+1] = vC[kk]+x[kk]*deltaT                                # calcula vc(t+deltaT)
    x[kk+1]  = x[kk]+(-R/L*x[kk]-1/(L*C)*(vC[kk]-Vs[kk]))*deltaT  # calcula vc'(t+deltaT)

# cálculo das tensões e da corrente partir de vc(t):
i  = np.append(I0, C*np.diff(vC)/deltaT)    # corrente no circuito
vR = R*i                                    # tensão no resistor
vL = Vs-vR-vC                               # tensão no indutor(LKT)

plt.figure(1, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t, i)
plt.legend(['corrente i(t)']);
plt.grid(color='k', linestyle='--', linewidth=0.1)
plt.ylabel('ampères (A)', fontsize = 14)
plt.xlabel('tempo (s)', fontsize = 14)
plt.title('Corrente no circuito RLC série', fontsize = 14)

plt.figure(2, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t, vC)
plt.plot(t, vR)
plt.plot(t, vL)
plt.plot(t, Vs)
plt.legend(('Capacitor','Resistor','Indutor','Fonte'), prop={'size': 14});
plt.grid(color='k', linestyle='--', linewidth=0.1)
plt.ylabel('volts (V)', fontsize = 14)
plt.xlabel('tempo (s)', fontsize = 14)
plt.title('Tensões no circuito RLC série', fontsize = 14)

# cálculo das potências fornecidas e consumidas por cada elemento do circuito:
pL = np.multiply(vL,i)  # indutor
pC = np.multiply(vC,i)  # capacitor
pR = np.multiply(vR,i)  # resistor
pS = np.multiply(Vs,i)  # fonte de alimentação

plt.figure(3, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t, pC)
plt.plot(t, pR)
plt.plot(t, pL)
plt.plot(t, pS)
plt.legend(('Capacitor','Resistor','Indutor','Fonte'), prop={'size': 14});
plt.grid(color='k', linestyle='--', linewidth=0.1)
plt.ylabel('watts (W)', fontsize = 14)
plt.xlabel('tempo (s)', fontsize = 14)
plt.title('Potências no circuito RLC série', fontsize = 14)

# cálculo das energias fornecidas e consumidas no circuito:
energiaL     = integrate.cumtrapz(pL, t, initial = 0.5*L*i[0]**2)/1e-3  # energia total consumida pelo indutor em função do tempo em mJ
energiaC     = integrate.cumtrapz(pC, t, initial = 0.5*C*vC[0]**2)/1e-3  # energia total consumida pelo capacitor em função do tempo em mJ 
energiaR     = integrate.cumtrapz(pR, t, initial = 0)/1e-3  # energia total consumida pelo resistor em função do tempo em mJ
energiaFonte = integrate.cumtrapz(pS, t, initial = 0)/1e-3  # energia total fornecida pela fonte de corrente em função do tempo em mJ 

plt.figure(4, figsize=(12, 9), dpi=80, facecolor='w', edgecolor='k')
plt.plot(t, energiaC)
plt.plot(t, energiaR)
plt.plot(t, energiaL)
plt.plot(t, energiaFonte)
plt.legend(('Capacitor','Resistor','Indutor','Fonte'), prop={'size': 14});
plt.grid(color='k', linestyle='--', linewidth=0.1)
plt.ylabel('mili Joules (mJ)', fontsize = 14)
plt.xlabel('tempo (s)', fontsize = 14)
plt.title('Energia consumida ou fornecida por cada elemento até o instante t', fontsize = 14)







