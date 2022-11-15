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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%2012.1%20-%20Exerc%C3%ADcios%20com%20fun%C3%A7%C3%A3o%20de%20transfer%C3%AAncia%20e%20integral%20de%20convolu%C3%A7%C3%A3o.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="7WPlhsHhUuWo" outputId="23066a1f-b4bd-479a-844c-deba904a0de7"
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

# + [markdown] id="h6sSBJ9bUuWs"
# # *Circuitos Elétricos I - Semana 12.1*

# + id="AEIxuYElUuWt"
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from circuit.utils import round_expr, symdisp, symplot

from sympy.polys.partfrac import apart

# temp workaround
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False


# + id="4LKqwI9nUuWt"
# transformada de Laplace
def L(f,t,s):
    return sp.laplace_transform(f, t, s, noconds=True)

# transformada inversa de Laplace
def invL(F,s,t):
    return sp.re(sp.inverse_laplace_transform(F, s, t, noconds=True))

# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    coeff = expr.as_numer_denom()
    c0 = sp.poly(coeff[1].cancel()).coeffs()[0]
    
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def partFrac(expr, Ndigits):
    expr = expr.cancel()
    expr = apart(adjustCoeff(expr), s, full=True).doit()
    
    return sp.N(expr, Ndigits)

sp.init_printing()

# + [markdown] id="0UcuJTrZUuWu"
# #### Definindo algumas variáveis simbólicas de interesse

# + id="05tOWwq7UuWu"
s     = sp.symbols('s')
a     = sp.symbols('a', real=True, positive=True)
omega, t = sp.symbols('omega, t', real=True)
infty = sp.oo

# + [markdown] id="DOu_DBGlUuWv"
# ### Problema 1
#
# O circuito da figura a seguir está em regime estacionário no momento em que chave é aberta. Sabe-se que $v(t)=\mathrm{12\;V}$.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J15C1.png?raw=1" width="600">
#
# Simulação do circuito: https://tinyurl.com/y84pozs3
#
# a. Determine $I_0(s)$ e $I_1(s)$.\
# b. Verifique a consistência das respostas do item a. com os teoremas do valor inicial e do valor final.\
# c. Determine a função de transferência $H_0(s)$ entre $V(s)$ e $I_0(s)$.\
# d. Determine a função de transferência $H_1(s)$ entre $V(s)$ e $I_1(s)$.\
# e. Determine a função de transferência $H_c(s)$ entre $V(s)$ e $V_c(s)$.\
# f. Determine a $v_c(t)$ para o caso em que a tensão aplicada $v(t)$ em $\mathrm{V}$ corresponde ao gráfico a seguir:
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J15Fig1.png?raw=1" width="400">

# + [markdown] id="k6YovyW1UuWv"
# a. Determinando $I_0(s)$ e $I_1(s)$:

# + id="WYDyrgDsUuWw" outputId="51baed0d-ce0b-42e2-dede-e641ecda82b3"
I0, I1, s = sp.symbols('I_0, I_1, s')

# define os sistema de equações
eq1 = sp.Eq((-2*s**2)*I0 + (2*s**2 + 10*s + 250)*I1, 2.4*s + 12)             
eq2 = sp.Eq((4*s+50)*I0 -2*s*I1, -2.4)  

# resolve o sistema
soluc = sp.solve([eq1, eq2],[I0, I1], dict=True)
soluc

I0 = [sol[I0] for sol in soluc]
I1 = [sol[I1] for sol in soluc]

I0 = I0[0]
I1 = I1[0]

print('Correntes no domínio de Laplace: \n')
symdisp('I_0(s) =', I0, 'As')
symdisp('I_1(s) =', I1, 'As')

# + [markdown] id="DX6d4RX1UuWw"
# b. Checando a consistência das soluções
#
# **Teorema do valor inicial (TVI)**
#
# $$
# f(0^+) = \lim_{t \to 0^+}f(t) = \lim_{s \to \infty}sF(s)
# $$
#

# + id="PwWicqlPUuWx" outputId="831debd6-0e3d-40d2-d1b6-1cee7792f4ec"
i0_0_tvi = sp.limit(s*I0, s, infty)
i1_0_tvi = sp.limit(s*I1, s, infty)


symdisp('i_0(0^+) = ', i0_0_tvi, ' A' )
symdisp('i_1(0^+) = ', i1_0_tvi, ' A' )

# + [markdown] id="UK0FH0oYUuWx"
# **Teorema do valor final (TVF)**
#
# $$
# f(\infty) = \lim_{t \to \infty}f(t) = \lim_{s \to 0}sF(s)
# $$
#
#

# + id="H6w_NEphUuWx" outputId="ad34bc08-7c53-49f2-a7f9-49a6e82fc109"
i0_inf_tvf = sp.limit(s*I0, s, 0)
i1_inf_tvf = sp.limit(s*I1, s, 0)


