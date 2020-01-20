import matplotlib.pylab as plt
import numpy as np
import math

MAX_POISSON = 38

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
	if isinstance(x, dict):
		return np.sqrt(V(x))		
	else:
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

def NB_probt(exitos, prob, max_cases = 100, acumulada=False):
	ans = [0] * (max_cases+1)
	acum = 0
	for i in range(0,max_cases+1):
		if acumulada:
			acum += nCr(exitos+i-1, exitos-1) * prob**exitos * (1-prob)**i
			ans[i] = acum
		else: 
			ans[i] = nCr(exitos+i-1, exitos-1) * prob**exitos * (1-prob)**i
	ans = dict(zip(range(0,max_cases+1),ans))
	return ans

def poisson_probt(lam, acumulada=False):
	ans = [0] * MAX_POISSON
	acum = 0
	for i in range (0, MAX_POISSON):
		if acumulada:
			acum += math.e**-lam * lam**i / fact(i)
			ans[i] = acum
		else: 
			ans[i] = math.e**-lam * lam**i / fact(i)
	ans = dict(zip(range(0,MAX_POISSON), ans))
	return ans
