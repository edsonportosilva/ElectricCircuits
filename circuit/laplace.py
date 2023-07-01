# -*- coding: utf-8 -*-
import sympy as sp
import circuit.utils as cp
from sympy.polys.partfrac import apart
        
# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    coeff = expr.as_numer_denom()
    c0 = sp.poly(coeff[1].cancel()).coeffs()[0]
    
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def expandDenom(expr,  Ndigits):
    s = sp.symbols('s')
    coeff = sp.N(adjustCoeff(expr), 20).cancel().as_numer_denom()      
    poles = sp.roots(coeff[1], s)        
        
    denom = 1
    for p in poles:
        r =  cp.round_expr(sp.N(p, 20),  Ndigits)
        denom *= (s-r)
                    
    return coeff[0]/denom

def partFrac(expr, Ndigits):
    s = sp.symbols('s')
    expr = expr.cancel()
    expr = apart(adjustCoeff(expr), s, full=True).doit()

    g = sum(adjustCoeff(f) for f in expr.args)
    return sp.N(g, Ndigits)

sp.init_printing()

# Laplace transform
def laplaceT(f,t,s):
    return sp.laplace_transform(f, t, s, noconds=True)

# Inverse Laplace transform (via partial fractions)
def invLaplaceT(F, s, t):
    
    F = F.simplify()
    F = adjustCoeff(F)

    for Ndigits in range(10, 20):
        try:
            F = partFrac(F, Ndigits)
            f = sum(sp.re(sp.inverse_laplace_transform(u, s, t)) for u in F.args)
            break
        except:
            pass    

    return f