import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	print("a)", "%.3f"%z_prob(a=-2.81, b=2.81))

	est = -2.50
	while z_prob(a=-est, b=est) < 0.997:
		est += 0.001
	
	print("b)", "%.3f"%est)
	e1 = (114.4 + 115.6)/2
	e2 = (114.1 + 115.9)/2
	print("i) μ1 =", e1, "y μ2 =", e2) 
	print("ii) el segundo.")

def ej2():
	izq = (58.3 - 1.96 * 3/5)
	der = (58.3 + 1.96 * 3/5)
	ic1 = ("%.3f"%izq, "%.3f"%der)
	longA = der - izq
	print("a)", ic1)
	izq = (58.3 - 1.96 * 3/10)
	der = (58.3 + 1.96 * 3/10)
	longB = der - izq
	ic2 = ("%.3f"%izq, "%.3f"%der)
	print("b)", ic2)
	print("   longitudB =", "%.2f"%(longB/longA), "* longitudA")

	izq = (58.3 - 2.575 * 3/10)
	der = (58.3 + 2.575 * 3/10)
	ic3 = ("%.3f"%izq, "%.3f"%der)
	longC = der - izq
	print("c)", ic3)
	print("   longitudC =", "%.2f"%(longC/longB), "* longitudB")

	n = ic_getN(58.3, 3, 1, 0.99)
	print("d) n >=", n)

def ej3():
	ica, _ = int_conf(1.028, 0.163, 69, 0.95)
	print("a)", ica)

	n = ic_getN(1.028, 0.16, 0.05, 0.95)
	print("b) n >=", n)

def ej4():
	e = 133
	p = 133/539
	v = p * (1-p)
	d = math.sqrt(v)
	ica, _ = int_conf(p, d, 539, 0.98)
	print("a)", ica)

	n = ic_getN(p, d, 0.10, 0.98)
	print("b) n >=", n)

def ej5():
	ica, _ = int_conf(188.0, 7.2, 40, .98)
	icva1, _ = ic_var(7.2, 40, 0.95)
	print("a)")
	print("   i)", ica)
	print("   ii)", icva1)

	icb, _ = ic_mean(188.0, 7.2, 9, .95)
	icva2, _ = ic_var(7.2, 9, 0.95)
	print("b)")
	print("   i)", icb)
	print("   ii)", icva2)
