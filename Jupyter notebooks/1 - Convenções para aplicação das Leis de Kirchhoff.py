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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%201%20-%20Conven%C3%A7%C3%B5es%20para%20aplica%C3%A7%C3%A3o%20das%20Leis%20de%20Kirchhoff.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="O1lt6sYYCmTJ" outputId="5ad5be9c-8d7c-4992-8832-543efca882c6" colab={"base_uri": "https://localhost:8080/"}
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

if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install .


# + [markdown] id="shtPIZVVCmTM"
# # *Circuitos Elétricos I*

# + [markdown] id="Mj2FFoAECmTN"
# ## 1 - Convenções para aplicação das Leis de Kirchhoff na análise de circuitos
#
# Neste notebook faremos um exercício comparativo entre as diferentes convenções que utilizamos na aplicação das Leis de Kirchhoff na análise de circuitos lineares. 
#
# Em particular veremos que:
#
# * A escolha das referências para sentido da corrente e polaridade da tensão é arbitrária, ou seja, existem diversas escolhas possíveis. Uma vez escolhido o conjunto de referências para a análise de determinado circuito, o resultado das equações do circuito deve ser interpretado de acordo com as referências adotadas.
#
# * A convenção passiva deve sempre ser obedecida na escrita das equações do circuito.
#
# Primeiramente, vamos analisar o circuito ilustrado na figura a seguir considerando o conjunto de referências indicado no diagrama (Caso 1).

# + [markdown] id="Mj2FFoAECmTN"
# ### Caso 1
#
# <img src="./figures/J1C1.png" width="500">
#
# #### Encontrando as equações do circuito

# + [markdown] id="qvVFL19qCmTO"
# **Lei de Kirchhoff das tensões (LKT)**
#
# Em qualquer malha frechada do circuito $\sum_k v_k = 0$
#
# `Convenção arbitrária (1): ao percorrer a malha, escolha um sinal (+ ou -) para indicar aumentos de tensão e o sinal oposto para indicar quedas de tensão no somatório da LKT.`
#
# Logo, atribuindo o sinal (-) para aumentos de tensão e o sinal (+) para quedas de tensão, ao aplicar a LKT no circuito mostrado acima, temos:
#
# $$ 
# \begin{align}
# -10 + v_1 + v_2 &= 0\\
# -v_2 + v_3 + v_4 &= 0
# \end{align}
# $$

# + [markdown] id="T3sRg4keCmTP"
# **Lei de Kirchhoff das correntes (LKC)**
#
# Em qualquer nó do circuito $\sum_k i_k = 0$
#
# `Convenção arbitrária (2): para o nó em questão, escolha um sinal (+ ou -) para indicar correntes chegando ao nó e o sinal oposto para indicar correntes deixando o nó no somatório da LKT.`
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

# + [markdown] id="Vq1WhDihCmTP"
# **Lei de Ohm (+convenção passiva)**
#
# `Convenção passiva (3): qualquer expressão que relacione as grandezas de tensão e corrente num elemento ideal de dois terminais deve ser escrita de acordo com a convenção passiva.`
#
# A convenção passiva estabelece que:
#
# 1. Se o sentido de referência adotado para corrente coincide com a queda de tensão na polaridade de referência ($+ \rightarrow -$), *qualquer expressão envolvendo $v$ e $i$* para o elemento em questão deve ser escrita com **sinal positivo**.
#
#
# 2. Se o sentido de referência adotado para corrente coincide com o aumento de tensão na polaridade de referência ($+ \leftarrow -$), *qualquer expressão envolvendo $v$ e $i$* para o elemento em questão deve ser escrita com **sinal negativo**.
#
# A Lei de Ohm expressa a relação entre tensão, corrente e resistência num resistor ideal. Logo, as expressões da Lei de Ohm devem obedecer a convenção passiva. 
#
# Desse modo, podemos escrever as seguintes equações para o circuito acima. 
#
# $$ 
# \begin{align}
# v_1 &= 10i_1\\
# v_2 &= 50i_2\\
# v_3 &= 20i_3
# \end{align}
# $$

# + [markdown] id="vjPAI94iCmTQ"
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

# + [markdown] id="-sasV6DzCmTQ"
# #### Solucionando as equações do circuito

# + id="rElDlGS1CmTR"
import sympy as sp
import numpy as np
from circuit.utils import symdisp

# + id="KWO5-o2oCmTR" outputId="bb70f2db-9e36-4a49-c631-de8d7224839f" colab={"base_uri": "https://localhost:8080/", "height": 120}
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq(10*i1 + 50*i2, 10)             
eq2 = sp.Eq(-50*i2 + v4, 10)  
eq3 = sp.Eq(i1 -i2, -0.5)

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)[0]

