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

# + id="Hc7c6bqNSg6U"
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')

import sympy as sp
import numpy as np
from utils import symdisp
from IPython.display import display

# + [markdown] id="vT4m4fzASg6X"
# # *Transformações Y - $\Delta$ e $\Delta$ - Y*
#

# + [markdown] toc=true id="MEYI9j6-Sg6Z"
# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Definindo-expressões-matemáticas" data-toc-modified-id="Definindo-expressões-matemáticas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Definindo expressões matemáticas</a></span></li><li><span><a href="#Transformação-Y-$\Delta$" data-toc-modified-id="Transformação-Y-$\Delta$-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Transformação Y-$\Delta$</a></span></li><li><span><a href="#Transformação-$\Delta$-Y" data-toc-modified-id="Transformação-$\Delta$-Y-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Transformação $\Delta$-Y</a></span></li></ul></div>

# + [markdown] id="PhSBDdQ_Sg6Z"
# ## Definindo expressões matemáticas
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

# + id="NkTtsJ8ISg6a" outputId="8a44c692-0bc4-47fc-bb8d-deb65656b5f9"
# define o sistema de equações
eq1 = sp.Eq( R1 + R2, Rc * ( Ra + Rb ) / ( Ra + Rb + Rc ) ) # para os terminais a e b             
eq2 = sp.Eq( R2 + R3, Ra * ( Rb + Rc ) / ( Ra + Rb + Rc ) ) # para os terminais b e c  
eq3 = sp.Eq( R3 + R1, Rb * ( Ra + Rc ) / ( Ra + Rb + Rc ) ) # para os terminais c e a  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

# + [markdown] id="Vtje9CBnSg6b"
# ## Transformação Y-$\Delta$
#
# Resolvendo o sistema de equações lineares para obter $R_a$, $R_b$, $R_c$ em função de $R_1$, $R_2$, $R_3$.

# + id="H4W4akTcSg6c" outputId="4e6fa211-cc8a-4492-f979-51e4976c68a4"
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
# ## Transformação $\Delta$-Y
#
# Resolvendo o sistema de equações lineares para obter $R_1$, $R_2$, $R_3$ em função de $R_a$, $R_b$, $R_c$.

# + id="QfV3clhRSg6d" outputId="4884c547-1dbc-41f4-a406-3adff88927f6"
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


# + id="1IqtFq7wSg6e" outputId="8954fde0-d637-4c83-e962-6f61abb8cda3"
YΔ(4, 2, 4)

# + id="BlgUcJXPSg6e" outputId="7797dbf6-8f19-4708-9006-d34933ed28e9"
YΔ(1, 3, 6)

# + id="HaGnGB4ESg6e" outputId="4273c28b-8f3c-4bfa-ad65-1010d34ebf2f"
ΔY(16, 8, 8)