symdisp('i_0(\infty) = ', i0_inf_tvf, ' A' )
symdisp('i_1(\infty) = ', i1_inf_tvf, ' A' )

# + id="juT2UhvrUuWy" outputId="cb5bb0e0-bab8-405d-bfa1-7f0be4256d5a"
C = 4e-3  # F

# Calculando Vc
Vc = (1/(s*C))*I1

Vc = Vc.simplify()

symdisp('V_c(s) =', adjustCoeff(Vc).simplify(), 'Vs')

# + id="aYmJ9MOAUuWy" outputId="5878586f-a742-48ca-a551-500a77e3e4e0"
 sp.limit(s*Vc, s, 0)

# + id="Pp1IFtV1UuWz" outputId="753791ec-99a5-451e-916e-9960213b787a"
np.roots([1, 35, 375, 3125, 0])

# + id="SOsp1CEbUuW0" outputId="e1d8d2ce-dd21-4bb4-86c0-9910ad500c37"
partFrac(Vc, 3)

# + id="Om6pHBZpUuW0"
#vc = invL(partFrac(Vc,4), s, t)

#symdisp('v_c(t) = ', vc, ' V')

# + id="ICrkbuDGUuW0" outputId="b6d2d1a5-5e04-4d71-dd1c-8587d73768ee"
vc = (12 + sp.exp(-5*t)*( -15*sp.cos(10*t) + 30*sp.sin(10*t) ) + 3*sp.exp(-25*t) )*sp.Heaviside(t)

symdisp('v_c(t) = ', vc, 'V')

# + id="pTNu5WsWUuW0" outputId="47d0fee5-51e7-47f1-f2a9-4523405f2992"
# plota funções no domínio do tempo
intervalo = np.arange(-1, 4, 0.01)
symplot(t, vc, intervalo, 'vc(t)')

# + [markdown] id="966-3kcCUuW1"
# c-e) Determinando $H_0(s)$, $H_0(s)$ e $H_c(s)$.

# + id="JRE0vhWTUuW1" outputId="acbeb82a-8483-49da-c934-c579f690456d"
V = 12/s

H0 = I0/V

symdisp('H_0(s) =', H0,)

# + id="XZKe1Oh2UuW1" outputId="b9a8e09f-1efe-4f41-90f0-9caefdb802cd"
H1 = I1/V
H1 = adjustCoeff(H1)

symdisp('H_1(s) =', H1,)

# + id="7n4eb_QwUuW1" outputId="b03aa34c-7dc3-480f-d101-6d2de3d65866"
Hc = Vc/V
Hc = adjustCoeff(Hc)

symdisp('H_c(s) =', Hc,)

# + [markdown] id="pCiEjYDQUuW2"
# f. $v_c(t)=?$

# + id="Sr9nC17dUuW2" outputId="eeafbcfa-cc13-4505-85da-3e94303857c7"
v = 2*(sp.Heaviside(t)-sp.Heaviside(t-1)) - 1*(sp.Heaviside(t-1)-sp.Heaviside(t-2))

symdisp('v(t) =', v, ' V')

# plota funções no domínio do tempo
intervalo = np.arange(-1, 3, 0.01)
symplot(t, v, intervalo, 'v(t)')

# + id="piKX_yB8UuW2" outputId="db1c2186-56ba-41c0-c746-8c4f2171ac3d"
# determina Vc(s) via função de transferência
V = L(v, t, s)
Vc = Hc*V

symdisp('V_c(s) =', Vc.simplify(), ' Vs')

# + id="YWU-ZiLgUuW2" outputId="6bf2df29-6ea2-41e7-abac-fca434bbad78"
# função auxiliar Va(s)
P = (25*s**2 + 875*s + 3125)/(s**4 + 35*s**3 + 375*s**2 + 3125*s)
#P = partFrac(P, 10)

symdisp('P(s) =', partFrac(P, 10), ' Vs')

# + id="_BDe5ZSZUuW2" outputId="67baf491-d24b-4bc3-b51c-e85fd24c69e3"
# encontra va(t)
p = invL(P.apart(), s, t)
p = p.expand()

symdisp('p(t) =', p, ' V')

# + id="wO_nqlEJUuW2" outputId="e16f51f0-bd09-4402-d2b2-50d078d947f4"
vc = 2*p - 3*p.subs({t:sp.UnevaluatedExpr(t-1)}) + p.subs({t:sp.UnevaluatedExpr(t-2)})

symdisp('v_c(t) =', vc, ' V')

# + id="L2RHQL_fUuW3" outputId="a1de4d18-c877-4f47-bd8a-dc6d95c3e166"
# plota funções no domínio do tempo
intervalo = np.arange(-1, 3, 0.01)
symplot(t, [v, vc], intervalo, ['v(t)','vc(t)'])
