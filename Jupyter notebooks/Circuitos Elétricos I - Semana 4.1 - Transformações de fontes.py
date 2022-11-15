# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%204.1%20-%20Transforma%C3%A7%C3%B5es%20de%20fontes.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="9KGudob6WsJw" outputId="b90476a8-1186-4cc7-f925-19de0b07ab78"
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
    cd('/content/ElectricCircuits/')
    # ! pip install -e .

# + [markdown] id="YpnadznCWsJz"
# # *Circuitos Elétricos I - Semana 4*

# + [markdown] id="3ACCnamDWsJ0"
# ## Transformações de fontes
#
# Uma fonte de tensão ideal de valor $V_s$ conectada em série com um resistor $R$ pode ser substituída por uma fonte de corrente ideal de valor $I_s$ conectada em paralelo com uma resistência $R$, e vice-versa. Estas substituições não alterarão o comportamento dos demais elementos do circuito desde que $V_s=RI_s$.
#
# <img src=https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J5C0.png?raw=1 width=600>
#
# ## Deslocamentos de fontes
#
# * **Deslocamento de fontes de tensão**: conectar fontes ideais de tensão em série com todos os elementos ideais de dois terminais ligados a um nó, com polaridades adequadas, não altera as equações que descrevem o comportamento do circuito.
#
# * **Deslocamento de fontes de corrente**: conectar um laço de fontes ideais de corrente iguais e de mesmo sentido num circuito não altera as equações que descrevem o comportamento do circuito.

# + [markdown] id="gEfD-4OLWsJ1"
# ### Problema 1
#   
# Determine a corrente que passa pelo resistor de $25~\Omega$ aplicando transformações e deslocamentos de fontes.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J5C1.png?raw=1" width="500">

# + [markdown] id="LJHfTVdTWsJ1"
# Simulação do circuito: https://tinyurl.com/ydk42vvn