i1 = soluc[i1]
i2 = soluc[i2]
v4 = soluc[v4] 
i3 = -0.5

print('Solução do sistema:')
symdisp('i_1 = ', round(i1,3), 'A')
symdisp('i_2 = ', round(i2,3), 'A')
symdisp('i_3 = ', round(i3,3), 'A')
symdisp('v_4 = ', round(v4,3), 'V')

# + [markdown] id="2awvSU-WCmTS"
# #### Cálculo das potências

# + id="vscVpbhhCmTS" outputId="5dc0f5ae-e5bb-4ce7-af45-bf76c9e474cc" colab={"base_uri": "https://localhost:8080/", "height": 141}
# expressões para a Lei de Ohm (convenção passiva)
# v1 = 
# v2 = 
# v3 = 

# expressões para as potências (convenção passiva)
p10V = -10*i1
p1   = 10*i1**2
p2   = 50*i2**2
p3   = 20*i3**2
p4   = v4*i3

print('Potências:')
symdisp('p_{10V} = ', round(p10V,3), 'W')
symdisp('p_1 = ', round(p1,3), 'W')
symdisp('p_2 = ', round(p2,3), 'W')
symdisp('p_3 = ', round(p3,3), 'W')
symdisp('p_4 = ', round(p4,3), 'W')

# + id="UbNfxF_iCmTS" outputId="8f9bb10a-96fa-478f-fbdd-187c00e15fb1" colab={"base_uri": "https://localhost:8080/", "height": 56}
# calcula somatório das potências
print('Somatório das potências :')
symdisp('\Sigma p = ', round(p10V+p1+p2+p3+p4,4), 'W')

# + [markdown] id="dGf532npCmTS"
# Cheque os resultados com a simulação do circuito no Falstad: https://tinyurl.com/yfbwd4vz

# + [markdown] id="LBCCr4w9CmTT"
# ### Caso 2
#
# Agora vamos resolver o mesmo circuito, porém adotando um conjunto de referências diferente, como ilustrado no digrama da figura a seguir. Resolva o circuito e compare os resultados com os obtidos na resolução do Caso 1.
#
# <img src="./figures/J1C2.png" width="500">

# + id="C_diAtOtCmTT"
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( )             
eq2 = sp.Eq( )  
eq3 = sp.Eq( )

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)[0]

i1 = soluc[i1]
i2 = soluc[i2]
v4 = soluc[v4] 
i3 = 0.5

print('Solução do sistema:')
symdisp('i_1 = ', round(i1,3), 'A')
symdisp('i_2 = ', round(i2,3), 'A')
symdisp('i_3 = ', round(i3,3), 'A')
symdisp('v_4 = ', round(v4,3), 'V')

# + id="HMW4WuAlCmTT"
# expressões para a Lei de Ohm (convenção passiva)
v1 = 
v2 = 
v3 = 

# expressões para as potências (convenção passiva)
p10V = 
p1   = 
p2   =  
p3   = 
p4   = 

print('Potências:')
symdisp('p_{10V} = ', round(p10V,3), 'W')
symdisp('p_1 = ', round(p1,3), 'W')
symdisp('p_2 = ', round(p2,3), 'W')
symdisp('p_3 = ', round(p3,3), 'W')
symdisp('p_4 = ', round(p4,3), 'W')

# + [markdown] id="ZQwR6ITFCmTT"
# ### Caso 3
#
# Vamos testar mais uma configuração de referências, como ilustrado no digrama da figura a seguir. Resolva o circuito e compare os resultados com os obtidos na resolução dos casos 1 e 2.
#
# <img src="./figures/J1C3.png" width="500">

# + id="7rDK5wfdCmTU"
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( )             
eq2 = sp.Eq( )  
eq3 = sp.Eq( )

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)[0]

i1 = soluc[i1]
i2 = soluc[i2]
v4 = soluc[v4] 
i3 = 0.5

print('Solução do sistema:')
symdisp('i_1 = ', round(i1,3), 'A')
symdisp('i_2 = ', round(i2,3), 'A')
symdisp('i_3 = ', round(i3,3), 'A')
symdisp('v_4 = ', round(v4,3), 'V')

# + id="nhtHWgOjCmTU"
# expressões para a Lei de Ohm (convenção passiva)
v1 = 
v2 = 
v3 = 

# expressões para as potências (convenção passiva)
p10V = 
p1   = 
p2   =  
p3   = 
p4   = 

print('Potências:')
symdisp('p_{10V} = ', round(p10V,3), 'W')
symdisp('p_1 = ', round(p1,3), 'W')
symdisp('p_2 = ', round(p2,3), 'W')
symdisp('p_3 = ', round(p3,3), 'W')
symdisp('p_4 = ', round(p4,3), 'W')
