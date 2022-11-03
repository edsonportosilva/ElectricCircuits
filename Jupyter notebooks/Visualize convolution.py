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
# <a href="https://colab.research.google.com/github/edsonportosilva/ElectricCircuits/blob/master/Jupyter%20notebooks/Visualize%20convolution.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + colab={"base_uri": "https://localhost:8080/"} id="cfMZxhRhFnde" outputId="810edf84-83f2-4a42-e308-0d9fb4ed58b7"
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
    # ! sudo apt update
    # ! sudo apt install imagemagick
    from os import chdir as cd
    cd('/content/ElectricCircuits/Jupyter notebooks')


# + id="iVVNJ8qSGNb8"
   

# + id="ZotYJEhnFndc"
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
from utils import round_expr, symdisp, symplot, genConvGIF

# temp workaround
import warnings
from matplotlib import MatplotlibDeprecationWarning
warnings.filterwarnings('ignore', category=MatplotlibDeprecationWarning)

plt.rcParams['figure.figsize'] = 6, 4
plt.rcParams['legend.fontsize'] = 13
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['axes.grid'] = False

# + [markdown] id="elvm0aQOFndf"
# # Visualize the convolution between two real functions defined with Sympy
#
#

# + [markdown] id="7m81rjNJFndg"
# **Define time variable in sympy**

# + id="ylaoumHgFndh"
t = sp.symbols('t', real=True)

# + [markdown] id="laoZX7j6Fndh"
# **Define functions:** $x(t)$, $h(t)$

# + colab={"base_uri": "https://localhost:8080/", "height": 119} id="JDzeVIMZFndi" outputId="39633985-fc77-40e0-a7d3-39d84838f7bc"
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (1, (t>=2)))

h = sp.Piecewise((0, t<0),                   
                 (5*sp.exp(-t)*sp.sin(5*t), (t>=0)))

symdisp('x(t) = ', round_expr(x,2))
symdisp('h(t) = ', round_expr(h,2))

# + colab={"base_uri": "https://localhost:8080/", "height": 283} id="Ot9feSTBFndi" outputId="00cd6897-1686-46d2-8735-d33a71a72263"
interval = np.arange(-2, 8, 0.01)
symplot(t, [x, h], interval, ['x(t)','h(t)'])

# + [markdown] id="7eOUb9ZHFndj"
# **Visualize convolution:** $y(t) = h(t)\ast x(t) =\int_{-\infty}^{\infty} h(\tau) x(t-\tau) d\tau$

# + colab={"base_uri": "https://localhost:8080/", "height": 350} id="jRsIpdN-Fndj" outputId="a37939db-539a-49ed-f4d9-af0f68bc98b8"
ti = -6  # animation starts at this time
tf = 8   # animation ends at this time
τ_max = 8

delay = np.arange(-τ_max, τ_max, 0.01) # must be symmetric w.r.t 0

figName  = './figures/convolutionFig1.gif'

genConvGIF(x, h, t, delay, ti, tf,\
           figName, xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)','y(t)'],\
           fram=50, inter=150, plotConv=True)

Image('./figures/convolutionFig1.gif', width=500)

# + [markdown] id="8kxLbdiQFndk"
# **Define functions:** $x(t)$, $h(t)$

# + colab={"base_uri": "https://localhost:8080/", "height": 141} id="vLlsHINEFndk" outputId="cee55db9-f2f0-4ce6-c84d-12394b014aca"
x = sp.Piecewise((0, t<0), 
                  (1, (t>=0)&(t<2)), 
                  (0, (t>=2)))

h = sp.Piecewise((0, t<0),                   
                 (2*sp.exp(-2*t), (t>=0)))

symdisp('x(t) = ', round_expr(x,2))
symdisp('h(t) = ', round_expr(h,2))

# + colab={"base_uri": "https://localhost:8080/", "height": 279} id="IyerHwEBFndl" outputId="9f7ac300-c5b9-49fa-c3fc-0bbf02b49b21"
interval = np.arange(-2, 8, 0.01)
symplot(t, [x, h], interval, ['x(t)','h(t)'])

# + [markdown] id="JdkVkmfLFndl"
# **Visualize convolution:** $y(t) = h(t)\ast x(t) =\int_{-\infty}^{\infty} h(\tau) x(t-\tau) d\tau$

# + id="-RmtMXhSFndl"
ti = -6 # animation starts at this time
tf = 8  # animation end at this time
τ_max = 8

atraso = np.arange(-τ_max, τ_max, 0.01) # must be symmetric w.r.t 0

figName  = './figures/convolutionFig2.gif'

genConvGIF(x, h, t, delay, ti, tf,\
           figName, xlabel= 'τ[s]', ylabel=['h(τ)', 'x(t-τ)','y(t)'],\
           fram=50, inter=150, plotConv=True)

Image('./figures/convolutionFig2.gif', width=500)
