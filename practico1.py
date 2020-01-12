
import matplotlib.pylab as plt
import numpy as np

def ej2():
	#Procesamos los datos
	cantidades = {'N': 7, 'O': 21, 'J': 10, 'F': 9, 'T': 3, 'B': 6, 'M': 4}
	#Ordenamos la lista
	frec = [{},{}]
	frec[0] = dict(sorted(cantidades.items(), key=lambda x: x[1]))
	
	#Armamos la tabla de frecuencia acumulada
	acumulada = 0
	for k in frec[0].keys():
		acumulada += frec[0][k]
		frec[1][k] = acumulada
	#Graficamos
	fig, graficos = plt.subplots(2)     
	fig.set_size_inches(5, 6.5)
	graficos[0].set_title('Frecuencia Relativa')
	graficos[1].set_title('Frecuencia Absoluta')
	for i in range(0, 2):
		graficos[i].bar(range(len(frec[i])), list(frec[i].values()), align='center')
		graficos[i].set_xticks(range(len(frec[i])))
		graficos[i].set_xticklabels(list(frec[i].keys()))
		graficos[i].grid(axis='y')
	plt.show()

def solve(arreglo):
	promedio = sum(arreglo) / len(arreglo)
	dispersion = 0
	for x in arreglo:
		dispersion += (x-promedio)*(x-promedio)
	return promedio, np.sqrt(dispersion)
	 
def ej3():
	pa,da = solve([0,20,40,50,60,80,100])
	pb,db = solve([0,48,49,50,51,52,100])
	pc,dc = solve([0,1,2,50,98,99,100])

	print("a) promedio =", "%.2f" % pa," desviacion =", "%.2f" % da)
	print("b) promedio =", "%.2f" % pb," desviacion =", "%.2f" % db)
	print("c) promedio =", "%.2f" % pc," desviacion =","%.2f" %  dc)

def ej4():
	prom10 = (5*2 + 3*3 + 1*1 + 1*0)/10
	prom20 = (10*2 + 6*3 + 2*1 + 2*0)/20

	print("a) promedio para 10 = ", "%.2f" % prom10)
	print("   promedio para 20 = ", "%.2f" % prom20)
	print("b)", prom10==prom20)

def ej5():
	claseA = [1] * 99
	claseA[0] = 1
	claseA[98] = 99
	for i in range(1, 98):
		claseA[i] = 50

	claseB = [1] * 99
	claseB[0] = 1
	claseB[1] = 50
	for i in range(2,99):
		claseB[i] = 99

	claseC = [1] * 99
	for i in range(0,99):
		claseC[i] = i

	pa, da = solve(claseA)
	pb, db = solve(claseB)
	pc, dc = solve(claseC)	

	print("clase A - promedio =","%.2f" %  pa)
	print("        - desviacion =","%.2f" %  da)
	print("clase B - promedio =","%.2f" %  pb)
	print("        - desviacion =","%.2f" %  db)
	print("clase C - promedio =", "%.2f" % pc)
	print("        - desviacion =", "%.2f" % dc)

def ej6():
	arreglo = [160,174,176,177,179,
				180,180,181,183,187,
				191,194,200,202,203,
				205,207,211,211,254]

	n = len(arreglo)
	media = sum(arreglo)/n
	if n%2==1:
		mediana = arreglo[int(n/2)]
	else:
		mediana = (arreglo[int(n/2)]+arreglo[int(n/2)-1])/2 

	print("a) media =","%.2f" %  media, "y mediana =","%.2f" %  mediana)
	arreglo2 = arreglo
	arreglo2[19] = 211

	media2 = sum(arreglo2)/n
	if n%2==1:
		mediana2 = arreglo2[int(n/2)]
	else:
		mediana2 = (arreglo2[int(n/2)]+arreglo2[int(n/2)-1])/2 
	print("b) media =", "%.2f" % media2, "y mediana =", "%.2f" % mediana2)

	media3 = (sum(arreglo2)-160-254)/(n-2)

	mediana3 = (arreglo2[int((n-2)/2)]+arreglo2[int((n-2)/2)-1])/2 
	print("c) media =", "%.2f" % media3, "y mediana =", "%.2f" % mediana3)
	print("   el porcentaje es de :", 100*1/20,"%")

	arreglo4 = [179,180,180,181,183,187,191,194,200,202,203,205]
	n = len(arreglo4)
	media4 = (sum(arreglo4))/(n)
	mediana4 = (arreglo4[int((n)/2)]+arreglo4[int((n)/2)-1])/2
	print("d) media =", "%.2f" % media4,"y mediana =", "%.2f" % mediana4)

	print("e)",(119.8*19+159)/20)

def ej7():

	arreglo = [1, 1, 0, 1, 1, 1, 0 ,0, 1, 1]

	prop_exitos = sum(arreglo)/10
	print("a) la proporcion de exitos es:", "%.2f" % prop_exitos)
	print("b) la media es:", "%.2f" % prop_exitos)
	print("c)", int(25*0.80))

def ej8():
	arreglo = [104, 104.8, 101.6, 108, 103.8, 200.8, 104.2, 100.2, 102.4, 101.4]

	pa, da = solve(arreglo)
	print("i)en Fahren: promedio =", "%.3f" % pa,"y desviacion =", "%.3f" % da)
	pb = (5/9)*pa-(5/9)*32
	db = (5/9)*(5/9)*da
	print("ii)en Celcius: promedio =", "%.3f" % pb,"y desviacion =", "%.3f" % db)
	pc = 87.3 * (9/5) + 32
	dc = (9/5)*(9/5)* 1.04
	print("iii) promedio = ","%.3f" % pc,"y desviacion =","%.3f" % dc)