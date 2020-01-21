import math
from scipy import integrate
from definiciones import *

def ej1():

	f = lambda x:x/2
	ansi = integrate.quad(f, 0, 1)
	print("i) P(X <= 1) =", ansi[0])
	ansii = integrate.quad(f, 0.5, 1.5)
	print("ii) P(0,5 <= X <= 1,5) =", ansii[0])
	ansiii = integrate.quad(f, 1.5, 2)
	print("iii) P(1,5 < X) =", ansiii[0])

	print("b) if x < 0, F(x)= 0")
	print("   if x < 2, F(x)= x**2 / 4")
	print("   if 2 < x, F(x)= 1")

	print("c) E(X) =","%.3f"%E(f, 0, 2, True), ", V(X) =", "%.3f"%V(f, 0, 2, True),", σ(X) =", "%.3f"%desvio(f, 0, 2, True))

	print("d)", E(lambda x: f(x**2), 0, 2, True))

def ej2():
	fk = lambda x:x**2
	ansa = integrate.quad(fk, 0, 2)
	print("a) ", "%.3f"%(1/ansa[0]))

	f = lambda x:x**2 * 3/8
	fda = integrate.quad(f, 0, 2)

	fb = integrate.quad(f, 0, 1)
	print("b) ", "%.3f"%fb[0])
	
	fc = integrate.quad(f, 1, 1.5)
	print("c) ", "%.3f"%fc[0])
	
	print("d) if x < 0, F(x)= 0")
	print("   if x < 2, F(x)= x**3 / 8")
	print("   if 2 < x, F(x)= 1")

	print("e) 0.75 = x**3 / 8, por lo tanto x =","%.3f"% (0.75*8)**(1/3))

	print("f) E(X) =", "%.3f"%E(f,0,2,True),"y σ(x) =", "%.3f"%desvio(f,0,2,True))
	left = E(f,0,2,True) - desvio(f,0,2,True)
	right = E(f,0,2,True) + desvio(f,0,2,True)
	fg = integrate.quad(f, left, right)
	print("g)", "%.3f"%fg[0])

def ej3():
	print("a)-fd----")
	print("   if x < 0 or x < 2, f(x)= 0")
	print("   if x < 2, f(x)= x**3 / 8")
	print("---fda---")
	print("   if x < 0, F(x)= 0")
	print("   if x < 2, F(x)= x**3 / 8")
	print("   if 2 < x, F(x)= 1")
	a = 25
	b = 35
	f, fda, e, v = uniform_dist(a,b)

	ansb = integrate.quad(f, 33, b)[0]
	print("b) ", "%.3f"%ansb)

	ansc = integrate.quad(f, 30, 32)[0]
	print("c) ", "%.3f"%ansc)

	print("d) E(X) =", "%.3f"%e,"y V(X) =", "%.3f"%v)
	lefti = e - math.sqrt(v)
	righti = e + math.sqrt(v)
	fgi = integrate.quad(f, lefti, righti)[0]
	print("e)", "%.3f"%fgi)
	leftii = e - 2*math.sqrt(v)
	rightii = e + 2*math.sqrt(v)
	fgii = integrate.quad(f, max(a,leftii), min(b,rightii))[0]
	print("--", "%.3f"%fgii)