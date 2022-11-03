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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%206.2%20-%20Armazenamento%20de%20energia.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="V0TybBSFVso4" outputId="8c20c740-7d66-4081-ca26-db62d9bed6d2"
from IPython.core.display import HTML
from IPython.display import Image

if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')

import numpy as np
import sympy as sp
from sympy import oo
from utils import symplot, symdisp, round_expr

HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# + [markdown] id="kSCA8lFBVso7"
# # *Circuitos Elétricos I - Semana 6*

# + [markdown] id="pkWoIwntVso8"
# ## Elementos armazenadores de energia
#
# Comparação entre capacitores convencionais, supercapacitores e baterias de lítio. A tabela abaixo mostra as especificações  necessários para cada dispositivo armazenar ∼1 megajoule (MJ) de energia (300 watts-hora). 1 MJ de energia irá alimentar um laptop com um consumo médio de 50 W por 6 horas. Observe na primeira coluna que uma bateria de íon de lítio pode conter 1000 vezes mais energia do que um capacitor convencional.
#
# $$
# \begin{array}{|c|c|c|c|c|c|}
# \hline \text { Dispositivo } & \begin{array}{c}
# \text { Energia } \\
# \text { específica } \\
# \text { [Wh/kg]} \\
# \end{array} & \begin{array}{c}
# \text { Energia } \\
# \text { específica } \\
# \text { [MJ/kg] }
# \end{array} & \begin{array}{c}
# \text { Densidade de} \\
# \text { Energia } \\
# \text { [MJ / L] }
# \end{array} & \begin{array}{c}
# \text { Volume } \\
# \text { requerido para } \\
# \text { armazenar 1 MJ } \\
# \text { [L] }
# \end{array} & \begin{array}{c}
# \text { Peso } \\
# \text { requerido para } \\
# \text { armazenar 1 MJ } \\
# \text { [kg] }
# \end{array} \\
# \hline \begin{array}{c}
# \text { Capacitor convencional} \\
# \end{array} & 0.01-0.1 & 4 \times 10^{-5}-4 \times 10^{-4} & 6 \times 10^{-5}-6 \times 10^{-4} & 17000-1700 & 25000-2500 \\
# \text { Supercapacitor } & 1-10 & 0.004-0.04 & 0.006-0.06 & 166-16 & 250-25 \\
# \text { Bateria de Íons de Lítio } & 100-250 & 0.36-0.9 & 1-2 & 1-0.5 & 2.8-1.1 \\
# \hline
# \end{array}
# $$
#
# Fonte: Fawwaz Ulaby, Michel M. Maharbiz and Cynthia M. Furse, $\textit{ Circuit Analysis and Design}$, Michigan Publishing Services, 2018
#
#
# ## Resumo dos elementos passivos ideais de dois terminais
#
# $$
# \begin{array}{|l|c|c|c|}
# \hline \text { Propriedade } & R & L & C \\
# \hline \text { Relação } i-v  & i=\frac{v}{R} & i=\frac{1}{L} \int_{t_{0}}^{t} v(\tau) d \tau+i\left(t_{0}\right) & i=C \frac{d v}{d t} \\
# \text { Relação } v-i & v=Ri & v=L \frac{d i}{d t} & v=\frac{1}{C} \int_{t_{0}}^{t} i(\tau) d \tau+v\left(t_{0}\right) \\
# p \text { (potência }) & p=Ri^{2} & p=L i \frac{d i}{d t} & p=C v \frac{d v}{d t} \\
# w \text { (energia armazenada) } & 0 & w=\frac{1}{2} L i^{2} & w=\frac{1}{2} C v^{2} \\
# \text { Associação em série } & R_{\mathrm{eq}}=R_{1}+R_{2} & L_{\mathrm{eq}}=L_{1}+L_{2} & \frac{1}{C_{\mathrm{eq}}}=\frac{1}{C_{1}}+\frac{1}{C_{2}} \\
# \text { Associação em paralelo } & \frac{1}{R_{\mathrm{eq}}}=\frac{1}{R_{1}}+\frac{1}{R_{2}} & \frac{1}{L_{\mathrm{eq}}}=\frac{1}{R_{1}}+\frac{1}{R_{2}} & C_{\mathrm{eq}}=C_{1}+C_{2} \\
# \text { Comportamento em regime estacionário } & \text { sem mudanças } & \text { curto-circuito } & \text { circuito aberto } \\
# \text { Pode } v \text { variar instantaneamente? } & \text { sim } & \text { sim } & \text { não } \\
# \text { Pode } i \text { variar instantaneamente? } & \text { sim } & \text { não } & \text { sim }\\ \hline
# \end{array}
# $$

