import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def ej1():
	datos = {0:18, 1:37, 2:42, 3:30, 4:13, 5:7, 6:2, 7:1}
	mean = E(datos)
	var = V(datos)/150
	print("a) un estimador insesgado es X barra. su valor es:", "%.3f"%mean)
	error = math.sqrt(var)
	print("b) desvio del estimador:", "%.3f"%error) 
	print("   error estandar estimado:", "%.3f"%error) 


