import math
from scipy import integrate
from definiciones import *

def ej1():

	f = lambda x:x/2
	ansi = integrate.quad(f, 0, 1)
	print("i) P(X<=1) =", ansi[0])
	ansii = integrate.quad(f, 0.5, 1.5)
	print("ii) P(0,5<=X<=1,5) =", ansii[0])
	ansiii = integrate.quad(f, 1.5, 2)
	print("iii) P(1,5 < X) =", ansiii[0])

	print("b) if x < 0, F(x)= 0")
	print("   if x < 2, F(x)= x**2 / 4")
	print("   if 2 < x, F(x)= 1")

	print("c) E(X) =","%.3f"%E(f, 0, 2), ", V(X) =", "%.3f"%V(f, 0, 2),", σ(X) =", "%.3f"%desvio(f, 0, 2))

	print("d)", E(lambda x: f(x**2), 0, 2))