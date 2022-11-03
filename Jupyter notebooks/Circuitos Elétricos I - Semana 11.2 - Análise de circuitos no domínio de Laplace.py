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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%2011.2%20-%20An%C3%A1lise%20de%20circuitos%20no%20dom%C3%ADnio%20de%20Laplace.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="tv8FnmLnV8mI" outputId="dc8322f3-39e1-40b5-a165-a849fa132961"
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
    cd('/content/ElectricCircuits/Jupyter notebooks')

# + id="LNKjNQzHV8mL"
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from utils import round_expr, symdisp, symplot

from sympy.polys.partfrac import apart

# temp workaround
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False


# + id="Dw_2I2F8V8mM"
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

# + [markdown] id="P36uXgAVV8mN"
# #### Definindo algumas variáveis simbólicas de interesse

# + id="ku-GxaZAV8mO"
t, s  = sp.symbols('t, s')
a     = sp.symbols('a', real=True, positive=True)
omega = sp.symbols('omega', real=True)

# + [markdown] id="9aIpp0HdV8mP"
# # *Circuitos Elétricos I - Semana 11*

# + [markdown] id="CDtctZKQV8mP"
# ### A integral de Laplace
#
# Seja $f(t)$ uma função definida no intervalo $0\leq t \leq \infty$, com $t$ e $f(t)$ reais, então a função $F(s)$, definida pela integral de Laplace
#
# $$\large
# \begin{equation}
# F(s)=\mathcal{L}\{f(t)\}=\int_{0}^{\infty} f(t) e^{-s t} dt,\;\; s \in \mathbb{C},
# \end{equation}
# $$
#
# é conhecida como a transformada de Laplace de $f(t)$.

# + [markdown] id="B586f5MPV8mQ"
# ## Leis de Kirchhoff no domínio de Laplace
#
#
# ### Lei de Kirchhoff das tensões (LKT)
#
# Para qualquer malha fechada no circuito:
#
# Domínio do tempo: $$v_{1}(t)+v_{2}(t)+\cdots+v_{n}(t)=0$$
#
# Domínio de Laplace: $$V_{1}(s)+V_{2}(s)+\cdots+V_{n}(s)=0$$
#
# ### Lei de Kirchhoff das correntes (LKC)
#
# Para qualquer nó no circuito:
#
# Domínio do tempo: $$i_{1}(t)+i_{2}(t)+\cdots+i_{n}(t)=0$$
#
# Domínio de Laplace: $$I_{1}(s)+I_{2}(s)+\cdots+I_{n}(s)=0$$
#

# + [markdown] id="l9gurJgpV8mQ"
# ## Representação de elementos ideais de circuitos no domínio de Laplace
#
# $$
# \begin{array}{|c|c|c|c|} 
# \hline
# \text{Elemento ideal} & \text{ Tensão vs corrente (tempo) } & \text{ Tensão vs corrente (Laplace)} & \text{Impedância } Z(s) = V(s)/I(s)\\
# \hline \text{Resistor} & v(t)=R i(t) & V(s)=R I(s) & Z_{R}(s)=R \\
# \text{Indutor} & v(t)=L \frac{d i(t)}{d t} & V(s)=s L I(s)-L i(0) & Z_{L}(s)=s L \\
# \text{Capacitor} & v(t)=\frac{1}{C} \int_{0}^{t} i(t)+v(0) & V(s)=\frac{I(s)}{s C}+\frac{v(0)}{s} & Z_{C}(s)=\frac{1}{s C} \\ \hline
# \end{array}
# $$

# + [markdown] id="K6-Zfa7fV8mR"
# ### Problema 1
#
# Não existe nenhuma energia armazenada no circuito da figura a seguir no momento em que a fonte de corrente é ligada.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J14C1.png?raw=1" width="500">
#
# a. Determine $I_a(s)$ e $I_b(s)$.\
# b. Determine $i_a(t)$ e $i_b(t)$.\
# c. Determine $V_a(s)$, $V_b(s)$ e $V_c(s)$.\
# d. Determine $v_a(t)$, $v_b(t)$ e $v_c(t)$.

# + [markdown] id="gGG0jl4QV8mR"
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J14C2.png?raw=1" width="500">

