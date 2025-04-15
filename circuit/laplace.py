# -*- coding: utf-8 -*-
import sympy as sp
import numpy as np
import circuit.utils as cp
from sympy.polys.partfrac import apart
from sympy import oo as infty

# funções para auxílio na expansão em frações parciais
def adjustCoeff(expr):    
    """
    Adjusts the coefficients of a given symbolic expression to ensure that the
    leading coefficient of the denominator is 1. This is useful for simplifying
    the expression before performing operations like partial fraction decomposition.

    Parameters
    ----------
    expr : sympy.Expr
        The symbolic expression to be adjusted. It is expected to be a rational
        function of a single variable (e.g., 's').
    
    Returns
    -------
    sympy.Expr
        The adjusted expression with the leading coefficient of the denominator set to 1.
    """
    coeff = expr.as_numer_denom() 
    try:
        c0 = sp.poly(coeff[1].cancel()).coeffs()[0]  
    except:
        c0 = coeff[1]
        
    return (coeff[0].cancel()/c0)/(coeff[1].cancel()/c0)

def expandDenom(expr,  Ndigits):
    """
    Expands the denominator and numerator of a given symbolic expression into 
    their factored forms based on the poles and zeros of the expression.

    Parameters
    ----------  
    expr : sympy.Expr
        The symbolic expression to be expanded. It is expected to be a 
        rational function of a single variable (e.g., 's').
    Ndigits : int
        The number of significant digits to use when rounding the poles 
        and zeros of the expression.

    Returns
    -------
        Sympy expression
        The expanded expression in terms of the poles and zeros of the
        original expression.
    """
    s = list(expr.free_symbols)[0]
    coeff = sp.N(adjustCoeff(expr), Ndigits).cancel().as_numer_denom()

    try:      
        poles = sp.nroots(coeff[1])
    except:
        poles = []

    try:
        zeros = sp.nroots(coeff[0])        
    except:
        zeros = []

    try:
        b0 = sp.poly(coeff[0].cancel()).coeffs()[0]
    except:
        b0 = coeff[0]

    denom = 1
    numerator = 1
    for z in zeros:
        r =  cp.round_expr(sp.N(z, Ndigits),  Ndigits)
        numerator *= (s-r)

    for p in poles:
        r =  cp.round_expr(sp.N(p, Ndigits),  Ndigits)
        denom *= (s-r)
                    
    return b0*numerator/denom

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
    """
    Computes the Laplace transform of a given function.

    Parameters:
    -----------
    f : sympy.Expr
        The function to be transformed.
    t : sympy.Symbol
        The time domain variable.
    s : sympy.Symbol
        The Laplace domain variable.
    Returns:
    --------
    sympy.Expr
        The Laplace-transformed function.    
    """    
    return sp.laplace_transform(f, t, s, noconds=True)

# Inverse Laplace transform (via partial fractions)
def invLaplaceT(F, s, t, partialFractions=False, Ndigits=10):
    """
    Computes the inverse Laplace transform of a given function.
    Parameters:
    -----------
    F : sympy.Expr
        The Laplace-transformed function to be inverted.
    s : sympy.Symbol
        The Laplace domain variable.
    t : sympy.Symbol
        The time domain variable.
    partialFractions : bool, optional
        If True, performs partial fraction decomposition on the input function
        before computing the inverse Laplace transform. Default is False.
    Ndigits : int, optional
        The number of significant digits to round the result to. Default is 10.
    Returns:
    --------
    sympy.Expr
        The time-domain function obtained by applying the inverse Laplace transform.
    Notes:
    ------
    - If `partialFractions` is True, the function applies partial fraction decomposition
      and simplifies the coefficients before computing the inverse Laplace transform.
    - If the inverse Laplace transform cannot be computed directly, the function attempts
      to compute it with conditions.
    - The result is rounded to the specified number of significant digits using `cp.round_expr`.
    Raises:
    -------
    Exception
        If the inverse Laplace transform computation fails.
    """
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