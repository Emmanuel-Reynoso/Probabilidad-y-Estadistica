import matplotlib.pylab as plt
import numpy as np
import math

def media(x):
	return sum(x)/len(x)

def mediana(x):
	if len(x)%2==0:
		i = int(len(x)/2)
		return (x[i]+x[i-1])/2
	else:
		i = int(len(x)/2)
		return x[i]

def varianza(x):
	ans = 0
	for i in x:
		ans += (i - media(x))**2
	return ans

def desvio(x):
	return np.sqrt(varianza(x))

def E(x):
	ans = 0
	for k in x.keys():
		ans += k * x[k]
	return ans

def V(x):
	esq = 0
	for k in x.keys():
		esq += k**2 * x[k]
	ans = esq - E(x)**2 
	return ans

def new_E(x, a, b):
	ans = a * E(x) - b
	return ans

def new_V(x, a, b):
	ans = a**2 * V(x)
	return ans

def fact(n):
	ans = 1
	for i in range(1, n+1):
		ans *= i
	return ans

def nCr(n, m):
	ans = fact(n) / (fact(m) * fact(n-m))
	return ans

def binomial_probt(casos, exito, acumulada=False):
	ans = [0] * (casos+1)
	acum = 0
	for i in range(0,casos+1):
		if acumulada:
			acum += nCr(casos,i) * exito**i * (1-exito)**(casos-i)
			ans[i] = acum
		else: 
			ans[i] = nCr(casos,i) * exito**i * (1-exito)**(casos-i)
	ans = dict(zip(range(0,casos+1),ans))
	return ans

def hypergeo_probt(casos,exitos,selec, acumulada=False):
	ans = [0] * (exitos+1)
	fracasos = casos - exitos
	acum = 0
	for i in range(0, exitos+1):
		if acumulada:
			if fracasos < (selec-i):
				acum += 0
				ans[i] = acum
			else:
				acum += nCr(exitos,i)*nCr(fracasos,(selec-i))/nCr(casos,selec)
				ans[i] = acum
		else: 
			if fracasos < (selec-i):
				ans[i] = 0
			else:
				ans[i] = nCr(exitos,i)*nCr(fracasos,(selec-i))/nCr(casos,selec)
	ans = dict(zip(range(0,exitos+1),ans))
	return ans

def ej6():
	datos = {13.5:0.2, 15.9:0.5, 19.1:0.3}

	exp = E(datos)
	esq = 0
	for k in datos.keys():
		esq += k**2 * datos[k]
	var = V(datos)

	print("a) E(X) =","%.2f"% exp, " E(X**2) =","%.2f"% esq, "y V(X) =","%.2f"% var)
	
	nexp = new_E(datos, 25, 8.5)
	nvar = new_V(datos, 25, 8.5)

	print("b) E(Y) =", "%.2f"% nexp, "y V(Y) =", "%.2f"% nvar)

	def h(x):
		ans = E(x)*g(x)
		return ans
	
	def g(x):
		ans = 1 - 0.01*E(x)
		return ans

	print("c) E(h(X)) =",  "%.2f"% h(datos))

def ej7():
	prob_table = [0] * 21

	for i in range(0,21):
		prob_table[i] = nCr(20,i) * 0.2**i * 0.8**(20-i) 

	ansi = 0
	for i in range(0,6):
		ansi += prob_table[i]
	print("i)","%.4f"% ansi)

	ansii = nCr(20, 15) * 0.8**15 * 0.2**5
	print("ii)","%.4f"% ansii)
  
	comp = 0
	for i in range(0,5):
		comp += prob_table[i]
	ansiii = 1 - comp
	print("iii)","%.4f"% ansiii)

	print("b)","%.4f"% E(dict(zip(range(0,21),prob_table))))

def ej8():
	prob = [0] * 11
	for i in range (0,11):
		prob[i] = nCr(10,i) * 0.6**i * 0.4**(10-i)

	ansa = 0
	for i in range(0,7):
		ansa += prob[i]
	print("a)","%.4f"% ansa)
	
	dprob = dict(zip(range(0,11), prob))
	left = math.floor(E(dprob)-math.sqrt(V(dprob)))
	right = math.ceil(E(dprob)+math.sqrt(V(dprob)))
	print("b) limite izquierdo:", left, "limite derecho:", right)
	ansb = 0
	for i in range(4,9):
		ansb += prob[i]
	print("   P("+str(left)+"<=X<="+str(right)+") =","%.3f"%ansb)

	
	ansc = 0
	for i in range(7,11):
		ansc += prob[i]
	for i in range(0,4):
		ansc += prob[i]
	print("c)", "%.3f"%(1-ansc))

def ej9():
	congar = binomial_probt(20, 0.2)
	singar = binomial_probt(20, 0.8)

	print("a) E(Sin Garantia) =", "%.3f"%E(singar))
	print("b) E(Garantia) =", "%.3f"%E(congar))
	
	ansc = 0
	for i in range(0,6):
		ansc += congar[i]
	print("c) P(5) =", "%.3f"%ansc)

	prob_d = hypergeo_probt(12,4,5)
	print("d) E(X) =", "%.3f"%E(prob_d),"y V(X) =", "%.3f"%V(prob_d))

def ej10():
	prob = hypergeo_probt(10, 7, 6)
	prob_acum =  hypergeo_probt(10, 7, 6, True)

	print("i)", prob[1])
	
	ansii = prob_acum[6] - prob_acum[3]
	print("ii)","%.3f"%ansii)
	
	ansiii = prob_acum[5] - prob_acum[2]
	print("iii)","%.3f"%ansiii)

	print("b) E(X) =", "%.3f"%E(prob),"y V(X) =", "%.3f"%V(prob))