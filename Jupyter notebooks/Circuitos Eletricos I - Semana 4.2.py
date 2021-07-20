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

Image("./figures/J6C1.png", width=700)

import sympy as sp
import numpy as np

# +
# define as N variáveis desconhecidas
v1, v2, v3, v4 = sp.symbols('v1, v2, v3, v4')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

v1 = np.array([sol[v1] for sol in soluc])
v2 = np.array([sol[v2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
v3 = 2 

print('Solução do sistema:\n\n v1 = %.2f V,\n v2 = %.2f V,\n v3 = %.2f V,\n v4 = %.2f V.' %(v1, v2, v3, v4))
# -


