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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Tutorial%20Sympy%20-%20Python%20para%20Circuitos%20Eletricos%20I%20.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="KgnjwkrqTLbc"
# # *Tutorial Sympy - Python para Circuitos Elétricos I*
#
# Este notebook contém um guia resumo de como utilizar o pacote **SymPy** do Python para implementar a maior parte das ferramentas matemáticas básicas utilizadas na disciplina de Circuitos Elétricos I.

# + [markdown] toc=true id="NKRw6g3bTLbf"
# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Definindo-expressões-matemáticas" data-toc-modified-id="Definindo-expressões-matemáticas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Definindo expressões matemáticas</a></span></li><li><span><a href="#Calculando-valores-numéricos-de-funções" data-toc-modified-id="Calculando-valores-numéricos-de-funções-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Calculando valores numéricos de funções</a></span></li><li><span><a href="#Arrendondamento-de-valores-numéricos-com-round" data-toc-modified-id="Arrendondamento-de-valores-numéricos-com-round-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Arrendondamento de valores numéricos com <em>round</em></a></span></li><li><span><a href="#Derivadas-utilizando-sp.diff" data-toc-modified-id="Derivadas-utilizando-sp.diff-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Derivadas utilizando <em>sp.diff</em></a></span></li><li><span><a href="#Integrais-definidas-utilizando-sp.integrate" data-toc-modified-id="Integrais-definidas-utilizando-sp.integrate-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Integrais definidas utilizando <em>sp.integrate</em></a></span></li><li><span><a href="#Plotando-gráficos-com-symplot" data-toc-modified-id="Plotando-gráficos-com-symplot-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Plotando gráficos com <em>symplot</em></a></span></li><li><span><a href="#Encontrando-numericamente-um-ponto-de-extremo-(máximo-ou-mínimo)-de-uma-função-com-sp.nsolve" data-toc-modified-id="Encontrando-numericamente-um-ponto-de-extremo-(máximo-ou-mínimo)-de-uma-função-com-sp.nsolve-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Encontrando numericamente um ponto de extremo (máximo ou mínimo) de uma função com <em>sp.nsolve</em></a></span></li><li><span><a href="#Resolvendo-um-sistema-de-equações-lineares-com-sp.solve" data-toc-modified-id="Resolvendo-um-sistema-de-equações-lineares-com-sp.solve-8"><span class="toc-item-num">8&nbsp;&nbsp;</span>Resolvendo um sistema de equações lineares com <em>sp.solve</em></a></span></li></ul></div>

# + id="yGeNv4fpTLbg" outputId="b9a8db6b-b9e7-428e-b127-fb4a8d0692d4" colab={"base_uri": "https://localhost:8080/"}
if 'google.colab' in str(get_ipython()):    
    # ! git clone -b master https://github.com/edsonportosilva/ElectricCircuits
    from os import chdir as cd
    cd('/content/ElectricCircuits/')
    # ! pip install -e .
    
import sympy as sp
import numpy as np
from circuit.utils import symdisp, symplot
from IPython.display import Math, Latex, display

# + [markdown] id="TRc-N0MxTLbh"
# ### Definindo expressões matemáticas

# + id="NN3NZa5mTLbh"
# definindo variável tempo
t = sp.symbols('t', real=True)

# + id="4vL9YbytTLbh" outputId="99d4ef4b-56b4-48bf-bf89-b980312b7a54" colab={"base_uri": "https://localhost:8080/", "height": 81}
i = sp.exp(-t)
v = t*sp.exp(-t)*sp.cos(t)
p = v*i

symdisp('i(t) = ', i, 'A')
symdisp('v(t) = ', v, 'V')
symdisp('p(t) = ', p, 'W')

# + [markdown] id="sVm4xXMgTLbi"
# ```symdisp``` é uma função customizada (disponível no arquivo ```utils.py``` presente no repositório) para mostrar expressões definidas simbolicamente com SymPy. Para utilizar esta função num notebooks qualquer, faz-se necessário que o arquivo ```utils.py``` esteja no mesmo diretório em que o notebook está salvo.

