# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] id="view-in-github" colab_type="text"
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Circuitos%20El%C3%A9tricos%20I%20-%20Semana%208.2%20-%20Circuitos%20RLC%20de%20segunda%20ordem.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + id="q2oERC9xSgCt" outputId="e4fa07da-12ec-4151-ccee-732e9387e59b"
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

# + [markdown] id="zdja3GqYSgCw"
# # *Circuitos Elétricos I - Semana 8*
#
# # Circuitos de segunda ordem

# + [markdown] id="O85zBEOVSgCx"
# ## Circuito RLC em paralelo
#
# <img src="./figures/J12C2.png?raw=1" width="800">
#
# Simulação: https://tinyurl.com/ycnkjnot
#
# ### Aplicação das Leis de Kirchhoff 
#
# $$\begin{align}
#    i_R + i_L + i_C &= i_s\\
#    \frac{v}{R} + i_L + C\frac{d v}{d t} &= i_s\nonumber\\
#     \frac{1}{R}\left[L\frac{d i_L}{d t}\right] + i_L + C \frac{d}{d t}\left[L\frac{d i_L}{d t}\right]  &= i_s\nonumber\\
#     \frac{d^{2} i_L}{d t^{2}}+\frac{1}{RC} \frac{d i_L}{d t}+\frac{1}{L C} i_L &=\frac{i_s}{LC}
#    \end{align}
# $$
#
# com $\alpha = \frac{1}{2RC}$ e $\omega_0 = \frac{1}{\sqrt{LC}}$, temos
#
# $$ 
# \begin{equation}\label{EDO1} 
# \frac{d^{2} i_L}{d t^{2}}+2\alpha \frac{d i_L}{d t}+\omega_0^2 i_L=i_{\mathrm{s}}\omega_0^2 
# \end{equation} 
# $$
#
# A equação \ref{EDO1} é uma EDO de segunda ordem, linear e de coeficientes constantes.
#
# Equação característica:
#
# $$\begin{equation} s^2+2\alpha s + \omega_0^2=0 \end{equation} $$
#
# Raízes da equação característica:
#
# $$
# \begin{align}
# s_1 &=-\alpha +\sqrt{\alpha^2-\omega_0^2}\\
# s_2 &=-\alpha -\sqrt{\alpha^2-\omega_0^2}
# \end{align}
# $$

# + [markdown] id="X5_oXX0jSgCy"
# ### Resposta total 
#
# A resposta transiente de circuitos RLC em paralelo, seja ela natural ($i_L(\infty)=0$) ou ao degrau ($i_L(\infty)=i_s$), pode ser classificada nas três casos seguintes. Em todos os casos, assume-se que o transiente teve início no instante $t_0$ (instante do chaveamento).
#
# #### Caso superamortecido ($\alpha>\omega_0\Rightarrow \text{raízes reais e distintas}$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} i_L(t) =A_{1} e^{s_{1} (t-t_0)}+A_{2} e^{s_{2} (t-t_0)}+i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=A_1 + A_2 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &=s_1A_1 + s_2A_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $A_1$ e $A_2$:
#
# $$
# \begin{align}
# A_{1} &=\frac{\frac{1}{L} v_C(t_0^+)-s_{2}\left[i_L(t_0^+)-i_L(\infty)\right]}{s_{1}-s_{2}} \\
# A_{2} &=\frac{-\frac{1}{L} v_C(t_0^+)+s_{1}\left[i_L(t_0^+)-i_L(\infty)\right]}{s_{1}-s_{2}}
# \end{align}
# $$

