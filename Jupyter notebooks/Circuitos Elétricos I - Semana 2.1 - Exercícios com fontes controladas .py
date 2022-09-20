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

# # *Circuitos Elétricos I*

# ## Semana 2 - Exercícios
#
# ### Exercício 1: circuito com fonte controlada de corrente
#
# No circuito abaixo, dado que $\frac{V_0}{V_s}=9$, determine o valor de $A$.
#
# <img src="./figures/J2C1.png" width="700">

# ### Exercício 2: circuito com fonte controlada de tensão
#
# Determine o valor de todas as correntes no circuito abaixo.
#
# <img src="./figures/J2C2.png" width="500">

# ### Solução das equações

import sympy as sp
from utils import symdisp

# +
# define as N variáveis desconhecidas
i1, i2, i3, i4 = sp.symbols('i1, i2, i3, i4')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()
eq4 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)
soluc = soluc[0]

i1 = soluc[i1]
i2 = soluc[i2]
i3 = soluc[i3]
i4 = soluc[i4]
ix = 3

print('Solução do sistema:')
symdisp('i_1 = ', round(i1, 2), ' A')
symdisp('i_2 = ', round(i2, 2), ' A')
symdisp('i_3 = ', round(i3, 2), ' A')
symdisp('i_4 = ', round(i4, 2), ' A')
symdisp('i_x = ', round(ix, 2), ' A')
# -

# #### Cálculo das potências

# +
# expressões para as potências 
pR = 
p10v = 
p15v = 
p2ix = 

print('Potências:')
symdisp('p_R = ', round(pR, 2), ' W')
symdisp('p_{10V} = ', round(p10v, 2), ' W')
symdisp('p_{15V} = ', round(p15v, 2), ' W')
symdisp('p_{2i_x} = ', round(p2ix, 2), ' W')
# -

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10v+p15v+p2ix))
