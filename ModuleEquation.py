"""
Le module Equation a été developpé par gaelBZH et RLRGC.
Il comporte des fonctions servant à résoudre des équations du premier et du second degré.
Pour le second degré, il est possible de calculer les racines dans ℂ ou dans ℝ.
"""

def degré1(a,b,c=0):
    """Equation de Type ax+b=c ou ax+b=0 si dans le cas d'un binome (a,b). Prend en argument des flottants. Renvoie x."""
    return (c-b)/a

def delta(a,b,c):
    """Equation de Type ax²+bx+c=0, ensemble ℂ. Prend en arguments des flottants. Renvoie Δ = b²-4ac."""
    return b**2-4*a*c

def degré2(a,b,c):
    """Equation de Type ax²+bx+c=0, ensemble ℝ. Prend en arguments des flottants. Renvoie x ou (x1,x2) ou None selon le nombre de racines réelles."""
    return ((-b-(delta(a,b,c))**0.5)/2*a,(-b+(delta(a,b,c))**0.5)/2*a) if delta(a,b,c)>0 else -b/2*a if delta(a,b,c)==0 else None
    
def degré2Complexe(a,b,c):
    """Equation de Type ax²+bx+c=0, ensemble ℂ. Prend en arguments des flottants. Renvoie x ou (x1,x2) ou (z1,z2) selon le nombre de racines réelles ou complexes."""
    return ((-b-(delta(a,b,c))**0.5)/2*a,(-b+(delta(a,b,c))**0.5)/2*a) if delta(a,b,c)>0 else -b/2*a if delta(a,b,c)==0 else (f"({-b}-i(√({-(delta(a,b,c))})))/{2*a}",f"({-b}+i(√({-(delta(a,b,c))})))/{2*a}")

def factoriser(a,b,c):
    """Fonction f(x)=ax²+bx+c=0, ∀x∈ℝ. Prend en arguments des flottants. Renvoie un texte de la forme factorisée a(x–x1)(x–x2) ou a(x–x0)² où x0,x1,x2 sont les racines réelles ou None selon le nombre de racines réelles."""
    return f"{a}(x-{(-b-(delta(a,b,c))**0.5)/(2*a)})(x-{(-b+(delta(a,b,c))**0.5)/(2*a)})" if delta(a,b,c)>0 else f"{a}(x-{(-b-(delta(a,b,c))**0.5)/(2*a)})²" if delta(a,b,c)==0 else None

def canonique (a,b,c):
    """Fonction f(x)=ax²+bx+c=0, ∀x∈ℝ. Prend en arguments des flottants. Renvoie un texte de la forme canonique a(x-α)²+β où α=-b/2a et β=f(α)"""
    return f"{a}(x-{(-b)/(2*a)}²+{a*(-b)/(2*a)**2+b*(-b)/(2*a)+c})"