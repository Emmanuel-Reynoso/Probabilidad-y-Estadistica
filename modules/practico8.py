import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	print("a) R1, estamos haciendo una prueba bilateral")
	print("b) X~B(25, 0.5)")
	pt, ct, e, v, d = binomial_dist(25, 0.5)
	err1 = ct[7] + 1 - ct[18]
	err2 = ct[18] - ct[7]
	print("   err1 =", "%.3f"%err1)

	print("c)")
	pt, ct, e, v, d = binomial_dist(25, 0.3)
	err2 = ct[18] - ct[7]
	print("   if p = 0.3: err2 =", "%.3f"%err2)
	pt, ct, e, v, d = binomial_dist(25, 0.4)
	err2 = ct[18] - ct[7]
	print("   if p = 0.4: err2 =", "%.3f"%err2)
	pt, ct, e, v, d = binomial_dist(25, 0.6)
	err2 = ct[18] - ct[7]
	print("   if p = 0.6: err2 =", "%.3f"%err2)
	pt, ct, e, v, d = binomial_dist(25, 0.7)
	err2 = ct[18] - ct[7]
	print("   if p = 0.7: err2 =", "%.3f"%err2)
	
	print("d) Como 6 pertenece a la región de rechazo, rechazamos la hipótesis nula.")

def ej2():
	print("a) Hipotesis alternativa del tipo bilateral")
	izq = 9.8968  
	der = 10.1032
	e = 10
	d = 0.2
	n = 25
	err1 = ph_mean_err1(e,d,n,izq,der,case='A', hip='equal')
	print("b) P(revisar en vano) =", "%.2f"%err1)
	e = 10.1
	err1 = ph_mean_err1(e,d,n,izq,der,case='A', hip='equal')
	print("c) P(revisar en vano con μ = 10.1) =", "%.3f"%err1)
	e = 9.8
	err1 = ph_mean_err1(e,d,n,izq,der,case='A', hip='equal')
	print("   P(revisar en vano con μ = 9.8) =", "%.3f"%err1)

	
	zde = math.sqrt(n) * (der-10)/d
	print("d) c =", "%.2f"%zde)