# + [markdown] id="Yjh1u6YdSgCy"
# #### Caso subamortecido ($ \alpha<\omega_0\Rightarrow\text{raízes complexas e conjugadas} $):
#
# Fazendo $\omega_d = \sqrt{\omega_0^2-\alpha^2}$ temos $s_1 = -\alpha +j\omega_d$ e $s_2 = -\alpha -j\omega_d$.
#
# Solução geral da EDO:
#
# $$\begin{equation} i_L(t) = e^{-\alpha(t-t_0)}\left\lbrace B_{1}\cos[\omega_d (t-t_0)] + B_{2}\sin[\omega_d (t-t_0)]  \right\rbrace + i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=B_1 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &= -\alpha B_1 +\omega_d B_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $B_1$ e $B_2$:
#
# $$
# \begin{align}
# B_{1} &=i_L(t_0^+)-i_L(\infty) \\
# B_{2} &=\frac{\frac{1}{L} v_C(t_0^+)+\alpha\left[i_L(t_0^+)-i_L(\infty)\right]}{\omega_d}
# \end{align}
# $$

# + [markdown] id="HfzAsEQMSgCz"
# #### Caso criticamente amortecido ($\alpha=\omega_0\Rightarrow \text{raízes reais e idênticas } s_1=s_2=-\alpha$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} i_L(t) =D_{1} e^{-\alpha(t-t_0)}+D_{2}(t-t_0) e^{-\alpha(t-t_0)}+i_L(\infty) \end{equation}$$
#
# Condições iniciais para $i_L(t)$:
#
# $$
# \begin{align}
# i_L(t_0^+) &=D_1 + i_L(\infty)\\
# \frac{di_L(t_0^+)}{dt} &=-\alpha D_1 + D_2 = \frac{1}{L} v_C(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $D_1$ e $D_2$:
#
# $$
# \begin{align}
# D_{1} &=i_L(t_0^+)-i_L(\infty) \\
# D_{2} &= \frac{1}{L} v_C(t_0^+)+\alpha\left[i_L(t_0^+)-i_L(\infty)\right]
# \end{align}
# $$

# + [markdown] id="hLRcb9zCSgCz"
# ### Problema 1
#
# Para o circuito a seguir, as chaves $ch1$ e $ch2$ estiveram abertas por um longo intervalo de tempo. 
#
# <img src="./figures/J12C3.png?raw=1" width="700">
#
#
# a. Considerando que apenas $ch1$ fecha em $t_0=0$s, determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.\
# b. Qual o máximo valor (absoluto) atingido pela tensão aplicada aos terminais do capacitor para $t\geq 0^+$? Em que instante ele ocorre?\
# c. Considerando que apenas $ch2$ fecha em $t_0=0$s, determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.
#
# Link para a simulação do circuito: https://tinyurl.com/yf8pj57t

# + id="uxLDMS0ySgC0"
import numpy as np
import sympy as sp
from circuit.utils import round_expr, symdisp, symplot

# + [markdown] id="TS7Si0UGSgC0"
# ### Resolvendo o problema com o Python
#
# **Resolução item (a):**
#
# **Calcula $\alpha$ e $\omega_0$**

# + id="o7B8socsSgC1" outputId="d9096e9a-e27a-4a47-e97c-655fdc265254"
# Parâmetros do circuito:
R = 1.64
L = 6e-3
C = 0.5e-3

# calculando α e ω0
α  = 1/(2*R*C)       # Frequência de Neper do circuito RLC em paralelo
ω0 = 1/np.sqrt(L*C)  # Frequência de ressonância do circuito RLC

symdisp('α =', round(α, 2), ' rad/s')
symdisp('ω_0 =', round(ω0, 2), ' rad/s')

# + [markdown] id="SbyFfLvYSgC1"
# **Define os valores iniciais $v_c(t_0^+)$ e $i_L(t_0^+)$ e o valor final $i_L(\infty)$ (obtidos da análise do circuito)**

# + id="4FikqyGVSgC1"
# informações obtidas pela análise do circuito

t0 = 0 # instante do chaveamento

iL_inf = -4 # valor final da corrente no indutor
iL_t0 = 2   # valor inicial da corrente no indutor
vc_t0 = 0   # valor inicial da tensão no capcitor

