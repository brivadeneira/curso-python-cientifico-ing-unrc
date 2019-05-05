
def raices(a, b=0, c=0):
    """dados los coeficientes, encuentra los valores de x tal que ax^2 + bx + c = 0"""

    discriminante = (b**2 - 4*a*c)**0.5
    x1 = (-b + discriminante)/(2*a)
    x2 = (-b - discriminante)/(2*a)
    return (x1, x2)
    
       