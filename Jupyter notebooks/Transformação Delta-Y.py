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

import sympy as sp
import numpy as np
from utils import symdisp, symplot
from IPython.display import Math, Latex, display

# # *Transformação Delta -Y*
#

# + [markdown] toc=true
# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Definindo-expressões-matemáticas" data-toc-modified-id="Definindo-expressões-matemáticas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Definindo expressões matemáticas</a></span></li><li><span><a href="#Transformação-Y-$\Delta$" data-toc-modified-id="Transformação-Y-$\Delta$-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Transformação Y-$\Delta$</a></span></li><li><span><a href="#Transformação-$\Delta$-Y" data-toc-modified-id="Transformação-$\Delta$-Y-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Transformação $\Delta$-Y</a></span></li></ul></div>
# -

# ## Definindo expressões matemáticas
#
# <img src="./figures/J16C1.png" width="500">
#
#
# Primeiramente definimos as variáveis indicando os valores das resistências da configuração $Y$ ($R_1$, $R_2$, $R_3$) e os valores da configuração $\Delta$ ($R_a$, $R_b$, $R_c$).

# definindo as variáveis:
R1, R2, R3 = sp.symbols('R_1, R_2, R_3', real=True, positive=True)
Ra, Rb, Rc = sp.symbols('R_a, R_b, R_c', real=True, positive=True)

# Para que as duas configurações sejam completamente equivalentes, a resistência medida em quaisquer dois pares de terminais deve ser a mesma na configuração $Y$ ou na configuração $\Delta$. Logo, analisando as relações de resistência equivalente para os três nós do circuito, temos que as seguintes equações devem ser válidas para que haja equivalência entre a configuração $Y$ e a configuração $\Delta$:

# +
# define os sistema de equações
eq1 = sp.Eq( R1 + R2, Rc * ( Ra + Rb ) / ( Ra + Rb + Rc ) )             
eq2 = sp.Eq( R2 + R3, Ra * ( Rb + Rc ) / ( Ra + Rb + Rc ) )    
eq3 = sp.Eq( R3 + R1, Rb * ( Ra + Rc ) / ( Ra + Rb + Rc ) )    

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 
# -

# ## Transformação Y-$\Delta$
#
# Resolvendo o sistema de equações lineares para obter $R_a$, $R_b$, $R_c$ em função de $R_1$, $R_2$, $R_3$.

# +
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
# -

# ## Transformação $\Delta$-Y
#
# Resolvendo o sistema de equações lineares para obter $R_1$, $R_2$, $R_3$ em função de $R_a$, $R_b$, $R_c$.

# +
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
