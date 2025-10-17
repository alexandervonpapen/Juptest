    ### gibt einen Näherungswert der Ableitung von f in x 
    ### per zentralem Differenzenquotient

def diffpoint(f,x):
    h=1e-5
    a=(f(x+h)-f(x-h))/h
    return a/2
