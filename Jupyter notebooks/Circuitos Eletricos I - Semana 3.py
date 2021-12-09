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

# # *Circuitos Elétricos I - Semana 3*

# ## Resolução de circuitos utilizando análise nodal: método das tensões de nó.
#
#
# ### Procedimento de solução:
#
# **Passo 1**: identifique todos os $n_e$ nós essenciais do circuito, selecione um deles como um nó de referência (terra) e, em seguida, atribua uma tensão de nó para cada um dos $n_e - 1$ nós essenciais restantes.
#
# **Passo 2**: em cada um dos $n_e - 1$ nós essenciais, obtenha uma equação aplicando a lei de Kirchhoff das correntes (LKC), ou seja, uma equação indicando que a soma de todas as correntes saindo do nó é igual a soma das correntes deixando o nó.
#
# **Passo 3**: escreva as equações obtidas em função das tensões de nó.
#
# **Passo 4**: resolva o sistema de $n_e - 1$ equações independentes para determinar as tensões de nó desconhecidas.
#
# **Passo 5**: determine os valores das grandezas de interesse a partir das tensões de nó obtidas.
#
#
# ### Problema 1
#
# Aplicando o método das tensões de nó, determine todas as correntes e potências desenvolvidas por cada elemento no circuito a seguir:
#
# <img src="./figures/J4C1.png" width="500">

# ### Solução das equações

from utils import symdisp
import sympy as sp
import numpy as np

# +
# define as N variáveis desconhecidas
va, vb, vc, vd = sp.symbols('va, vb, vc, vd')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()
eq3 = sp.Eq()
eq4 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)
soluc = soluc[0]

va = soluc[va]
vb = soluc[vb]
vc = soluc[vc]
vd = soluc[vd]

print('Solução do sistema:')
symdisp('v_a = ', round(va, 2), ' V')
symdisp('v_b = ', round(vb, 2), ' V')
symdisp('v_c = ', round(vc, 2), ' V')
symdisp('v_d = ', round(vd, 2), ' V')
# -

# ### Cálculo das correntes

# +
i2 = 
ix = 
i3 = 
i4 = 
i6 = 
i1 = 
i5 = 

print('Correntes:')
symdisp('i_1 = ', round(i1, 2), ' A')
symdisp('i_2 = ', round(i2, 2), ' A')
symdisp('i_3 = ', round(i3, 2), ' A')
symdisp('i_4 = ', round(i4, 2), ' A')
symdisp('i_5 = ', round(i5, 2), ' A')
symdisp('i_6 = ', round(i6, 2), ' A')
symdisp('i_x = ', round(ix, 2), ' A')
# -

# ### Cálculo das potências

# +
pR = 
p10V = 
p05A = 
p12V = 
p2ix = 

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10V+p05A+p12V+p2ix))
# -

# ## Resolução de circuitos utilizando análise de malhas: correntes de malha.
#
#
# ### Procedimento de solução:
#
# **Passo 1**: identifique todas as malhas simples e atribua a cada uma delas uma corrente de malha desconhecida. A escolha sentido de referência para cada corrente de malha é arbitrário. Por conveniência, costuma-se definir utilizar o mesmo sentido para todas as correntes de malha.
#
# **Passo 2**: para cada uma das malhas simples do circuito, obtenha uma equação aplicando a lei de Kirchhoff das tensões (LKT).
#
# **Passo 3**: resolva o sistema de equações independentes resultantes para determinar as correntes de malha.
#
# **Passo 4**: determine os valores das grandezas de interesse a partir das correntes de malha obtidas.
#
# ### Problema 2
#
# Aplicando o método das correntes de malha, determine todas as correntes e potências desenvolvidas por cada elemento no circuito a seguir:
#
# <img src="./figures/J4C2.png" width="500">

# ### Solução das equações

# +
# define as N variáveis desconhecidas
Ia, Ib, Ic, Id = sp.symbols('ia, ib, ic, id')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()             
eq3 = sp.Eq()             
eq4 = sp.Eq()  

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)
soluc = soluc[0]

Ia = soluc[Ia]
Ib = soluc[Ib]
Ic = soluc[Ic]
Id = soluc[Id]

print('Correntes:')
symdisp('i_a = ', round(Ia, 2), ' A')
symdisp('i_b = ', round(Ib, 2), ' A')
symdisp('i_c = ', round(Ic, 2), ' A')
symdisp('i_d = ', round(Id, 2), ' A')
# -

# ### Cálculo das correntes

# +
i2 = 
ix = 
i3 = 
i4 = 
i6 = 
i1 = 
i5 = 

print('Correntes:')
symdisp('i_1 = ', round(i1, 2), ' A')
symdisp('i_2 = ', round(i2, 2), ' A')
symdisp('i_3 = ', round(i3, 2), ' A')
symdisp('i_4 = ', round(i4, 2), ' A')
symdisp('i_5 = ', round(i5, 2), ' A')
symdisp('i_6 = ', round(i6, 2), ' A')
symdisp('i_x = ', round(ix, 2), ' A')
# -

# ### Cálculo das potências

# +
pR = 
p10V = 
p05A = 
p12V = 
p2ix =

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10V+p05A+p12V+p2ix))