# + [markdown] id="xDltYQcWV8mS"
# a. Determinando $I_a(s)$ e $I_b(s)$:

# + id="_cqvt3GAV8mS" outputId="4030ae96-412d-4a09-c20b-471297915bd8"
I2, I3, s = sp.symbols('I2, I3, s')

# define os sistema de equações
eq1 = sp.Eq((4 + s)*I2 - 2*I3, 4)             
eq2 = sp.Eq(-2*s*I2 + s*(4 + s)*I3, 8)  

# resolve o sistema
soluc = sp.solve([eq1, eq2],[I2, I3], dict=True)
soluc

I2 = [sol[I2] for sol in soluc]
I3 = [sol[I3] for sol in soluc]

I1 = 4/s
I2 = I2[0]
I3 = I3[0]

print('Correntes de malha no domínio de Laplace: \n')
symdisp('I_1(s) =', I1, 'As')
symdisp('I_2(s) =', I2, 'As')
symdisp('I_3(s) =', I3, 'As')

# + id="hJ_WRU6TV8mS" outputId="8d8ab3be-6676-45da-87f3-44deeadfe41e"
# Calculando Ia
Ia = I1-I2
Ia = Ia.simplify()

symdisp('I_a(s) =', Ia, 'As')

# + id="AN0_8_SfV8mT" outputId="d7c2cc9b-2642-49e6-a5a1-f01430d1c684"
# Calculando Ib
Ib = I2

symdisp('I_b(s) =', Ib.simplify(), 'As')

# + [markdown] id="EHZTTuJhV8mT"
# b. Determinando $i_a(t)$ e $i_b(t)$

# + id="ZNcZYGocV8mT" outputId="f6f800bd-0e60-42f4-8eb7-5f8a1788bf70"
symdisp('I_a(s) =', Ia.apart(), 'As')

# + id="v00DIDXmV8mU" outputId="a3a83404-7355-401c-c378-da8ab660d3bb"
t = sp.symbols('t',real=True)

ia = invL(Ia.apart(),s,t)

symdisp('i_a(t) =', ia, 'A')

# + id="ezbWSo4JV8mU" outputId="efa875a1-28d8-4bd4-d6a0-bb9f2f534a4c"
symdisp('I_b(s) =', Ib.apart(), 'As')

# + id="UOF5aQz6V8mU" outputId="84cef58c-4fb4-499e-a20b-17c322da4c56"
ib = invL(Ib,s,t)

symdisp('i_b(t) =', ib, 'A')

# + [markdown] id="uLBVs4hgV8mV"
# c. Determinando $V_a(s)$, $V_b(s)$ e $V_c(s)$.

# + id="cM_PfiQgV8mV" outputId="b4926814-f833-4531-80d7-90851ee0a116"
Va = (100/s)*I2
Vb = (100/s)*(I3-I2)
Vc = (100/s)*(I1-I3)

symdisp('V_a(s) =', Va.simplify(), 'Vs')
symdisp('V_b(s) =', Vb.simplify(), 'Vs')
symdisp('V_c(s) =', Vc.simplify(), 'Vs')

# + id="g_9GVkpGV8mV" outputId="ab8cec0c-ce73-4123-f7e9-ec7d59a7f8ef"
symdisp('V_a(s) =', Va.apart(), 'Vs')

# + id="A8iyxQ2FV8mX" outputId="f4c09050-1194-451e-8ef3-1859ff2881cc"
symdisp('V_b(s) =', Vb.apart(), 'Vs')

# + id="rpNyaONeV8mX" outputId="4fa0d8f2-e5fc-461d-ec55-6368e6624689"
symdisp('V_c(s) =', Vc.apart(), 'Vs')

# + [markdown] id="0IpgQuDTV8mX"
# d. Determinando $v_a(t)$, $v_b(t)$ e $v_c(t)$.

# + id="nl4SxN48V8mY" outputId="e79c9ac4-49e9-4e2e-e72e-14bd193589ae"
va = ((-400/9)*sp.exp(-6*t) + (400/9) + (400/3)*t)*sp.Heaviside(t)

symdisp('v_a(t) =', round_expr(va,2), 'V')

