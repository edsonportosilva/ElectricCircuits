# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

from IPython.core.display import HTML
from IPython.display import Image
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# # *Circuitos Elétricos I - Semana 4*

# ### Problema 1
#   
# Determine o circuito equivalente de Thévenin ($v_{th}$, $R_{th}$) do ponto de vista dos terminais $(a,b)$ do circuito abaixo.
#
# a) Determine a $v_{th}$ pelo método das tensões de nó.\
# b) Determine a corrente de curto-circuito $i_{cc}$ pelo método das tensões de nó.\
# c) Determine a $v_{th}$ via superposição.\
# d) Determine a $R_{th}$ via resistência equivalente.\
# e) Determine $v_{th}$, $R_{th}$ via transformação de fontes.
#
# <img src="./figures/J6C1.png" width="700">
#
# Simulação do circuito: https://tinyurl.com/y4kwdr8z

import sympy as sp
from utils import symdisp

# +
# define as N variáveis desconhecidas
v1, v2, v3, v4 = sp.symbols('v1, v2, v3, v4')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)
soluc = soluc[0]

v1 = soluc[v1]
v2 = soluc[v2]
v4 = soluc[v4]
v3 = 2

print('Solução do sistema:')
symdisp('v_1 = ', round(v1, 2), ' V')
symdisp('v_2 = ', round(v2, 2), ' V')
symdisp('v_3 = ', round(v3, 2), ' V')
symdisp('v_4 = ', round(v4, 2), ' V')
