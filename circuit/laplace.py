# -*- coding: utf-8 -*-
import sympy as sp
import numpy as np
import circuit.utils as cp
from sympy.polys.partfrac import apart
from sympy import oo as infty

# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    coeff = expr.as_numer_denom()    
    c0 = sp.poly(coeff[1].cancel()).coeffs()[0]  
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def expandDenom(expr,  Ndigits):
    s = list(expr.free_symbols)[0]
    coeff = sp.N(adjustCoeff(expr), Ndigits).cancel().as_numer_denom()      
    poles = sp.nroots(coeff[1])        
        
    denom = 1
    for p in poles:
        r =  cp.round_expr(sp.N(p, Ndigits),  Ndigits)
        denom *= (s-r)
                    
    return coeff[0]/denom

# def partFrac(expr, Ndigits):
#     s = list(expr.free_symbols)[0]
#     expr = expr.cancel()
#     expr = apart(adjustCoeff(expr), s, full=True).doit()
#     # for f in expr.args:
#     #     g = sum(adjustCoeff(f) )

#     return sp.N(expr, Ndigits)

def partFrac(F, roundPoles=5):
    """
    Expand a rational function in partial fractions.

    Parameters
    ----------
    F : sympy expression
        The rational function to be expanded.   
    roundPoles : int, optional
        Number of decimal places to round poles (default is 5).

    Returns
    -------
    sympy expression
        The expanded partial fraction form of the input rational function.

    Notes
    -----
    This function expands a rational function in partial fractions. It first
    expands the denominator to identify poles and their multiplicities. Then,
    it constructs the partial fraction decomposition based on the unique poles
    and their multiplicities.

    """
    s = list(F.free_symbols)[0]

    F = adjustCoeff(F)
    num, den = F.as_numer_denom()
    
    n = sp.degree(den)    
    poles = np.round(np.roots(np.asarray(sp.Poly(den.expand(),s).all_coeffs()).astype(np.complex64)), roundPoles)    
    poles = np.concatenate((poles, np.zeros(n-len(poles))))
    
    unique_poles = np.unique(poles)
    multiplicity = np.zeros(unique_poles.shape, dtype=np.int64)
        
    for ind, p in enumerate(unique_poles):
        multiplicity[ind] = np.count_nonzero(poles==p)

    den = 1
    for ind, p in enumerate(unique_poles):
        den *= (s-p)**multiplicity[ind]

    Func = num/den

    Fpf = 0
    
    for ind, p in enumerate(unique_poles):
        if multiplicity[ind] == 1:
            K = (Func*(s-p)).subs({s:p})
            K = K.expand()
            Fpf += K/(s-p)
           
        elif multiplicity[ind] > 1:
            for k in range(multiplicity[ind]):
                K = sp.diff(Func*(s-p)**multiplicity[ind], s, k).subs({s:p})
                K = K.expand()
                Fpf += K/(s-p)**(multiplicity[ind]-k)

    return Fpf

sp.init_printing()

# Laplace transform
def laplaceT(f,t,s):
    return sp.laplace_transform(f, t, s, noconds=True)

# Inverse Laplace transform (via partial fractions)
def invLaplaceT(F, s, t, partialFractions=False, Ndigits=4):
    
    F = F.simplify()

    if partialFractions:
        F = adjustCoeff(F)
        F = partFrac(F, Ndigits)
        F = cp.round_expr(partFrac(F), Ndigits)
        f = sum(sp.re(sp.inverse_laplace_transform(u, s, t)) for u in F.args)
    else:
        try:
            f = sp.inverse_laplace_transform(F, s, t, noconds=True)
        except:
            f = sp.inverse_laplace_transform(F, s, t)

    return cp.round_expr(f,Ndigits)

def tvi(expr):
    s = list(expr.free_symbols)[0]    
    return sp.limit(s*expr, s, infty)

def tvf(expr):
    s = list(expr.free_symbols)[0]    
    return sp.limit(s*expr, s, 0)