# + id="poXlcAvRTLbj" outputId="eb05f36f-4c73-410d-94bc-74239a84d31a" colab={"base_uri": "https://localhost:8080/"}
help(symdisp)

# + [markdown] id="W59zFdILTLbj"
# ### Calculando valores numéricos de funções

# + id="hKRLzF4FTLbk" outputId="0aa5dbb3-7cd5-4d54-b4e9-8381b3753bed" colab={"base_uri": "https://localhost:8080/", "height": 81}
symdisp('i(2) = ',  i.evalf(subs={t:2}), 'A')
symdisp('v(2) = ',  v.evalf(subs={t:2}), 'V')
symdisp('p(2) = ',  p.evalf(subs={t:2}), 'W')

# + [markdown] id="6IuE9sJkTLbk"
# ###  Arrendondamento de valores numéricos com *round*

# + id="GeweyHZJTLbl" outputId="83fcf422-0ad4-436e-f822-c7dc6178bb97" colab={"base_uri": "https://localhost:8080/", "height": 81}
symdisp('i(2) = ',  round(i.evalf(subs={t:2}),3), 'A')
symdisp('v(2) = ',  round(v.evalf(subs={t:2}),3), 'V')
symdisp('p(2) = ',  round(p.evalf(subs={t:2}),3), 'W')

# + [markdown] id="OvYly-V5TLbl"
# ### Derivadas utilizando *sp.diff*

# + id="3lbUrVvKTLbl" outputId="d550c240-934f-4cff-9bce-b4e20b333cc1" colab={"base_uri": "https://localhost:8080/", "height": 124}
didt = sp.diff(i,t)
dvdt = sp.diff(v,t)
dpdt = sp.diff(p,t)

symdisp('\\frac{ d i(t) }{ dt } =', didt)
symdisp('\\frac{ d v(t) }{ dt } =', dvdt)
symdisp('\\frac{ d p(t) }{ dt } =', dpdt)

# + id="k-SnF68OTLbl" outputId="c05a860a-d28b-4dbc-d11e-b152bf106f88" colab={"base_uri": "https://localhost:8080/", "height": 128}
d2idt2 = sp.diff(i,t,t)
d2vdt2 = sp.diff(v,t,t)
d2pdt2 = sp.diff(p,t,t)

symdisp('\\frac{ d^2 i(t) }{ dt^2 } =', d2idt2)
symdisp('\\frac{ d^2 v(t) }{ dt^2 } =', d2vdt2)
symdisp('\\frac{ d^2 p(t) }{ dt^2 } =', d2pdt2)

# + [markdown] id="kGxXuO2_TLbm"
# ### Integrais definidas utilizando *sp.integrate*

# + id="ga1tccimTLbm" outputId="7566779c-3e31-45b5-8173-1ae12fdebc13" colab={"base_uri": "https://localhost:8080/", "height": 142}
int_i = sp.integrate(i, (t, 0, t))
int_v = sp.integrate(v, (t, 0, t))
int_p = sp.integrate(p, (t, 0, t))

symdisp('\int_{0}^{t} i(u)du =', int_i)
symdisp('\int_{0}^{t} v(u)du =', int_v)
symdisp('\int_{0}^{t} p(u)du =', int_p)

# + id="gK55iMIVTLbm" outputId="6ded263e-bc7b-4f47-8ec8-797b68e6164c" colab={"base_uri": "https://localhost:8080/", "height": 143}
int_i = sp.integrate(i, (t, 0, 1))
int_v = sp.integrate(v, (t, 0, 1))
int_p = sp.integrate(p, (t, 0, 1))

symdisp('\int_{0}^{1} i(u)du =', int_i)
symdisp('\int_{0}^{1} v(u)du =', int_v)
symdisp('\int_{0}^{1} p(u)du =', int_p)