# + [markdown] id="9ChJkHc5SgC2"
# **Calcula as raízes da equação característica $s_1$ e $s_2$**

# + id="d025MREqSgC2" outputId="330a88a9-f47c-47de-f701-abc6766a4947"
# raízes da equação característica
s1 = -α + np.sqrt(α**2-ω0**2)
s2 = -α - np.sqrt(α**2-ω0**2)

print('Raízes da equação característica:')
symdisp('s_1 =', round(s1, 2), ' rad/s')
symdisp('s_2 =', round(s2, 2), ' rad/s')

# define variáveis da solução geral
t, A1, A2 = sp.symbols('t, A1, A2')

# expressão geral da resposta superamortecida
iL = A1*sp.exp(s1*(t-t0)) + A2*sp.exp(s2*(t-t0)) + iL_inf

print('Forma geral da solução:')
symdisp('i_L(t) = ', round_expr(iL,2), 'A')

# + [markdown] id="61MPzEsKSgC2"
# **Resolve o sistema de equações para determinação das constantes $A_1$ e $A_2$**

# + id="NhfPuDUeSgC3" outputId="2f2d2958-41d2-47eb-c60a-91c75dc58149"
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq(   A1 +    A2 + iL_inf, iL_t0)             
eq2 = sp.Eq(s1*A1 + s2*A2,        vc_t0/L)  

print('Sistema de equações:')
symdisp('(I): ', round_expr(eq1, 2),' ')
symdisp('(II): ', round_expr(eq2, 2),' ')

# + id="obvKRyd2SgC3" outputId="bc70d843-1c22-43e3-bda3-871e6451335d"
# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
A1 = np.array([sol[A1] for sol in soluc])
A2 = np.array([sol[A2] for sol in soluc])

A1 = A1[0]
A2 = A2[0]

print('Solução do sistema:')
symdisp('A_1 =', round(A1, 2), ' A')
symdisp('A_2 =', round(A2, 2), ' A')

# + [markdown] id="GarNXHCQSgC3"
# **Determina a expressão final para $i_L(t)$**

# + id="p9TqqUWUSgC3" outputId="bcc03d15-9f9b-443f-fec3-e2ab97ee2ea5"
# expressão geral da resposta subamortecida
iL = A1*sp.exp(s1*(t-t0)) + A2*sp.exp(s2*(t-t0)) + iL_inf

symdisp('i_L(t) = ', round_expr(iL,2), 'A')

# + [markdown] id="rdoc4f9nSgC4"
# **Plota gráfico de $i_L(t)$**

# + id="V0t-pc4CSgC4" outputId="a401c41a-b180-49eb-fcd6-1a0292a7f48c"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.02,100)
symplot(t,iL, intervalo, 'iL(t)')

# + [markdown] id="uQaYfe1dSgC4"
# **Determina $v_C(t)$ a partir de $i_L(t)$**

# + id="nfJX_EUeSgC4" outputId="4a51dc90-a952-4272-9631-006ac18856b6"
# tensão aplicada sobre o capacitor (= tensão sobre o indutor)
vC = L*sp.diff(iL, t)

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + [markdown] id="va80jJURSgC4"
# **Plota gráfico de $v_C(t)$**

# + id="v2YTfgG9SgC5" outputId="36a3509d-8609-4f1f-bd8e-b9878f0ddd08"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.02,100)
symplot(t, vC, intervalo, 'vC(t)')

# + [markdown] id="m8XlMuifSgC5"
# **Resolução item (b):**
#
# $$\frac{dv_C}{dt} = 0$$

# + id="Oskah7UySgC5" outputId="faa1f6ce-ed86-4beb-fcb3-d2bc21502bf5"
# define a equação dvC/dt = 0
eq1 = sp.Eq(sp.diff(vC, t),0)  

round_expr(eq1, 2)

