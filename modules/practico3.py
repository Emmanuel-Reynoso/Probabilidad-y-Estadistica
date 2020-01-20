import matplotlib.pylab as plt
import math
from definiciones import *

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
	prob_acum = hypergeo_probt(10, 7, 6, True)

	print("i)", prob[1])
	
	ansii = prob_acum[6] - prob_acum[3]
	print("ii)","%.3f"%ansii)
	
	ansiii = prob_acum[5] - prob_acum[2]
	print("iii)","%.3f"%ansiii)

	print("b) E(X) =", "%.3f"%E(prob),"y V(X) =", "%.3f"%V(prob))

def ej11():
	print("a) Utilizando una Binomial Negativa X~B-(2,0.5)")
	print("p(x) = nCr(2+x-1, 2-1) * 0.5**2 * 0.5**x = (x+1) * 0.5**(x+2)")

	datos = NB_probt(2,0.5)
	print("b)", "%.3f"%datos[2])

	ansc = datos[0] + datos[1] + datos[2]  
	print("c)","%.3f"%ansc)

	print("d) varones esperados =", E(datos),",total de hijos esperados =", 2+E(datos))

def ej12():

	tabla = poisson_probt(8, True)
	
	print("i) P(X <= 5) =", "%.3f"% (tabla[5]))
	print("ii) P(6 <= X <= 8) =", "%.3f"% (tabla[9] - tabla[5]))
	print("iii) P(X >= 1) =", "%.3f"% (1-tabla[1]))

	print("b) E(X) = 8, desvio(X) =", "%.3f"% (math.sqrt(8)))

def ej13():
	p3 = poisson_probt(3)
	p4 = poisson_probt(4)
	ans = 0
	for i in range(0,4):
		ans += p3[i]*p4[3-i]
	print("la probabilidad es de","%.3f"%ans)
	