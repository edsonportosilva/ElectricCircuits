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

# # *Resolução de sistemas lineares*
#  

import sympy as sp
import numpy as np
from utils import symdisp, symplot
from IPython.display import Math, Latex, display

# ### Resolvendo um sistema de equações lineares com *sp.solve*

# #### Sistema $2\times2$ de tensões desconhecidas

# +
# define as N variáveis desconhecidas
v1, v2 = sp.symbols('v_1, v_2')

# define os sistema de N equações
eq1 = sp.Eq(17*v1 - 5*v2, 100)             
eq2 = sp.Eq(5*v1 - 6*v2, -20)  

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
# -

# #### Sistema $2\times2$ de correntes desconhecidas

# +
# define as N variáveis desconhecidas
ia, ib = sp.symbols('i_a, i_b')

# define os sistema de N equações
eq1 = sp.Eq(200*ia - 50*ib, 0.5)             
eq2 = sp.Eq(50*ia + 6*ib, -0.25)  

print('Sistema de equações lineares:')
display(eq1, eq2) 

# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
soluc = soluc[0]

ia = soluc[ia]
ib = soluc[ib]

print('Solução do sistema:')
symdisp('i_a =', sp.N(ia,2), 'A')
symdisp('i_b =', sp.N(ib,2), 'A')
# -

# #### Sistema $3\times3$ de tensões desconhecidas

# +
# define as N variáveis desconhecidas
v1, v2, v3 = sp.symbols('v_1, v_2, v_3')

# define os sistema de N equações
eq1 = sp.Eq(17*v1 - 5*v2 - 2*v3, 100)             
eq2 = sp.Eq(5*v1 - 6*v2, -20)  
eq3 = sp.Eq(v1 + 6*v3, 2)  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)
soluc = soluc[0]

v1 = soluc[v1]
v2 = soluc[v2]
v3 = soluc[v3]

print('Solução do sistema:')
symdisp('v_1 =', sp.N(v1,2), 'V')
symdisp('v_2 =', sp.N(v2,2), 'V')
symdisp('v_3 =', sp.N(v3,2), 'V')
# -

# #### Sistema $3\times3$ de correntes desconhecidas

# +
# define as N variáveis desconhecidas
ia, ib, ic = sp.symbols('i_a, i_b, i_c')

# define os sistema de N equações
eq1 = sp.Eq(50*ia - 15*ib - 20*ic, 1)             
eq2 = sp.Eq(30*ia + 60*ib, -0.25)  
eq3 = sp.Eq(ia + 60*ib, 0.1)  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)
soluc = soluc[0]

ia = soluc[ia]
ib = soluc[ib]
ic = soluc[ic]

print('Solução do sistema:')
symdisp('i_a =', sp.N(ia,2), 'A')
symdisp('i_b =', sp.N(ib,2), 'A')
symdisp('i_c =', sp.N(ic,2), 'A')
