import matplotlib.pylab as plt
import numpy as np
from scipy import special
from scipy import integrate
import math

MAX_POISSON = 28

def mediana(x, cont=False):
	if len(x)%2==0:
		i = int(len(x)/2)
		return (x[i]+x[i-1])/2
	else:
		i = int(len(x)/2)
		return x[i]


def desvio(x, a=None, b=None, continuous=False, modify=False):
	return math.sqrt(V(x, a, b, continuous, modify))

def E(x, a=None, b=None, continuous=False, modify=False):
	if modify:
		return a * E(x) - b
	if continuous:
		return integrate.quad(lambda y:y*x(y),a,b)[0]
	if isinstance(x, dict):
		ans = 0
		for k in x.keys():
			ans += k * x[k]
	else:
		return sum(x)/len(x)
	return ans

def E2(x, a, b):	
	return integrate.quad(lambda y:y*y*x(y),a,b)[0]

def V(x, a=None, b=None, continuous=False, modify=False):
	if modify:
		return a**2 * V(x)
	if continuous:
		return E2(x, a, b) - E(x,a,b, True)**2
	if isinstance(x, dict):
		esqared = 0
		for k in x.keys():
			esqared += k**2 * x[k]
		ans = esqared - E(x)**2 
	else:
		ans = 0
		for i in x:
			ans += (i - E(x))**2
	return ans

def fact(n):
	ans = 1
	for i in range(1, n+1):
		ans *= i
	return ans

def nCr(n, m):
	ans = fact(n) / (fact(m) * fact(n-m))
	return ans

def binomial_probt(ensayos, p_exito, acumulada=False):
	ans = [0] * (ensayos+1)
	acum = 0
	for i in range(0,ensayos+1):
		if acumulada:
			acum += nCr(ensayos,i) * p_exito**i * (1-p_exito)**(ensayos-i)
			ans[i] = acum
		else: 
			ans[i] = nCr(ensayos,i) * p_exito**i * (1-p_exito)**(ensayos-i)
	ans = dict(zip(range(0,ensayos+1),ans))
	return ans

def hypergeo_probt(muestra, num_exitos, total, acumulada=False):
	ans = [0] * (num_exitos+1)
	fracasos = total - num_exitos
	acum = 0
	for i in range(0, num_exitos+1):
		if acumulada:
			if fracasos < (muestra-i):
				acum += 0
				ans[i] = acum
			else:
				acum += nCr(num_exitos,i)*nCr(fracasos,(muestra-i))/nCr(total,muestra)
				ans[i] = acum
		else: 
			if fracasos < (muestra-i):
				ans[i] = 0
			else:
				ans[i] = nCr(num_exitos,i)*nCr(fracasos,(muestra-i))/nCr(total,muestra)
	ans = dict(zip(range(0,num_exitos+1),ans))
	return ans

def BN_probt(num_exitos, prob, max_cases = 100, acumulada=False):
	ans = [0] * (max_cases+1)
	acum = 0
	for i in range(0,max_cases+1):
		if acumulada:
			acum += nCr(num_exitos+i-1, num_exitos-1) * prob**num_exitos * (1-prob)**i
			ans[i] = acum
		else: 
			ans[i] = nCr(num_exitos+i-1, num_exitos-1) * prob**num_exitos * (1-prob)**i
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


def binomial_dist(n, p):
	prob_table = binomial_probt(n, p, False)
	cumulative_table = binomial_probt(n, p, True)
	e = n*p
	v = n*p*(1-p)
	return prob_table, cumulative_table, e, v, math.sqrt(v)

def hypergeo_dist(n, M, N):
	prob_table = hypergeo_probt(M, N, n, False)
	cumulative_table = hypergeo_probt(M, N, n, True)
	e = n * M / N
	v = n*M/N * (1 - M/N) * (N-n)/(N-1)
	des = math.sqrt(v)
	return prob_table, cumulative_table, e, v, des

