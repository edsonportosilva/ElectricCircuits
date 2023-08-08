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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Transforma%C3%A7%C3%B5es%20Delta-Y%20e%20Y-Delta.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="Hc7c6bqNSg6U" outputId="7fd489b9-b2f5-4e99-9613-8be45ee45a2f" colab={"base_uri": "https://localhost:8080/"}
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install .

import sympy as sp
import numpy as np
from circuit.utils import symdisp
from IPython.display import display

# + [markdown] id="vT4m4fzASg6X"
# # *Transformações Y - $\Delta$ e $\Delta$ - Y*
#

# + [markdown] id="MEYI9j6-Sg6Z" toc=true
# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Transformações--Y-$\Delta$-e-$\Delta$-Y" data-toc-modified-id="Transformações--Y-$\Delta$-e-$\Delta$-Y-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Transformações  Y-$\Delta$ e $\Delta$-Y</a></span></li><li><span><a href="#Obtendo-as-expressões-matemáticas-para-as-conversões-$\Delta$-Y-e-Y-$\Delta$" data-toc-modified-id="Obtendo-as-expressões-matemáticas-para-as-conversões-$\Delta$-Y-e-Y-$\Delta$-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Obtendo as expressões matemáticas para as conversões $\Delta$-Y e Y-$\Delta$</a></span><ul class="toc-item"><li><span><a href="#Transformação-Y-$\Delta$" data-toc-modified-id="Transformação-Y-$\Delta$-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Transformação Y-$\Delta$</a></span></li><li><span><a href="#Transformação-$\Delta$-Y" data-toc-modified-id="Transformação-$\Delta$-Y-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Transformação $\Delta$-Y</a></span></li></ul></li></ul></div>
# -

# ## Transformações  Y-$\Delta$ e $\Delta$-Y
#
# Transformações Y-$\Delta$ e $\Delta$-Y são técnicas utilizadas na análise de circuitos elétricos para substituir configurações de resistência Y por configurações ∆ equivalentes, e vice-versa. Tais substituições são mais comumente aplicadas em circuitos trifásicos para simplificar a análise dos mesmos. Estas transformações envolvem a manipulação das relações entre as resistências dos elementos do circuito nas diferentes configurações.
#
# Na conversão Y-$\Delta$:
#
# 1. Identificam-se as resistências de cada componente na configuração em $Y$.
# 2. Utilizam-se as respectivas expressões para calcular cada uma das resistências da configuração em $\Delta$ equivalente.
#
# Na conversão $\Delta$-Y:
#
# 1. Identificam-se as resistências de cada ramo do circuito na configuração em $\Delta$.
# 2. Utilizam-se as respectivas expressões para calcular cada uma das resistências da configuração em $Y$ equivalente.

# + [markdown] id="PhSBDdQ_Sg6Z"
# ## Obtendo as expressões matemáticas para as conversões $\Delta$-Y e Y-$\Delta$
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J16C1.png?raw=1" width="500">
#
#
# Primeiramente definimos as variáveis indicando os valores das resistências da configuração $Y$ ($R_1$, $R_2$, $R_3$) e os valores da configuração $\Delta$ ($R_a$, $R_b$, $R_c$).

# + id="Alp2CSP5Sg6a"
# definindo as variáveis:
R1, R2, R3 = sp.symbols('R_1, R_2, R_3', real=True, positive=True) # resistências da configuração Y
Ra, Rb, Rc = sp.symbols('R_a, R_b, R_c', real=True, positive=True) # resistências da configuração Δ

# + [markdown] id="NVrYaeUwSg6a"
# Para que as duas configurações sejam completamente equivalentes, a resistência medida em quaisquer dois pares de terminais deve ser a mesma na configuração $Y$ ou na configuração $\Delta$. Logo, analisando as relações de resistência equivalente para os três nós do circuito, temos que as seguintes equações devem ser válidas para que haja equivalência entre a configuração $Y$ e a configuração $\Delta$:

# + id="NkTtsJ8ISg6a" outputId="5fb28d80-f79a-40dc-fe10-188955770555" colab={"base_uri": "https://localhost:8080/", "height": 149}
# define o sistema de equações
eq1 = sp.Eq( R1 + R2, Rc * ( Ra + Rb ) / ( Ra + Rb + Rc ) ) # para os terminais a e b             
eq2 = sp.Eq( R2 + R3, Ra * ( Rb + Rc ) / ( Ra + Rb + Rc ) ) # para os terminais b e c  
eq3 = sp.Eq( R3 + R1, Rb * ( Ra + Rc ) / ( Ra + Rb + Rc ) ) # para os terminais c e a  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

# + [markdown] id="Vtje9CBnSg6b"
# ### Transformação Y-$\Delta$
#
# Resolvendo o sistema de equações lineares para obter $R_a$, $R_b$, $R_c$ em função de $R_1$, $R_2$, $R_3$.

# + id="H4W4akTcSg6c" outputId="2734a0cf-ead4-444d-d9a1-b4cc6a22c435" colab={"base_uri": "https://localhost:8080/", "height": 146}
# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), (Ra, Rb, Rc), dict=True)
soluc = soluc[0]

Ra = soluc[Ra]
Rb = soluc[Rb]
Rc = soluc[Rc]

print('Solução do sistema:')
symdisp('R_a =', Ra.cancel())
symdisp('R_b =', Rb.cancel())
symdisp('R_c =', Rc.cancel())

# + [markdown] id="uKpKsAv_Sg6d"
# ### Transformação $\Delta$-Y
#
# Resolvendo o sistema de equações lineares para obter $R_1$, $R_2$, $R_3$ em função de $R_a$, $R_b$, $R_c$.

# + id="QfV3clhRSg6d" outputId="e4115a9b-d6a0-4e97-9b0f-ef72faad5407" colab={"base_uri": "https://localhost:8080/", "height": 146}
# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), (R1, R2, R3), dict=True)
soluc = soluc[0]

R1 = soluc[R1]
R2 = soluc[R2]
R3 = soluc[R3]

print('Solução do sistema:')
symdisp('R_1 =', R1.cancel())
symdisp('R_2 =', R2.cancel())
symdisp('R_3 =', R3.cancel())


# + id="rq7i6xu3Sg6e"
def YΔ(R1, R2, R3):
    p = R1*R2 + R2*R3 + R3*R1
    
    Ra = p/R1
    Rb = p/R2
    Rc = p/R3
    
    return Ra, Rb, Rc

def ΔY(Ra, Rb, Rc):
    s = Ra + Rb + Rc
    
    R1 = Rb*Rc/s
    R2 = Ra*Rc/s
    R3 = Ra*Rb/s
    
    return R1, R2, R3


# + id="1IqtFq7wSg6e" outputId="7bf6e9c9-0a5a-42a0-8ed2-4a8ee2dedc59" colab={"base_uri": "https://localhost:8080/"}
YΔ(4, 2, 4)

# + id="BlgUcJXPSg6e" outputId="70634a5d-2c51-425a-fe6a-ace62c79e2fe" colab={"base_uri": "https://localhost:8080/"}
YΔ(1, 3, 6)

# + id="HaGnGB4ESg6e" outputId="dad7555a-81c3-4e53-b04e-f4dc0b1fe3b2" colab={"base_uri": "https://localhost:8080/"}
ΔY(16, 8, 8)
