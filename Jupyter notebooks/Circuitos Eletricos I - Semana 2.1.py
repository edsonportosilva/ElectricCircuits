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
HTML("""
<style>
.output_png {
    display: table-cell;
    text-align: center;
    vertical-align: middle;
}
</style>
""")

# # *Circuitos Elétricos I*

# ## Semana 2 - Exercícios
#
# ### Exercício 1: circuito com fonte controlada de corrente
#
# No circuito abaixo, dado que $\frac{V_0}{V_s}=9$, determine o valor de $A$.

from IPython.display import Image
Image("./figures/J2C1.png", width=600)

# ### Exercício 2: circuito com fonte controlada de tensão
#
# Determine o valor de todas as correntes no circuito abaixo.

from IPython.display import Image
Image("./figures/J2C2.png", width=500)

# ### Solução das equações

import sympy as sp
import numpy as np

# +
# define as N variáveis desconhecidas
i1, i2, i3, i4 = sp.symbols('i1, i2, i3, i4')

# define os sistema de N equações
eq1 = sp.Eq(i1 - i2 + i3,    0)             
eq2 = sp.Eq(i1 + i3 -i4,     3)  
eq3 = sp.Eq(30*i2 + 10*i3, -11)
eq4 = sp.Eq(20*i1 + 30*i2,  -5)

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3, eq4), dict=True)

i1 = np.array([sol[i1] for sol in soluc])
i2 = np.array([sol[i2] for sol in soluc]) 
i3 = np.array([sol[i3] for sol in soluc]) 
i4 = np.array([sol[i4] for sol in soluc]) 
ix = 3

print('Solução do sistema:\n\n i1 = %.3f A,\n i2 = %.3f A,\n i3 = %.3f A,\n i4 = %.3f A, \n ix = %.3f A.'\
      %(i1, i2, i3, i4, ix))
# -

# #### Cálculo das potências

# +
# expressões para as potências associadas a cada corrente
p1 = 20*i1**2
p2 = 30*i2**2 -10*i2
p3 = 10*i3**2 + 6*i3
p4 = 15*i4
px = 5*ix**2

print('Potências:\n\n p1 = %.2f W,\n p2 = %.2f W,\n p3 = %.2f W,\n p4 = %.2f W\n px = %.2f W'\
      %(p1, p2, p3, p4, px))
# -

# calcula somatório das potências
print('Somatório das potências : %.2f W\n' %(p1+p2+p3+p4+px))


