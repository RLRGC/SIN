def Calculatrice(a=0,b=0,c=0,addition=False,soustraction=False,multiplication=False,division=False,trinome=False,PremierDegre=False):
    if multiplication:
        return a*b 
    elif addition:
            return a+b 
    elif soustraction:
        return a-b
    elif  division and b!=0:
        return a/b
    elif division and b==0:
        return None
    elif b**2-4*a*c>0 and trinome:
        return ((-b-(b**2-4*a*c)**0.5)/2*a,(-b+(b**2-4*a*c)**0.5)/2*a) 
    elif b**2-4*a*c==0 and trinome:
        return -b/2*a
    elif PremierDegre:
        (c-b)/a
    else:
        return None