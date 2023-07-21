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

# + [markdown] colab_type="text" id="view-in-github"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/2.1%20-%20Exercícios%20com%20fontes%20controladas%20.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="1h_y-WuzQppc"
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
    # ! pip install -e .

# + [markdown] id="ZSGbDF-6Qppg"
# # *Circuitos Elétricos I*

# + [markdown] id="MhDD8K5VQpph"
# ## Circuitos com fontes controladas
#
# Em circuitos elétricos, uma fonte controlada (ou fonte dependente) é uma fonte de tensão ou corrente cujo valor é determinado por uma outra grandeza (tensão ou corrente) associada a um segundo elemento do circuito. Em outras palavras, a saída da fonte controlada depende das condições ou parâmetros de um outro elemento, presente no mesmo circuito ou num circuito externo.
#
# Existem quatro tipos principais de fontes controladas:
#
# * Fonte de tensão controlada por tensão (VCVS - *Voltage-Controlled Voltage Source*): A tensão fornecida por essa fonte depende de uma tensão aplicada em outro elemento do circuito.
#
# * Fonte de tensão controlada por corrente (CCVS - *Current-Controlled Voltage Source*): A tensão fornecida por essa fonte é determinada por uma corrente que atravessa outro elemento do circuito.
#
# * Fonte de corrente controlada por tensão (VCCS - *Voltage-Controlled Current Source*): A corrente fornecida por essa fonte depende de uma tensão aplicada em outro elemento do circuito.
#
# * Fonte de corrente controlada por corrente (CCCS - *Current-Controlled Current Source*): A corrente fornecida por essa fonte é determinada por uma corrente que atravessa outro elemento do circuito.
#
# As fontes controladas são frequentemente usadas em análises de circuitos para modelar dispositivos e sistemas que respondem a sinais externos de forma dependente ou proporcional a certas grandezas do circuito.
#
# ### Exercício 1: circuito com fonte controlada de corrente
#
# No circuito abaixo, dado que $\frac{V_0}{V_s}=9$, determine o valor de $A$.
#
# <img src="./figures/J2C1.png?raw=1" width="700">

# + [markdown] id="6tr9snCkQpph"
# ### Exercício 2: circuito com fonte controlada de tensão
#
# Determine o valor de todas as correntes no circuito abaixo.
#
# <img src="./figures/J2C2.png?raw=1" width="500">

# + [markdown] id="cq4Vjf7hQppi"
# ### Solução das equações

# + id="TiSCR6n-Qppi"
import sympy as sp
from circuit.utils import symdisp

# + id="9oBpqWEoQppj"
# define as N variáveis desconhecidas
i1, i2, i3, i4 = sp.symbols('i1, i2, i3, i4')

# define os sistema de N equações
eq1 = sp.Eq()             
eq2 = sp.Eq()  
eq3 = sp.Eq()
eq4 = sp.Eq()

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)
soluc = soluc[0]

i1 = soluc[i1]
i2 = soluc[i2]
i3 = soluc[i3]
i4 = soluc[i4]
ix = 3

print('Solução do sistema:')
symdisp('i_1 = ', round(i1, 2), ' A')
symdisp('i_2 = ', round(i2, 2), ' A')
symdisp('i_3 = ', round(i3, 2), ' A')
symdisp('i_4 = ', round(i4, 2), ' A')
symdisp('i_x = ', round(ix, 2), ' A')

# + [markdown] id="_NUaDGsHQppk"
# #### Cálculo das potências

# + id="IpKh5-elQppk"
# expressões para as potências 
pR = 
p10v = 
p15v = 
p2ix = 

print('Potências:')
symdisp('p_R = ', round(pR, 2), ' W')
symdisp('p_{10V} = ', round(p10v, 2), ' W')
symdisp('p_{15V} = ', round(p15v, 2), ' W')
symdisp('p_{2i_x} = ', round(p2ix, 2), ' W')

# + id="y9YoVakqQppl"
# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(pR+p10v+p15v+p2ix))
