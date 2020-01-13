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

def ej13():

	prob_def = 1 - 0.86**(1/25)

	print("* a) P(D) = 1 - 0.86**(1/25) =", "%.3f" %prob_def)

	prob_10 = 1 - 0.90**(1/25)

	print("* b) P(D) = 1 - 0.90**(1/25) =", "%.3f" %prob_10)
