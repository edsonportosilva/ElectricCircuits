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

# + id="O1lt6sYYCmTJ"
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


# + [markdown] id="shtPIZVVCmTM"
# # *Circuitos Elétricos I*

# + [markdown] id="Mj2FFoAECmTN"
# ## Semana 1 - Convenções para aplicação das Leis de Kirchhoff na análise de circuitos
#
#
#
# ### Caso 1

# + id="VhzNUPc_CmTO" outputId="d7b4f321-d39d-4f47-caa8-d6dc67ad1972" colab={"base_uri": "https://localhost:8080/", "height": 228}
Image("./figures/J1C1.png", width=500)

# + [markdown] id="qvVFL19qCmTO"
# #### Lei de Kirchhoff das tensões (LKT) 
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
# #### Lei de Kirchhoff das correntes (LKC)
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
# #### Lei de Ohm (+convenção passiva)
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
# ### Solução das equações

# + id="rElDlGS1CmTR"
import sympy as sp
import numpy as np

# + id="KWO5-o2oCmTR"
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
i3 = -0.5

print('Solução do sistema:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n v4 = %.2f V.' %(i1, i2, i3, v4))

# + [markdown] id="2awvSU-WCmTS"
# #### Cálculo das potências

# + id="vscVpbhhCmTS"
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

print('Potências:\n\n p10V = %.2f W\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n' %(p10V, p1, p2, p3, p4))

# + id="UbNfxF_iCmTS"
# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(p10V+p1+p2+p3+p4))

# + [markdown] id="dGf532npCmTS"
# Simulação do circuito: https://tinyurl.com/yfbwd4vz

# + [markdown] id="LBCCr4w9CmTT"
# ### Caso 2

# + id="0e9Jy_b0CmTT"
Image("./figures/J1C2.png", width=500)

# + id="C_diAtOtCmTT"
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( )             
eq2 = sp.Eq( )  
eq3 = sp.Eq( )

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
i3 = 0.5

print('Solução do sistema:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n v4 = %.2f V.' %(i1, i2, i3, v4))

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

print('Potências:\n\n p10V = %.2f W\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n' %(p10V, p1, p2, p3, p4))

# + [markdown] id="ZQwR6ITFCmTT"
# ### Caso 3

# + id="UuV0DcDXCmTU"
Image("./figures/J1C3.png", width=500)

# + id="7rDK5wfdCmTU"
# define as N variáveis desconhecidas
i1, i2, v4 = sp.symbols('i1, i2, v4')

# define os sistema de N equações
eq1 = sp.Eq( )             
eq2 = sp.Eq( )  
eq3 = sp.Eq( )

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
v4 = np.array([sol[v4] for sol in soluc]) 
i3 = 0.5

print('Solução do sistema:\n\n i1 = %.2f A,\n i2 = %.2f A,\n i3 = %.2f A,\n v4 = %.2f V.' %(i1, i2, i3, v4))

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

print('Potências:\n\n p10V = %.2f W\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n' %(p10V, p1, p2, p3, p4))