# + id="vVQqhyUPV8mY" outputId="f65bacb2-667c-4659-c305-1da5225c0434"
vb = ((800/9)*sp.exp(-6*t) - (800/9) + (400/3)*t)*sp.Heaviside(t)

symdisp('v_b(t) =', round_expr(vb,2), 'V')

# + id="-yZQ4Q3aV8mY" outputId="3f4612e7-908d-4d4c-fc1b-3dfa41ccc465"
vc = va

symdisp('v_c(t) =', round_expr(vc,2), 'V')

# + id="sjtr_EYmV8mY" outputId="9e9983f6-d5c4-4035-9a08-99b6c3d3c08f"
# plota funções no domínio do tempo
intervalo = np.arange(-4, 10, 0.1)
symplot(t, [va, vb, vc], intervalo, ['va(t)','vb(t)','vc(t)'])

# + [markdown] id="7b59ix5LV8mZ"
# Pergunta: estas soluções fazem sentido para o circuito analisado?

# + [markdown] id="BUPN6YahV8mZ"
# ### Problema 2
#
# Não existe nenhuma energia armazenada no circuito da figura a seguir no momento em que a fonte de tensão é conectada.
#
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J14C3.png?raw=1" width="600">
#
# a. Determine $V_0(s)$.\
# b. Determine $v_0(t)$.

# + [markdown] id="lC6CYIRgV8mZ"
# <img src="https://github.com/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/figures/J14C4.png?raw=1" width="600">

# + id="DZBOCABOV8mZ"
Ia, Ib, s = sp.symbols('Ia, Ib, s')

# define o sistema de equações
eq1 = sp.Eq(10*Ia + (s + 250/s)*Ib, 35/s)             
eq2 = sp.Eq(Ia - (1 + 0.4*s)*Ib, 0)

# resolve o sistema
soluc = sp.solve([eq1, eq2],[Ia, Ib], dict=True)
soluc

Ia = [sol[Ia] for sol in soluc]
Ib = [sol[Ib] for sol in soluc]

Ia = Ia[0]
Ib = Ib[0]

# + id="Wr8eYzwSV8mZ" outputId="7064c064-edc2-45b7-e484-a8a17b530772"
symdisp('I_a(s) =', Ia.simplify(), 'As')

# + id="YHcmTWQ1V8mZ" outputId="10925e2a-020d-48da-d5df-d885698b39d2"
symdisp('I_b(s) =', Ib.simplify(), 'As')

# + id="davxp05nV8ma" outputId="cb0b692f-6f4e-40df-8892-a07efe3420e2"
V0 = 35/s - 2*Ia

symdisp('V_0(s) =', V0.simplify(), 'Vs')

# + id="0p9jLv8IV8ma" outputId="90d19806-8085-4a90-a37f-fb42f638f84a"
symdisp('V_0(s) =', partFrac(V0, 4), 'Vs')

# + id="m5NcG_8vV8ma" outputId="84a50bd6-e0d3-4c9c-f0bd-6b2b207ea8b1"
raizes = np.roots([5, 10, 250, 0])
raizes

# + id="X0iMBpDJV8ma" outputId="b5fb41f1-4836-4c6e-8ee2-98338b86be6a"
K    = sp.symbols('K')
σ, ω = sp.symbols('σ, ω', real=True)

j = sp.I

F = K/(s + σ + ω*j) + sp.conjugate(K)/(s + σ - ω*j)

symdisp('F(s) =', F)

# + id="YqiiFk5IV8mb" outputId="226ad186-5ae7-4717-abd1-aab4c8644272"
symdisp('f(t) =', invL(F,s,t))

# + id="LjlGrdWkV8mb" outputId="808ed847-ca7e-4271-a4bf-cb2b585dce0d"
v0 = (35 + sp.exp(-t)*(-5.6*sp.cos(7*t)-1.2*sp.sin(7*t)))*sp.Heaviside(t)

symdisp('v_0(t) =', v0)

# + id="ivadXkoyV8mb" outputId="dab9f945-42a3-40f6-e978-b5455a739564"
# plota funções no domínio do tempo
intervalo = np.arange(-4, 10, 0.05)
symplot(t, v0, intervalo, 'v0(t)')