# + id="zshlpG4wSgC5" outputId="b858fd50-69ee-4c03-8252-7e3304d92f9a"
# resolve a equação em t
ts = sp.solveset(eq1, t).args[0]

# calcula o valor de vC(t) para t = ts
vC_ts = vC.evalf(subs={t:ts})

symdisp('t_s = ', round(ts*1000,2), 'ms')
symdisp('v_C(t_s) = ', round(vC_ts,2), 'V')

# + [markdown] id="y0RjHQnOSgC5"
# **Resolução item (c):**

# + id="e9--hMZ-SgC5" outputId="7341ce55-6330-4c47-bf40-345df19d2b46"
# Parâmetros do circuito:
R = 6
L = 6e-3
C = 0.5e-3

# calculando α e ω0
α  = 1/(2*R*C)       # Frequência de Neper do circuito RLC em paralelo
ω0 = 1/np.sqrt(L*C)  # Frequência de ressonância do circuito RLC

symdisp('α =', round(α, 2), ' rad/s')
symdisp('ω_0 =', round(ω0, 2), ' rad/s')

# + id="9kAVXVo4SgC6"
# informações obtidas pela análise do circuito
iL_inf = 0  # valor final da corrente no indutor
iL_t0 = 2   # valor inicial da corrente no indutor
vc_t0 = 0   # valor inicial da tensão no capcitor

t0 = 0 # instante do chaveamento

# + id="ikzX5ptFSgC6" outputId="28800e38-b6b9-40e2-976f-c3f3cd6059be"
# define a frequência de oscilação amortecida
ωd = np.sqrt(ω0**2 - α**2)

print('Frequência de oscilação amortercida:')
symdisp('ω_d =', round(ωd, 2), ' rad/s')

# define variáveis da solução geral
t, B1, B2 = sp.symbols('t, B1, B2')

# expressão geral da resposta subamortecida
iL = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0)) + B2*sp.sin(ωd*(t-t0))) + iL_inf

print('Forma geral da solução:')
symdisp('i_L(t) = ', round_expr(iL,2), ' A')

# + id="65gCoDZtSgC7" outputId="8c9fe797-f5b9-4995-c42b-59a099c44c74"
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq(   B1 + iL_inf, iL_t0)             
eq2 = sp.Eq(-α*B1 + ωd*B2,  vc_t0/L)  

print('Sistema de equações:')
symdisp('(I): ', round_expr(eq1, 2),' ')
symdisp('(II): ', round_expr(eq2, 2),' ')

# + id="J5-wGR1zSgC7" outputId="826a004a-62e2-43f7-ed41-82827fc384d9"
# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
B1 = np.array([sol[B1] for sol in soluc])
B2 = np.array([sol[B2] for sol in soluc])

B1 = B1[0]
B2 = B2[0]

print('Solução do sistema:')
symdisp('B_1 =', round(B1, 2), ' A')
symdisp('B_2 =', round(B2, 2), ' A')

# + id="wqGDhdF8SgC7" outputId="3906a6dd-6cdd-4df8-fb35-d38118979f32"
# expressão geral da resposta subamortecida
iL = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0))+B2*sp.sin(ωd*(t-t0))) + iL_inf

symdisp('i_L(t) = ', round_expr(iL,2), 'A')

# + id="Uvw5XKEZSgC7" outputId="157083d1-c76a-4c39-fd27-92b60db7d67a"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.05,100)
symplot(t, iL, intervalo, 'iL(t)')

# + id="v4fQEF-ESgC7" outputId="f1e0db89-1201-4763-9f7e-e2fbe08f3a61"
# tensão aplicada sobre o capacitor (= tensão sobre o indutor)
vC = L*sp.diff(iL, t)
vC = sp.simplify(vC)

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + id="NUshGl_LSgC8" outputId="61cf0dba-1b25-43eb-906f-d918a812b050"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.05,100)
symplot(t, vC, intervalo, 'vC(t)')
symplot(t, [iL, vC], intervalo, ['iL(t)', 'vC(t)'])

