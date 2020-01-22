import math
from scipy import integrate
from pynverse import inversefunc
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
	leftii = e - 2*math.sqrt(v)
	rightii = e + 2*math.sqrt(v)
	fgii = integrate.quad(f, max(a,leftii), min(b,rightii))[0]
	print("e)", "%.3f"%fgi, "y", "%.3f"%fgii)

def ej4():
	f, std = normal_dist(80,100)
	ans = integrate.quad(f, -math.inf, 100)[0]
	print("P(X < 100) =", "%.3f"%ans)
	ans = integrate.quad(std, -math.inf, 2)[0]
	print("P(X < 100) =", "%.3f"%ans)
	ans = integrate.quad(f, 65, 100)[0]
	print("P(65 < X < 100) =", "%.3f"%ans)
	ans = integrate.quad(f, 70, math.inf)[0] 
	print("P(70 < X) =", "%.3f"%ans)
	ans = integrate.quad(f, 85, 95)[0]
	print("P(85 < X 95) =", "%.3f"%ans)
	ans = integrate.quad(f, 70, 90)[0]
	print("P(|X-80| < 10) =", "%.3f"%ans)

def ej5():
	e = 8.8
	v = 2.8
	d = math.sqrt(v)
	f, std = normal_dist(8.8, 2.8)
	std_a = (10-e)/d	
	ansi = integrate.quad(f, -math.inf, 10)[0]
	ansii = integrate.quad(std, std_a, math.inf)[0]
	#solo queria probar que eran lo mismo
	print("a) P(X < 10) =","%.3f"%ansi, "y P(10 < X) =", "%.3f"%ansii)
	std_b = (5-e)/d
	ans = integrate.quad(std, std_b, std_a)[0]
	print("b) P(5 < X < 10) =", "%.3f"%ans)
	print("c) c =", "%.3f"%(2.33*d)) 
	exito = ans
	prob_0arboles = (1-exito)**5
	print("d)", "%.3f"%(1-prob_0arboles))
	
def ej8():
	f, fda, e, v = exp_dist(0.01386)
	d = math.sqrt(v)
	print("a) P(X < 100) =","%.3f"%fda(100))
	print("   P(X < 100) =","%.3f"%fda(200))
	print("   P(100 < X < 200) =","%.3f"%(fda(200)-fda(100)))
	print("b) P(e+d*2 < X) =", "%.3f"%(1 - fda(e+d*2)))
	print("c) mediana(X) =", "%.3f"%(inversefunc(fda,0.5)))