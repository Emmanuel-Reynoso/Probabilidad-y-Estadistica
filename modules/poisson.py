import matplotlib.pylab as plt
from definiciones import *

def show():
	table = [{}] * MAX_POISSON
	fig, ax = plt.subplots(MAX_POISSON, figsize=(12, 150))
	for i in range(0,MAX_POISSON):
		table[i] = poisson_probt(i)
		ax[i].plot(list(table[i].keys()), list(table[i].values()))
		ax[i].grid(axis='y')
		ax[i].set_xlabel('P(X = x)')
		ax[i].set_ylabel('λ = '+ str(i))
	plt.show()

def show_cummulative():
	table = [{}] * MAX_POISSON
	fig, ax = plt.subplots(MAX_POISSON )
	fig.set_size_inches(12,150)
	for i in range(0,MAX_POISSON):
		table[i] = poisson_probt(i, True)
		ax[i].plot(list(table[i].keys()), list(table[i].values()))
		ax[i].grid(axis='y')
		ax[i].set_xlabel('P(X <= x)')
		ax[i].set_ylabel('λ = '+ str(i))
	plt.show()