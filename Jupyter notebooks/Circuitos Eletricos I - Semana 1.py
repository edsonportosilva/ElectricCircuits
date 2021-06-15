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

# # *Circuitos Elétricos I*

# ## Semana 1 - Convenções para aplicação das Leis de Kirchhoff na análise de circuitos resistivos
#
# ### Caso 1

from IPython.display import Image
Image("./figures/J1C1.png", width=500)

# #### Lei de Kirchhoff das tensões (LKT) 
#
# Em qualquer malha frechada do circuito $\sum_k v_k = 0$
#
# `Convenção arbitrária: ao percorrer a malha, escolha um sinal (+ ou -) para indicar aumentos de tensão e o sinal oposto para indicar quedas de tensão no somatório da LKT.`
#
# $$ 
# \begin{align}
# -10 + v_1 + v_2 &= 0\\
# -v_2 + v_3 + v_4 &= 0
# \end{align}
# $$

# #### Lei de Kirchhoff das correntes (LKC)
#
# Em qualquer nó do circuito $\sum_k i_k = 0$
#
# `Convenção arbitrária: para o nó em questão, escolha um sinal (+ ou -) para indicar correntes chegando ao nó e o sinal oposto para indicar correntes deixando o nó no somatório da LKT.`
#
# ou, para evitar erros com troca de sinais, simplesmente faça
#
# `Somatório das correntes chegando ao nó igual ao somatório das correntes deixando o nó.`
#
# $$ 
# \begin{align}
# i_1 &= i_2 + i_3\\
# i_3 &= -0.5~A
# \end{align}
# $$

# #### Lei de Ohm (+convenção passiva):
#
# $$ 
# \begin{align}
# v_1 &= 10i_1\\
# v_2 &= 50i_2\\
# v_3 &= 20i_3
# \end{align}
# $$

# Logo:
#
# $$ 
# \begin{align}
# -10 + 10i_1 + 50i_2 &= 0\\
# -50i_2 -10 + v_4 &= 0\\
# i_1 - i_2 &= -0.5
# \end{align}
# $$
#
# Rearranjando as equações:
#
# $$ 
# \begin{align}
#  10i_1 + 50i_2 &= 10\\
# -50i_2 + v_4 &= 10\\
# i_1 - i_2 &= -0.5
# \end{align}
# $$

# ### Solução das equações

import sympy as sp
import numpy as np

# +
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( 10*i1 + 50*i2, 10)             
eq2 = sp.Eq(    i1 -    i2, -0.5)  
eq3 = sp.Eq(-50*i2 +    v4, 10)

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
i3 = -0.5

print('Solução do sistema:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n v4 = %.2f V.' %(i1, i2, i3, v4))
# -

# #### Cálculo das potências

# +
# expressões para a Lei de Ohm (convenção passiva)
v1 = 10*i1
v2 = 50*i2
v3 = 20*i3

# expressões para as potências (convenção passiva)
p10V = -10*i1
p1   =  v1*i1
p2   =  v2*i2
p3   =  v3*i3
p4   =  v4*i3

print('Potências:\n\n p10V = %.2f W\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n' %(p10V, p1, p2, p3, p4))
# -

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(p10V+p1+p2+p3+p4))

# ### Caso 2

Image("./figures/J1C2.png", width=500)

# +
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( 10*i1 - 50*i2, 10)             
eq2 = sp.Eq(    i1 +    i2, -0.5)  
eq3 = sp.Eq( 50*i2 +    v4, 10)

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
i3 = 0.5

print('Solução do sistema:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n v4 = %.2f V.' %(i1, i2, i3, v4))

# +
# expressões para a Lei de Ohm (convenção passiva)
v1 = 10*i1
v2 = -50*i2
v3 = -20*i3

# expressões para as potências (convenção passiva)
p10V = -10*i1
p1   =  v1*i1
p2   =  -v2*i2
p3   =  -v3*i3
p4   =  -v4*i3

print('Potências:\n\n p10V = %.2f W\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n' %(p10V, p1, p2, p3, p4))
# -

# ### Caso 3

Image("./figures/J1C3.png", width=500)


