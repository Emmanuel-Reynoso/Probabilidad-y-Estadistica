import matplotlib.pylab as plt
import math
from definiciones import *

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
	print("Frecuencia relativa: ", frec[0])
	print("Frecuencia Absoluta: ", frec[1])
	#Graficamos
	fig, graficos = plt.subplots(2)     
	fig.set_size_inches(5, 12)
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
	return promedio, math.sqrt(dispersion)
	 
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

def ej11():
	control = [1202.6, 830.1, 372.4, 345.5, 321.2, 244.3, 163, 147.8, 95, 87, 81.2, 68.5, 47.3, 41.1, 36.6, 29.0, 28.6, 26.3, 26.1, 24.4, 21.7, 17.3, 11.5, 4.9, 4.9, 1]
	sembradas = [2745.6, 1697.8, 1656, 978, 703.4, 489.1, 430, 334.1, 302.8, 274.7, 274.7, 255, 242.5, 200.7, 198.6, 129.6, 119, 118.3, 115.3, 92.4, 40.6, 32.7, 31.4, 17.5, 7.7, 4.1]

	cmax = max(control)
	smax = max(sembradas)
	cmin = min(control)
	smin = min(sembradas)
	crange = cmax - cmin
	srange = smax - smin
	cmedia = sum(control)/len(control)
	smedia = sum(sembradas)/len(sembradas)
	cdesvio = desvio(control)
	sdesvio = desvio(sembradas)
	cq1 = control[int(0.25*len(control))]
	cq3 = control[int(0.75*len(control))]
	sq1 = sembradas[int(0.25*len(sembradas))]
	sq3 = sembradas[int(0.75*len(sembradas))]
	print("a)")
	print("maximo control: ","%.3f" % cmax)
	print("minimo control: ", "%.3f" % cmin)
	print("rango control: ", "%.3f" % crange)
	print("promedio control: ", "%.3f" % cmedia)
	print("desvio estandar control: ", "%.3f" % cdesvio)
	print("Q1 control:", "%.3f" % cq1,"Q3 control:", "%.3f" % cq3)
	print("-----------------------------------")
	print("maximo sembradas: ", "%.3f" % smax)
	print("minimo sembradas: ", "%.3f" % smin)
	print("rango sembradas: ", "%.3f" % srange)
	print("promedio sembradas: ", "%.3f" % smedia)
	print("desvio estandar sembradas: ", "%.3f" % sdesvio)
	print("Q1 sembradas:", "%.3f" % sq1,"Q3 sembradas:", "%.3f" % sq3)
	print("")
	print("b)")
	fig, cajas = plt.subplots(2)     
	fig.set_size_inches(5, 12)
	cajas[0].set_title('Control')
	cajas[1].set_title('Sembradas')
	cajas[0].grid(axis='y')
	cajas[1].grid(axis='y')
	cajas[0].boxplot(control)
	cajas[1].boxplot(sembradas)
	
	plt.show()
	
def ej12():
	IDT = [13.7, 15.5, 16.8, 17.40, 17.9, 18.6, 19.1, 19.5, 20.7, 21, 21.1, 21.4, 21.4, 22.3, 23.7, 25.5, 25.8, 26.2, 26.6, 28, 28.1, 28.9, 30.6, 31.2, 31.90, 32, 34.8, 36.3, 38.4, 38.8, 40.9, 43.5, 46, 48.9, 52.1, 55.6, 57.3, 60.1, 62.3, 72.8]
	ln_IDT = list(map(math.log,IDT))
	
	solve12(IDT, "IDT", 10, 10)
	print("-----------------------------")
	solve12(ln_IDT, "ln_IDT", 0.4, 2.5)

def solve12(arr, name, interval, start):

	print("a)")
	print("maximo",name,":", "%.3f" % max(arr))
	print("minimo",name,":", "%.3f" % min(arr))
	print("rango",name,":","%.3f" % (max(arr) - min(arr)))
	print("promedio",name,":","%.3f" % E(arr))
	print("mediana",name,":","%.3f" % mediana(arr))
	print("desvio estandar",name,":","%.3f" % desvio(arr))

	num_inter = math.ceil((max(arr)-start)/interval)
	frec = [0] * num_inter
	for el in arr:
		i = int((el-start)/interval)
		frec[i] = frec[i]+1

	abso = [0] * num_inter
	acum = 0
	for i in range(0, len(frec)):
		acum+= frec[i]
		abso[i] = acum

	tix = [start] * num_inter
	for i in range(1, len(tix)):
		tix[i] += interval*i

	fig, graficos = plt.subplots(2)     
	fig.set_size_inches(5, 12)
	graficos[0].set_title(name+' - Frecuencia Relativa')
	graficos[1].set_title(name + ' - Frecuencia Absoluta')
	graficos[0].bar(range(len(frec)), frec, align='center')
	graficos[1].bar(range(len(frec)), abso, align='center')
	graficos[0].set_xticks(range(len(frec)))
	graficos[1].set_xticks(range(len(frec)))
	graficos[0].set_xticklabels(tix)
	graficos[1].set_xticklabels(tix)
	graficos[0].grid(axis='y')
	graficos[1].grid(axis='y')
	plt.show()

	plt.title(name+" - Boxplot")
	plt.grid(axis='y')
	plt.boxplot(arr)
	plt.show()

	print("g) ")
	for i in range(1,4):
		left = E(arr) - i * desvio(arr)
		right = E(arr) + i * desvio(arr)
		ans = 0
		for el in arr:
			if left <= el and el <= right:
				ans = ans + 1
		print("hay un", int((ans/len(arr))*100), "% con k =", i, "entre","%.3f" % left, "y","%.3f" % right)