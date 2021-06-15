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

# # *Circuitos Elétricos I - Semana 7*

#
# ## Resumo dos elementos passivos ideais de dois terminais
#
# $$
# \begin{array}{|l|c|c|c|}
# \hline \text { Propriedade } & R & L & C \\
# \hline \text { Relação } i-v  & i=\frac{v}{R} & i=\frac{1}{L} \int_{t_{0}}^{t} v(\tau) d \tau+i\left(t_{0}\right) & i=C \frac{d v}{d t} \\
# \text { Relação } v-i & v=Ri & v=L \frac{d i}{d t} & v=\frac{1}{C} \int_{t_{0}}^{t} i(\tau) d \tau+v\left(t_{0}\right) \\
# p \text { (potência }) & p=Ri^{2} & p=L i \frac{d i}{d t} & p=C v \frac{d v}{d t} \\
# w \text { (energia armazenada) } & 0 & w=\frac{1}{2} L i^{2} & w=\frac{1}{2} C v^{2} \\
# \text { Associação em série } & R_{\mathrm{eq}}=R_{1}+R_{2} & L_{\mathrm{eq}}=L_{1}+L_{2} & \frac{1}{C_{\mathrm{eq}}}=\frac{1}{C_{1}}+\frac{1}{C_{2}} \\
# \text { Associação em paralelo } & \frac{1}{R_{\mathrm{eq}}}=\frac{1}{R_{1}}+\frac{1}{R_{2}} & \frac{1}{L_{\mathrm{eq}}}=\frac{1}{R_{1}}+\frac{1}{R_{2}} & C_{\mathrm{eq}}=C_{1}+C_{2} \\
# \text { Comportamento em regime estacionário } & \text { sem mudanças } & \text { curto-circuito } & \text { circuito aberto } \\
# \text { Pode } v \text { variar instantaneamente? } & \text { sim } & \text { sim } & \text { não } \\
# \text { Pode } i \text { variar instantaneamente? } & \text { sim } & \text { não } & \text { sim }\\ \hline
# \end{array}
# $$

# ### Divisores de tensão e corrente com indutores e capacitores
#   
# Determine as expressões para os circuitos divisores de tensão e corrente ilustrados na figura abaixo.
#

Image("./figures/J10C1.png", width=700)
