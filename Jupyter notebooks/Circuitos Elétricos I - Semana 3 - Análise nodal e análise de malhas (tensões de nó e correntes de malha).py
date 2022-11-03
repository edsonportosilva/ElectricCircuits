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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%203%20-%20An%C3%A1lise%20nodal%20e%20an%C3%A1lise%20de%20malhas%20(tens%C3%B5es%20de%20n%C3%B3%20e%20correntes%20de%20malha).ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="EUGlOHljRuEv" outputId="15499b6e-97bd-4b49-84ff-98ef48471424"
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

if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')

# + [markdown] id="NCN78FeZRuE3"
# # *Circuitos Elétricos I - Semana 3*

# + [markdown] id="N4R7G-U0RuE5"
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
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J4C1.png?raw=1" width="500">

# + [markdown] id="jLxc-NiARuE6"
# ### Solução das equações

# + id="CfOI7gfQRuE7"
from utils import symdisp
import sympy as sp

# + id="75b-vmokRuE7" outputId="b7d0961f-c575-476a-e8bb-cd8a9bbcfa05"
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

# + [markdown] id="_ZOLCzZARuE8"
# ### Cálculo das correntes

# + id="Etz8sTSfRuE9"
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

# + [markdown] id="rhCCkb0VRuE9"
# ### Cálculo das potências

# + id="TJ9wWRKURuE9"
pR = 
p10V = 
p05A = 
p12V = 
p2ix = 

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10V+p05A+p12V+p2ix))

# + [markdown] id="vJ9Ya0saRuE-"
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
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J4C2.png?raw=1" width="500">

# + [markdown] id="FJ2auVYVRuE_"
# ### Solução das equações

# + id="YNvXOEL_RuE_" outputId="3bc928d0-d60a-4ce3-8b6d-8b8b72677ac3"
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

# + [markdown] id="7wKdN2LNRuE_"
# ### Cálculo das correntes

# + id="L5-tBYmURuFA"
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

# + [markdown] id="8A4ncDbDRuFA"
# ### Cálculo das potências

# + id="y-6wu7-SRuFA"
pR = 
p10V = 
p05A = 
p12V = 
p2ix =

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10V+p05A+p12V+p2ix))
