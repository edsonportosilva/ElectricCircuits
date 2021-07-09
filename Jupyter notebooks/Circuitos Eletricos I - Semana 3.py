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

# + [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Resolução-de-circuitos-utilizando-análise-nodal:-método-das-tensões-de-nó." data-toc-modified-id="Resolução-de-circuitos-utilizando-análise-nodal:-método-das-tensões-de-nó.-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Resolução de circuitos utilizando análise nodal: método das tensões de nó.</a></span><ul class="toc-item"><li><span><a href="#Procedimento-de-solução:" data-toc-modified-id="Procedimento-de-solução:-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Procedimento de solução:</a></span></li><li><span><a href="#Problema-1" data-toc-modified-id="Problema-1-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Problema 1</a></span></li><li><span><a href="#Solução-das-equações" data-toc-modified-id="Solução-das-equações-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Solução das equações</a></span></li><li><span><a href="#Cálculo-das-correntes" data-toc-modified-id="Cálculo-das-correntes-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Cálculo das correntes</a></span></li><li><span><a href="#Cálculo-das-potências" data-toc-modified-id="Cálculo-das-potências-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Cálculo das potências</a></span></li></ul></li><li><span><a href="#Resolução-de-circuitos-utilizando-análise-de-malhas:-correntes-de-malha." data-toc-modified-id="Resolução-de-circuitos-utilizando-análise-de-malhas:-correntes-de-malha.-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Resolução de circuitos utilizando análise de malhas: correntes de malha.</a></span><ul class="toc-item"><li><span><a href="#Procedimento-de-solução:" data-toc-modified-id="Procedimento-de-solução:-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Procedimento de solução:</a></span></li><li><span><a href="#Problema-2" data-toc-modified-id="Problema-2-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Problema 2</a></span></li><li><span><a href="#Solução-das-equações" data-toc-modified-id="Solução-das-equações-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Solução das equações</a></span></li><li><span><a href="#Cálculo-das-correntes" data-toc-modified-id="Cálculo-das-correntes-2.4"><span class="toc-item-num">2.4&nbsp;&nbsp;</span>Cálculo das correntes</a></span></li><li><span><a href="#Cálculo-das-potências" data-toc-modified-id="Cálculo-das-potências-2.5"><span class="toc-item-num">2.5&nbsp;&nbsp;</span>Cálculo das potências</a></span></li></ul></li></ul></div>
# -

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

Image("./figures/J4C1.png", width=500)

# ### Solução das equações

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

va = np.array([sol[va] for sol in soluc])
vb = np.array([sol[vb] for sol in soluc]) 
vc = np.array([sol[vc] for sol in soluc]) 
vd = np.array([sol[vd] for sol in soluc]) 

print('Solução do sistema:\n\n va = %.2f V,\n vb = %.2f V,\n vc = %.2f V,\n vd = %.2f V.' %(va, vb, vc, vd))
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

print('Correntes:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n i4 = %.2f A,\n i5 = %.2f A,\n i6 = %.2f A,\n ix = %.2f A.'\
      %(i1, i2, i3, i4, i5, i6, ix))
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

Image("./figures/J4C2.png", width=500)

# ### Solução das equações

# +
# define as N variáveis desconhecidas
ia, ib, ic, id = sp.symbols('ia, ib, ic, id')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()
eq4 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)

ia = np.array([sol[ia] for sol in soluc])
ib = np.array([sol[ib] for sol in soluc]) 
ic = np.array([sol[ic] for sol in soluc]) 
id = np.array([sol[id] for sol in soluc]) 

print('Solução do sistema:\n\n ia = %.2f A,\n ib = %.2f A,\n ic = %.2f A,\n id = %.2f A.' %(ia, ib, ic, id))
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

print('Correntes:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n i4 = %.2f A,\n i5 = %.2f A,\n i6 = %.2f A,\n ix = %.2f A.'\
      %(i1, i2, i3, i4, i5, i6, ix))
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
