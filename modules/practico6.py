import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	datos = {0:18, 1:37, 2:42, 3:30, 4:13, 5:7, 6:2, 7:1}
	mean = E(datos)
	var = V(datos)/150
	print("a) un estimador insesgado es X barra. su valor es:", "%.3f"%mean)
	error = math.sqrt(var)
	print("b) desvio del estimador:", "%.3f"%error) 
	print("   error estandar estimado:", "%.3f"%error) 

def ej2():

	X = [5.9, 7.2, 7.3, 6.3, 8.1, 6.8, 7.0, 7.6, 6.8, 6.5, 7.0, 6.3, 7.9, 9.0, 8.2, 8.7, 7.8, 9.7, 7.4, 7.7]
	Y = [6.1, 5.8, 7.8, 7.1, 7.2, 9.2, 6.6, 8.3, 7.0, 8.3, 7.8, 8.1, 7.4, 8.5, 8.9, 9.8, 9.7, 14.1, 12.6, 11.2]

	e1 = E(X)
	e2 = E(Y)
	d1 = math.sqrt(V(X)/20)
	d2 = math.sqrt(V(Y)/20)
	print("a) e1 =", "%.3f"%e1)
	print("   e2 =", "%.3f"%e2)
	print("   d1 =", "%.3f"%d1)
	print("   d2 =", "%.3f"%d2)

	diff = e1 - e2
	print("b) E(X-Y) es un estimador insesgado.")
	print("   E(X-Y) =", "%.3f"%diff) 

	error = d1 + d2
	varb = error**2
	print("c) V(X-Y) =", "%.3f"%varb)
	print("    error =", "%.3f"%error)

	print("d)", "%.3f"%(d1/d2))

def ej3():
	X1, fda1, e1, v1, d1 = binomial_dist(200, 127/200)
	X2, fda2, e2, v2, d2 = binomial_dist(200, 176/200)
	prob = (E(X1) - E(X2))/200
	var = V(X1)/200**2 + V(X2)/200**2
	error = math.sqrt(var)
	print("c)valor estimado:", "%.3f"%prob)
	print("d) error estandar estimado:", "%.3f"%error) 

def ej6():
	ans = 0