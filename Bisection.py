


def bisection(f,a,b,tol):
    if f(a)==0:
        return a
    if f(b)==0:
        return b
    a0=a
    b0=b
    ## Falls auf dem anfänglichen Intervall kein Bisektionsverfahren möglich ist
    ## (Vorzeichenwechsel), verkleinern wir das Intervall, um es zu ermöglichen
    if f(a)*f(b)>0:
        x=(b-a)
        c=a
        for k in range(1,101):
            c=c+x/100
            if f(c)*f(b)<0:
                return bisection(f,c,b,tol)
            k=k+1
            if k==100:
                print("Bisektion nix gut")
                return None
    ## Eigentliches Bisektionsverfahren
    while abs(b0-a0)>tol or f(a0)>tol:
        x=(a0+b0)/2
        if f(x)==0:
            return x
        if f(a0)*f(x)<0:
            b0=x
        else:
            a0=x
    return (a0+b0)/2