# + [markdown] id="iyqAkxZGSgC8"
# ## Circuito RLC em série

# + [markdown] id="zgBsE64OSgC8"
# <img src="./figures/J12C1.png?raw=1" width="800">
#
# ### Aplicação das Leis de Kirchhoff 
#
# $$\begin{align}
#    v_R + v_L + v_C &= v_s\\
#    R i + L\frac{d i}{dt}+v_C &= v_s\nonumber\\
#    R\left[C\frac{dv_C}{dt}\right] + L\frac{d}{dt}\left[C\frac{dv_C}{dt} \right] + v_C &= v_s\nonumber\\
#     \frac{d^{2} v_{\mathrm{C}}}{d t^{2}}+\frac{R}{L} \frac{d v_{\mathrm{C}}}{d t}+\frac{1}{L C}   v_{\mathrm{C}} &=\frac{v_{\mathrm{s}}}{LC}
#    \end{align} 
# $$
#
# com $ \alpha = \frac{R}{2L}$ e $\omega_0 = \frac{1}{\sqrt{LC}}$, temos
#
# $$ \begin{equation}\label{EDO2} \frac{d^{2} v_{\mathrm{C}}}{d t^{2}}+2\alpha \frac{d v_{\mathrm{C}}}{d t}+\omega_0^2 v_{\mathrm{C}}=v_{\mathrm{s}}\omega_0^2 \end{equation} $$
#
# A equação \ref{EDO2} é uma EDO de segunda ordem, linear e de coeficientes constantes.
#
# Equação característica:
#
# $$\begin{equation} s^2+2\alpha s + \omega_0^2=0 \end{equation}$$
#
# Raízes da equação característica:
#
# $$
# \begin{align}
# s_1 &=-\alpha +\sqrt{\alpha^2-\omega_0^2}\\
# s_2 &=-\alpha -\sqrt{\alpha^2-\omega_0^2}
# \end{align}
# $$

# + [markdown] id="8t3m-zXzSgC8"
# ### Resposta total 
#
# A resposta transiente de circuitos RLC em série, seja ela natural ($v_C(\infty)=0$) ou ao degrau ($v_C(\infty)=v_s$), pode ser classificada nas três casos seguintes. Em todos os casos, assume-se que o transiente teve início no instante $t_0$ (instante do chaveamento).
#
# #### Caso superamortecido ($\alpha>\omega_0\Rightarrow \text{raízes reais e distintas}$):
#
# Solução geral da EDO:
#
# $$\begin{equation} v_{\mathrm{C}}(t) =A_{1} e^{s_{1} (t-t_0)}+A_{2} e^{s_{2} (t-t_0)}+v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=A_1 + A_2 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &=s_1A_1 + s_2A_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $A_1$ e $A_2$:
#
# $$
# \begin{align}
# A_{1} &=\frac{\frac{1}{C} i_{\mathrm{L}}(t_0^+)-s_{2}\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{s_{1}-s_{2}} \\
# A_{2} &=\frac{-\frac{1}{C} i_{\mathrm{L}}(t_0^+)+s_{1}\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{s_{1}-s_{2}}
# \end{align}
# $$

# + [markdown] id="ogSletHESgC8"
# #### Caso subamortecido ($\alpha<\omega_0\Rightarrow \text{raízes complexas e conjugadas}$):
#
# Fazendo $\omega_d = \sqrt{\omega_0^2-\alpha^2}$ temos $s_1 = -\alpha +j\omega_d$ e $s_2 = -\alpha -j\omega_d$.
#
# Solução geral da EDO:
#
# $$\begin{equation} v_{\mathrm{C}}(t) = e^{-\alpha(t-t_0)}\left\lbrace B_{1}\cos[\omega_d (t-t_0)] + B_{2}\sin[\omega_d (t-t_0)]  \right\rbrace + v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=B_1 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &= -\alpha B_1 +\omega_d B_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $B_1$ e $B_2$:
#
# $$
# \begin{align}
# B_{1} &=v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty) \\
# B_{2} &=\frac{\frac{1}{C} i_{\mathrm{L}}(t_0^+)+\alpha\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]}{\omega_d}
# \end{align}
# $$

