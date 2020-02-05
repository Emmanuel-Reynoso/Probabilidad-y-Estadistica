import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	print("a) R1, estamos haciendo una prueba bilateral")
	print("b) X~B(25, 0.5)")
	pt, ct, e, _, _ = binomial_dist(25, 0.5)
	err1 = ct[7] + 1 - ct[18]
	err2 = ct[18] - ct[7]
	print("   err1 =", "%.3f"%err1)
	print("c)")
	pt, ct, _, _, _ = binomial_dist(25, 0.3)
	err2 = ct[18] - ct[7]
	print("   if p = 0.3: err2 =", "%.3f"%err2)
	pt, ct, _,_,_ = binomial_dist(25, 0.4)
	err2 = ct[18] - ct[7]
	print("   if p = 0.4: err2 =", "%.3f"%err2)
	pt, ct, _,_,_ = binomial_dist(25, 0.6)
	err2 = ct[18] - ct[7]
	print("   if p = 0.6: err2 =", "%.3f"%err2)
	
	pt, ct, _,_,_ = binomial_dist(25, 0.7)
	err2 = ct[18] - ct[7]
	print("   if p = 0.7: err2 =", "%.3f"%err2)
	
	print("d)")
	print("   Como 6 pertenece a la región de rechazo, rechazamos la hipótesis nula.")

def ej2():
	print("a) Hipotesis alternativa del tipo bilateral:")
	print("   H0: μ = 10")
	print("   Ha: μ != 10")
	print("   estadístico de prueba: Z")
	izq = 9.8968  
	der = 10.1032
	x = 10
	e = 10
	d = 0.2
	n = 25
	err1 = ph_mean_err1(e,d,n,izq,der,case='A', hip='equal')
	print("b) P(revisar en vano) =", "%.4f"%err1)
	e = 10.1
	err2 = ph_mean_err2(e,d,n,x,err1,case='A', hip='equal')
	print("c) P(rechazar revision con μ = 10.1) =", "%.3f"%err2)
	e = 9.8
	err2 = ph_mean_err2(e,d,n,x, err1,case='A', hip='equal')
	print("   P(rechazar revision con μ = 9.8) =", "%.3f"%err2)

	zde = math.sqrt(n) * (der-10)/d
	print("d) c =", "%.2f"%zde)

def ej3():
	ans = z_prob(a=1.88)
	print("a)", "%.2f"%ans)
	ans = z_prob(b=-2.75)
	print("b)", "%.3f"%ans)
	ans = 1 - z_prob(a=-2.88, b=2.88)
	print("c)", "%.3f"%ans)

def ej4():
	x = 94.32
	d = 1.2
	n = 16
	e = 95

	a = 0.01
	if ph_mean_result(x,d,n,94,a,hip='equal', case='A'):
		print("a) No se rechaza la hopótesis nula porque x no cayó en el RR")
	x = 94
	b = ph_mean_err2(x, d, n, e, a, hip='equal', case='A')
	print("b)", "%.3f"%b)
	b = 0.1
	c = ph_mean_n(x,d,e,a, b, hip='equal')
	print("c)", "%.3f"%c)
