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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # *Tutorial Sympy - Python para Circuitos Elétricos I*

# + [markdown] toc=true
# <h1>Sumário<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Definindo-expressões-matemáticas" data-toc-modified-id="Definindo-expressões-matemáticas-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Definindo expressões matemáticas</a></span></li><li><span><a href="#Calculando-valores-numéricos-de-funções" data-toc-modified-id="Calculando-valores-numéricos-de-funções-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Calculando valores numéricos de funções</a></span></li><li><span><a href="#Arrendondamento-de-valores-numéricos" data-toc-modified-id="Arrendondamento-de-valores-numéricos-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Arrendondamento de valores numéricos</a></span></li><li><span><a href="#Derivadas-utilizando-sp.diff" data-toc-modified-id="Derivadas-utilizando-sp.diff-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Derivadas utilizando <em>sp.diff</em></a></span></li><li><span><a href="#Integrais-definidas-utilizando-sp.integrate" data-toc-modified-id="Integrais-definidas-utilizando-sp.integrate-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Integrais definidas utilizando <em>sp.integrate</em></a></span></li><li><span><a href="#Plotando-gráficos-com-symplot" data-toc-modified-id="Plotando-gráficos-com-symplot-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Plotando gráficos com symplot</a></span></li><li><span><a href="#Encontrando-numericamente-um-ponto-de-extremo-(máximo-ou-mínimo)-de-uma-função-com-sp.nsolve" data-toc-modified-id="Encontrando-numericamente-um-ponto-de-extremo-(máximo-ou-mínimo)-de-uma-função-com-sp.nsolve-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Encontrando numericamente um ponto de extremo (máximo ou mínimo) de uma função com <em>sp.nsolve</em></a></span></li></ul></div>
# -

import sympy as sp
import numpy as np
from utils import symdisp, symplot
from IPython.display import Math, Latex

# ### Definindo expressões matemáticas

# definindo variável tempo
t = sp.symbols('t', real=True)

# +
i = sp.exp(-t)
v = t*sp.exp(-t)*sp.cos(t)
p = v*i

symdisp('i(t) = ', i)
symdisp('v(t) = ', v)
symdisp('p(t) = ', p)
# -

# ### Calculando valores numéricos de funções

symdisp('i(2) = ',  i.evalf(subs={t:2}) )
symdisp('v(2) = ',  v.evalf(subs={t:2}) )
symdisp('p(2) = ',  p.evalf(subs={t:2}) )

# ###  Arrendondamento de valores numéricos

symdisp('i(2) = ',  round(i.evalf(subs={t:2}),3) )
symdisp('v(2) = ',  round(v.evalf(subs={t:2}),3) )
symdisp('p(2) = ',  round(p.evalf(subs={t:2}),3) )

# ### Derivadas utilizando *sp.diff*

symdisp('\\frac{ d i(t) }{ dt } =', sp.diff(i,t))
symdisp('\\frac{ d v(t) }{ dt } =', sp.diff(v,t))
symdisp('\\frac{ d p(t) }{ dt } =', sp.diff(p,t))

symdisp('\\frac{ d^2 i(t) }{ dt^2 } =', sp.diff(i,t,t))
symdisp('\\frac{ d^2 v(t) }{ dt^2 } =', sp.diff(v,t,t))
symdisp('\\frac{ d^2 p(t) }{ dt^2 } =', sp.diff(p,t,t))

# ### Integrais definidas utilizando *sp.integrate*

symdisp('\int_{0}^{t} i(u)du =', sp.integrate(i, (t, 0, t)))
symdisp('\int_{0}^{t} v(u)du =', sp.integrate(v, (t, 0, t)))
symdisp('\int_{0}^{t} p(u)du =', sp.integrate(p, (t, 0, t)))

# ### Plotando gráficos com symplot

# +
intervalo = np.arange(0, 5, 0.01)

symplot(t, p, intervalo, 'p(t)')
# -

symplot(t, [v, i, p], intervalo, ['v(t)','i(t)','p(t)'])

# ### Encontrando numericamente um ponto de extremo (máximo ou mínimo) de uma função com *sp.nsolve*

# +
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