# + id="zwkBuP-UTLbn" outputId="58d06512-de5a-4981-dec0-dd4a0ee344eb" colab={"base_uri": "https://localhost:8080/", "height": 143}
symdisp('\int_{0}^{1} i(u)du =', sp.N(int_i, 2))
symdisp('\int_{0}^{1} v(u)du =', sp.N(int_v, 2))
symdisp('\int_{0}^{1} p(u)du =', sp.N(int_p, 2))

# + [markdown] id="J0nRft6eTLbn"
# ### Plotando gráficos com *symplot*
#
# ```symplot``` é uma função customizada (disponível no arquivo ```utils.py``` presente no repositório) para plotar gráficos de funções definidas simbolicamente com SymPy. Para utilizar esta função num notebooks qualquer, faz-se necessário que o arquivo ```utils.py``` esteja no mesmo diretório em que o notebook está salvo.

# + id="PNByM0JKTLbn" outputId="5d3e9a45-91c8-475d-e430-e9a9fa811d41" colab={"base_uri": "https://localhost:8080/"}
help(symplot)

# + [markdown] id="cJC2Tao0TLbn"
# **Exemplos**:

# + id="0x03ecwKTLbn" outputId="ec7586a5-a297-45c3-aaf5-6308df399620" colab={"base_uri": "https://localhost:8080/", "height": 279}
intervalo = np.arange(0, 5, 0.01)

symplot(t, p, intervalo, 'p(t)')

# + id="FNxJn6k_TLbo" outputId="cf128cdf-100b-41c6-c993-8c8ca81ffb4e" colab={"base_uri": "https://localhost:8080/", "height": 279}
symplot(t, [v, i, p], intervalo, ['v(t)','i(t)','p(t)'])

# + [markdown] id="ceLLxmaMTLbo"
# ### Encontrando numericamente um ponto de extremo (máximo ou mínimo) de uma função com *sp.nsolve*

# + id="tw1KKHzaTLbo" outputId="0da3ce3a-2308-4afd-e68a-8e18836bf995" colab={"base_uri": "https://localhost:8080/", "height": 98}
# define a equação dp(t)/dt = 0
eq = sp.Eq(sp.diff(p, t), 0)   

# encontra numericamente o valor de t para o qual dp(t)/dt = 0, no intervalo (0 a 1)
text = sp.nsolve(eq, t, (0 , 1), solver='bisect') # método da bisseção

pext = p.evalf(subs={t:text})  # calcula o valor de p(t) para t=text

d2 = sp.diff(p, t, t)  # calcula derivada segunda de p(t)

sinal_d2 = sp.sign(d2.evalf(subs={t:text})) # verifica sinal da derivada segunda em t=text

if sinal_d2 > 0:
    print('sinal da derivada segunda: positivo (ponto de extremo é um mínimo)')
elif sinal_d2 < 0:
    print('sinal da derivada segunda: negativo (ponto de extremo é um máximo)')
    
symdisp('p(t) = ', p)
symdisp('t_{ext} =', round(text,3))    
symdisp('p_{ext} =', round(pext,3))

# + [markdown] id="JJum2ShMTLbp"
# ### Resolvendo um sistema de equações lineares com *sp.solve*

# + id="Ztxu-bKITLbp" outputId="cae5e9c5-fde3-4ea2-d25d-f42b21b5a61a" colab={"base_uri": "https://localhost:8080/", "height": 180}
# define as N variáveis desconhecidas
x, y, z = sp.symbols('x, y, z')

# define os sistema de N equações
eq1 = sp.Eq(x   + y + z, 10)             
eq2 = sp.Eq(2*x - y + z, 1)  
eq3 = sp.Eq(5*x - 2*y + 3*z, 5)  

print('Sistema de equações lineares:')
display(eq1, eq2, eq3) 

# resolve o sistema
soluc = sp.solve((eq1, eq2, eq3), dict=True)
soluc = soluc[0]

x = soluc[x]
y = soluc[y]
z = soluc[z]

print('Solução do sistema:')
symdisp('x =', x)
symdisp('y =', y)
symdisp('z =', z)