# + [markdown] id="zphv7eY7Vso9"
# ### Problema 1
#   
# Para o circuito abaixo, determine $v_{C1}$, $v_{C2}$ e $i_{L}$ assumindo que o circuito encontra-se em regime estacionário.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J9C1.png?raw=1" width="600">

# + [markdown] id="raSjAxVcVso-"
# ### Problema 2
#   
# No circuito abaixo, sabe-se que $i_0(t)= 50e^{-8000t}[\cos(6000t)+2\mathrm{sen}(6000t)]$ mA, para $t\geq 0^+$. Determine $v_{C}(0^+)$, $v_{L}(0^+)$ e $v_{R}(0^+)$.
#
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J9C2.png?raw=1" width="600">

# + id="pHY9ieYPVso-" outputId="d48b1d62-5be0-477e-b2bc-a21c7b132cb6"
# define variável tempo 
t = sp.symbols('t', real=True)

# expressão para a corrente no circuito
i0 = 50*sp.exp(-8000*t)*(sp.cos(6000*t)+2*sp.sin(6000*t))*1e-3

# plota gráfico da corrente
tmax = 1e-3
intervalo  = np.linspace(0, tmax, num = 1000)
symplot(t, i0, intervalo, funLabel='$i_0(t)$')

# + id="ghmDGHJMVso_"
# valores dos parâmetros do circuito
R = 320
L = 20e-3
C = 0.5e-6

# + id="ulZfzRFWVso_" outputId="131424e4-776d-4fea-b576-ab858b33f81a"
# calcula tensão no indutor
vL = L*sp.diff(i0, t)
vL = sp.simplify(vL)

print('Tensão no indutor:')
symdisp('v_L(t) = ', vL, 'V')

# + id="CBTmQEaMVspA" outputId="41959fed-a8cd-4245-e527-5049fffe850b"
symdisp('v_L(0^+) = ', vL.evalf(subs={t:0}), 'V')

# + id="grQEH9t3VspA" outputId="f8277c6c-6c58-4767-bd19-840c997fdee2"
# calcula tensão no resistor
vR = R*i0
vR = sp.simplify(vR)

print('Tensão no resistor:')
symdisp('v_R(t) = ', vR, 'V')

# + id="_nnVZ53OVspB" outputId="5634bfb7-dd0a-4edb-ee2c-7157c11ab03a"
symdisp('v_R(0^+) = ', vR.evalf(subs={t:0}), 'V')

# + id="Y2JBVNXpVspB" outputId="3bce8a6d-944e-405e-c8f4-91c3a3907fd6"
# calcula tensão no capacitor (LKT)
vC = vR + vL
vC = sp.simplify(vC)

print('Tensão no capacitor:')
symdisp('v_C(t) = ', vC, 'V')

# + id="SDkH_uCJVspC" outputId="d6d49626-0081-4475-b343-e4ae90a4f4b4"
symdisp('v_C(0^+) = ', vC.evalf(subs={t:0}), 'V')

# + id="TSTrhSSoVspC" outputId="c0e54e5a-f671-4cd7-a0cf-aed5f53d15f9"
# checagem de vC(t) via integração de i0

vC = -(1/C)*sp.integrate(i0, (t, 0, t)) + 20
vC = sp.simplify(vC)

symdisp('v_C(t) = ', vC, 'V')

# + id="tvYylxPdVspC" outputId="2f219a67-2017-453e-91f5-c8e39a3500b6"
symplot(t, [vC, vR, vL], intervalo, funLabel=['$v_C(t)$ ','$v_R(t)$','$v_L(t)$'])