def BN_dist(r, p, max_cases=100):
	prob_table = BN_probt(r, p, False)
	cumulative_table = BN_probt(r, p, True)
	e = r * (1-p) / p
	v = r * (1-p) / p**2
	des = math.sqrt(v)
	return prob_table, cumulative_table, e, v, des

def poisson_dist(lam):
	prob_table = binomial_probt(lam, False)
	cumulative_table = binomial_probt(lam, True)
	e = lam
	v = lam
	return prob_table, cumulative_table, e, v, math.sqrt(v)

def uniform_dist(a, b):
	fda = lambda x: (x-a)/(b-a)
	f = lambda x: 1/(b-a)
	e = (a+b) / 2
	v = (b-a)**2 / 12
	return f, fda, e, v

def normal_dist(e=None, v=None):
	std = lambda x: (math.e**((x**2 / 2)*(-1))) / math.sqrt(2*math.pi) 
	if e != None:
		f = lambda x: (math.e**(((x-e)**2 / (2*v)) * (-1))) / math.sqrt(2*math.pi*v)
		return f, std	
	else:
		return std

def gamma_dist(a, b):
	f = lambda x: x**(a-1.) * np.e**(-x/b) / (b**a * special.gamma(a))
	e = a * b
	v = a * b**2
	fda = lambda x: integrate.quad(f, 0., x)[0]
	return f, fda, e, v

def exp_dist(lam):
	f, fda, e, v = gamma_dist(1.,1./lam)
	e = 1 / lam
	v = 1 / lam**2
	fda = lambda x: 1.-math.e**(-lam*x)
	return f, fda, e, v

def chi2_dist(k):
	f, fda, e, v = gamma_dist(int(k)/2,2)
	e = k
	v = 2*k
	return f, fda, e, v

def weibull_dist(a, b):
	f = lambda x: a * x**(a-1.) * np.e**(-((x/b)**a)) / (b**a)
	e = b * special.gamma(1+1/a)
	v =  b**2 * (special.gamma(1+2/a) - special.gamma(1+1/a)**2)
	fda = lambda x: integrate.quad(f, 0., x)[0]
	return f, fda, e, v

"""
def test():
	bi_prob = binomial_probt(20, 0.2)
	bit, bict, bie, biv, bid = binomial_dist(20, 0.2)
	print("binomial:")
	print("E(X) =", "%.3f"%E(bi_prob),"y V(X) =", "%.3f"%V(bi_prob))
	print("E(X) =", "%.3f"%bie,"y V(X) =", "%.3f"%biv)

	hg_prob = hypergeo_probt(6, 7, 10)
	hgt, hgct, hge, hgv, hgd = hypergeo_dist(6, 7, 10)
	print("hipergeometrica:")
	print("E(X) =", "%.3f"%E(hg_prob),"y V(X) =", "%.3f"%V(hg_prob))
	print("E(X) =", "%.3f"%hge,"y V(X) =", "%.3f"%hgv)


	bn_prob = BN_probt(4, 0.3)
	bnt, bnct, bne, bnv, bnd = BN_dist(4, 0.3)
	print("binomial negativa:")
	print("E(X) =", "%.3f"%E(bn_prob),"y V(X) =", "%.3f"%V(bn_prob))
	print("E(X) =", "%.3f"%bne,"y V(X) =", "%.3f"%bnv)

	po_prob = poisson_probt(5)
	pot, poct, poe, pov, pod = poisson_dist(5)
	print("poisson:")
	print("E(X) =", "%.3f"%E(po_prob),"y V(X) =", "%.3f"%V(po_prob))
	print("E(X) =", "%.3f"%poe,"y V(X) =", "%.3f"%pov)

	unif,unie,univ = uniform_dist(0,1)
	print("uniforme:")
	print("E(X) =", "%.3f"%E(unif,0,1,True),"y V(X) =", "%.3f"%V(unif,0,1,True))
	print("E(X) =", "%.3f"%unie,"y V(X) =", "%.3f"%univ)
"""
