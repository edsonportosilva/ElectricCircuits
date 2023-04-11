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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Princípio%20da%20superposição.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="FQT9KaLMXye6"
# # Princípio da superposição
#  

# + id="Gys5dAF0XyfN" outputId="9021f914-9c84-4459-cf39-9295c6be6f36" colab={"base_uri": "https://localhost:8080/"}
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install .

import sympy as sp
import numpy as np
from circuit.utils import symdisp, symplot
from IPython.display import Math, Latex, display

# + [markdown] id="A84zfdRBXyfT"
# #### Equações das correntes de malha

# + id="HjKwx-rPXyfU" outputId="77c17164-ec51-43ed-cbd1-b660fcf714de" colab={"base_uri": "https://localhost:8080/", "height": 197}
# define os parâmetros do circuito
R1, R2, R3, R4, R5 = sp.symbols('R_1, R_2, R_3, R_4, R_5', real=True, positive=True)

V1, V2 = sp.symbols('V_1, V_2', real=True, positive=True)

# define as N variáveis desconhecidas
ia, ib, ic = sp.symbols('i_a, i_b, i_c', real=True)

# define os sistema de N equações
eq1 = sp.Eq(-V1 + R1*ia + R2*(ia-ib), 0)             
eq2 = sp.Eq(-R2*(ia - ib) + R3*ib + R4*(ib-ic), 0)  
eq3 = sp.Eq(-R4*(ib - ic)+ R5*ic + V2, 0)  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

print('Simplificando:')
display(eq1.expand(), eq2.expand(), eq3.expand()) 

# # resolve o sistema
# soluc = sp.solve((eq1, eq2, eq3),(ia, ib, ic), dict=True)[0]

# ia = soluc[ia]
# ib = soluc[ib]
# ic = soluc[ic]

# print('\nSolução:')
# symdisp('i_a =', ia, 'A')
# symdisp('i_b =', ib, 'A')
# symdisp('i_c =', ic, 'A')
# -

# ### Rescrevendo o sistema na forma matricial $Ai = v$

# +
A = sp.Matrix([[R1+R2, -R2,      0],
               [-R2, R2+R3+R4, -R4], 
               [0,    -R4,   R4+R5]])

symdisp('A = ', A)

# +
v = sp.Matrix([[V1],
               [0],
               [-V2]])

symdisp('v = ', v)
# -

symdisp('A^{-1} = ', A.inv())

# +
A_ = A.subs({R1:1, R2:1, R3:1, R4:1, R5:1})

symdisp('A = ', A_)
symdisp('A^{-1} = ', A_.inv())
# -

v_ = v.subs({V1:10, V2:20})
symdisp('v = ', v_)

i = A_.inv() * v_
symdisp('\\begin{bmatrix} i_a \\\ i_b \\\ i_c \\end{bmatrix} = A^{-1}v = ', sp.N(i))

# **Fazendo $V_2$ = 0**

# +
symdisp('v = ', v)
v1 = v.subs({V1:10, V2:0})
symdisp('v_1 = ', v1)


i = A_.inv() * v1
symdisp('\\begin{bmatrix} i_a \\\ i_b \\\ i_c \\end{bmatrix} = A^{-1}v_1 = ', sp.N(i))
# -

# **Fazendo $V_1$ = 0**

# +
symdisp('v = ', v)

v2 = v.subs({V1:0, V2:20}) # v1 = 0 V, v2 = 20 V
symdisp('v_2 = ', v2)

i = A_.inv() * v2
symdisp('\\begin{bmatrix} i_a \\\ i_b \\\ i_c \\end{bmatrix} = A^{-1}v_2 = ', sp.N(i))

# +
i = A_.inv() * (v1 + v2)

symdisp('\\begin{bmatrix} i_a \\\ i_b \\\ i_c \\end{bmatrix} = A^{-1}(v_1+v_2) = ', sp.N(i))
