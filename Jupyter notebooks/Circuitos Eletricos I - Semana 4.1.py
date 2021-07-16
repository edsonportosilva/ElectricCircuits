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

# # *Circuitos Elétricos I - Semana 4*

# ## Transformações de fontes
#
# Uma fonte de tensão ideal de valor $V_s$ conectada em série com um resistor $R$ pode ser substituída por uma fonte de corrente ideal de valor $I_s$ conectada em paralelo com uma resistência $R$, e vice-versa. Estas substituições não alterarão o comportamento dos demais elementos do circuito desde que $V_s=RI_s$.
#
# <img src=./figures/J5C0.png width=600>
#
# ## Deslocamentos de fontes
#
# * **Deslocamento de fontes de tensão**: conectar fontes ideais de tensão em série com todos os elementos ideais de dois terminais ligados a um nó, com polaridades adequadas, não altera as equações que descrevem o comportamento do circuito.
#
# * **Deslocamento de fontes de corrente**: conectar um laço de fontes ideais de corrente iguais e de mesmo sentido num circuito não altera as equações que descrevem o comportamento do circuito.

# ### Problema 1
#   
# Determine a corrente que passa pelo resistor de $25~\Omega$ aplicando transformações e deslocamentos de fontes.

Image("./figures/J5C1.png", width=500)

# Simulação do circuito: https://tinyurl.com/ydk42vvn