# + [markdown] id="gqM2jennSgC8"
# #### Caso criticamente amortecido ($\alpha=\omega_0\Rightarrow \text{raízes reais e idênticas } s_1=s_2=-\alpha$):
#
# Solução geral da EDO:
#
# $$ \begin{equation} v_{\mathrm{C}}(t) =D_{1} e^{-\alpha(t-t_0)}+D_{2}(t-t_0) e^{-\alpha(t-t_0)}+v_{\mathrm{C}}(\infty) \end{equation}$$
#
# Condições iniciais para $v_{\mathrm{C}}(t)$:
#
# $$
# \begin{align}
# v_{\mathrm{C}}(t_0^+) &=D_1 + v_{\mathrm{C}}(\infty)\\
# \frac{dv_{\mathrm{C}}(t_0^+)}{dt} &=-\alpha D_1 + D_2 = \frac{1}{C} i_{\mathrm{L}}(t_0^+)
# \end{align}
# $$
#
# Solução do sistema em $D_1$ e $D_2$:
#
# $$
# \begin{align}
# D_{1} &=v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty) \\
# D_{2} &= \frac{1}{C} i_{\mathrm{L}}(t_0^+)+\alpha\left[v_{\mathrm{C}}(t_0^+)-v_{\mathrm{C}}(\infty)\right]
# \end{align}
# $$

# + [markdown] id="XdICHxemSgC9"
# ### Problema 2
#
# No circuito da figura a seguir, a chave $ch1$ estive aberta por um longo intervalo de tempo antes de fechar, no instante $t_0=0$s.
#
# <img src="./figures/J12C4.png?raw=1" width="500">
#
# a. Para qual valor de $R_x$ o circuito exibe uma resposta criticamente amortecida para $t\geq 0^+$?\
# b. Considerando que $R_x$ vale exatamente o valor calculado em (a), determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.\
# c. Considerando que $R_x$ vale um décimo do valor calculado em (a), determine a tensão sobre o capacitor $v_C(t)$ para $t\geq 0^+$.
#
# Link para a simulação deste circuito: https://tinyurl.com/yjgkkzhu

# + [markdown] id="YWDjsuKUSgC9"
# Resolução item (b):

# + id="smznWrT9SgC9" outputId="2907ab1d-ccbd-4e5c-faa8-9a52f0db1421"
# Parâmetros do circuito:
R = 
L = 
C = 

# calculando α e ω0
α  = R/(2*L)
ω0 = 1/np.sqrt(L*C)

symdisp('α =', round(α, 2), ' rad/s')
symdisp('ω_0 =', round(ω0, 2), ' rad/s')

# + id="zbr9r5Y7SgC9"
# informações obtidas pela análise do circuito
vC_inf =    # valor final da tensão sobre o capacitor
iL_t0 =   # valor inicial da corrente no indutor
vC_t0 =     # valor inicial da tensão sobre o capacitor

t0 = 0 # instante do chaveamento

# + id="lwRZU5nISgC9"
# raízes da equação característica
s1 = -α
s2 = -α

# define variáveis da solução geral
t, D1, D2 = sp.symbols('t, D1, D2')

# expressão geral da resposta 
vC = D1*sp.exp(s1*(t-t0)) + D2*(t-t0)*sp.exp(s2*(t-t0)) + vC_inf

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + id="7nKTngDpSgC9"
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq()             
eq2 = sp.Eq()  

print('Sistema de equações:')
symdisp('(I): ', round_expr(eq1, 2),' ')
symdisp('(II): ', round_expr(eq2, 2),' ')

