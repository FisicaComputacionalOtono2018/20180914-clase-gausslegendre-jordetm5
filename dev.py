
#jorge Dettle Meza Dominguez
#13/09/2018
#derivadas n-simas para el algoritmo de gauss
from sympy import Symbol

def nf(x):
	n=1
	s=x
	while n<x:
		s=s*n
		n=n+1
	return s
def P(x,n):
	return x/((2**n)*nf(n))

n=int(input("introduzca el grado del polinomio : "))

r=float(input("introduzca el valor a evaluar : "))

x=Symbol("x")
y=((x**2)-1)**n
for i in range (0,n):
	y=y.diff(x)

y=float(y.subs(x,r))

print("con el polinomio de grado ",n,", P(",r,")=",P(y,n))

