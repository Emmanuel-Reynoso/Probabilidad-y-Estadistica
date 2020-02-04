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

	n = 25
	longD = 2
	while 1 < longD: 
		izq = (58.3 - 2.575 * 3/math.sqrt(n))
		der = (58.3 + 2.575 * 3/math.sqrt(n))
		longD = der - izq
		n += 1
	print("d)", n)

def ej3():
	ica, _ = int_conf(1.028, 0.163, 69, 0.95)
	print("a)", ica)

	n = 50
	_, lon = int_conf(1.028, 0.16, n, 0.95)
	while 0.05 <= lon:
		n += 1
		_, lon = int_conf(1.028, 0.16, n, 0.95)
	print("b) n =", n)