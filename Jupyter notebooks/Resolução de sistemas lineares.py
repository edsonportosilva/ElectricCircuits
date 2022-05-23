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

# # *Resolução de sistemas lineares*
#  

import sympy as sp
import numpy as np
from utils import symdisp, symplot
from IPython.display import Math, Latex, display

# ### Resolvendo um sistema de equações lineares com *sp.solve*

# +
# define as N variáveis desconhecidas
v1, v2 = sp.symbols('v_1, v_2')

# define os sistema de N equações
eq1 = sp.Eq(17*v1 - 5*v2, 100)             
eq2 = sp.Eq(5*v1 - 6*v2, -20)  
#eq3 = sp.Eq(5*x - 2*y + 3*z, 5)  

print('Sistema de equações lineares:')
display(eq1, eq2) 

# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
soluc = soluc[0]

v1 = soluc[v1]
v2 = soluc[v2]

print('Solução do sistema:')
symdisp('v_1 =', sp.N(v1,2), 'V')
symdisp('v_2 =', sp.N(v2,2), 'V')
#symdisp('z =', z)