# + id="rezufMFESgC9"
# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
D1 = np.array([sol[D1] for sol in soluc])
D2 = np.array([sol[D2] for sol in soluc])

D1 = D1[0]
D2 = D2[0]

print('Solução do sistema:')
symdisp('D_1 =', round(D1, 2), ' V')
symdisp('D_2 =', round(D2, 2), ' V')

# + id="PcKbi4SISgC-"
# expressão geral da resposta 
vC = D1*sp.exp(s1*(t-t0)) + D2*(t-t0)*sp.exp(s2*(t-t0)) + vC_inf

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + id="6awOpy-OSgC-"
# corrente passando pelo indutor
iL = C*sp.diff(vC, t)

symdisp('i_L(t) = ', round_expr(iL,2), 'A')

# + id="YaKhmn-zSgC-"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.05,100)
symplot(t, vC, intervalo, 'vC(t)')

# + id="kLg0UPpeSgC-"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.05,100)
symplot(t, iL, intervalo, 'iL(t)')

# + [markdown] id="nXpmRawHSgC-"
# Resolução item (c):

# + id="xfwHqmGrSgC-"
# Parâmetros do circuito:
R = 65.02
L = 1
C = 100e-6

# calculando α e ω0
α  = R/(2*L)
ω0 = 1/np.sqrt(L*C)

symdisp('α =', round(α, 2), ' rad/s')
symdisp('ω_0 =', round(ω0, 2), ' rad/s')

# + id="_xF0yFqaSgC-"
# informações obtidas pela análise do circuito
vC_inf = 75.84   # valor final da tensão sobre o capacitor
iL_t0 = 0        #  valor inicial da corrente no indutor
vC_t0 = 21.3     # valor inicial da tensão sobre o capacitor

t0 = 0 # instante do chaveamento

# + id="51InQDYkSgC-"
# define a frequência de oscilação amortecida
ωd =np.sqrt(ω0**2-α**2)

symdisp('ω_d =', round(ωd, 2), ' rad/s')

# define variáveis da solução geral
t, B1, B2 = sp.symbols('t, B1, B2')

# expressão geral da resposta subamortecida
vC = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0)) + B2*sp.sin(ωd*(t-t0))) + vC_inf

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + id="TnSgyXKiSgC_"
# define os sistema de equações com as condições iniciais
eq1 = sp.Eq(   B1 + vC_inf, vC_t0)             
eq2 = sp.Eq(-α*B1 + ωd*B2,  iL_t0/C)  

print('Sistema de equações:')
symdisp('(I): ', round_expr(eq1, 2),' ')
symdisp('(II): ', round_expr(eq2, 2),' ')

# + id="XXh4LZeFSgC_"
# resolve o sistema
soluc = sp.solve((eq1, eq2), dict=True)
B1 = np.array([sol[B1] for sol in soluc])
B2 = np.array([sol[B2] for sol in soluc])

B1 = B1[0]
B2 = B2[0]

print('Solução do sistema:')
symdisp('B_1 =', round(B1, 2), ' V')
symdisp('B_2 =', round(B2, 2), ' V')

# + id="T5yUYx7hSgC_"
# expressão geral da resposta subamortecida
vC = sp.exp(-α*(t-t0))*(B1*sp.cos(ωd*(t-t0)) + B2*sp.sin(ωd*(t-t0))) + vC_inf

symdisp('v_C(t) = ', round_expr(vC, 2), ' V')

# + id="SoIi5bVHSgC_"
# corrente passando pelo indutor
iL = C*sp.diff(vC, t)

symdisp('i_L(t) = ', round_expr(iL.simplify(),5), 'A')

# + id="i_p5aM7qSgC_"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.25,100)
symplot(t, vC, intervalo, 'vC(t)')

# + id="l5_dOTOHSgC_"
# plota gráfico da função
intervalo = np.linspace(t0,t0+0.25,100)
symplot(t, iL, intervalo, 'iL(t)')
