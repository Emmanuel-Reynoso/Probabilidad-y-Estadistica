import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *

def show():
	ans = 0

def ej2():
	k = 1./1000
	print("a) k =", k)
	f = lambda y, x: k*(x+y)
	ib = integrate.dblquad(f, 0, 8, lambda x: 2, lambda x: x+2)
	ans = 1 - 2*ib[0]
	print("b) P(|X-Y|<2) = 1 - 2*P(0<X<8 ∩ 2<Y<2+X) =", "%.3f"%ans)
	ic1 = integrate.dblquad(f, 0, 5, lambda x: 0, lambda x: 5-x)
	ans = ic1[0] 	
	print("c) P(|X-Y|<5) = P(Y < 5-X) =", "%.3f"%ans)
	print("d) Px(x) = (x+5)/100")
	print("   Py(y) = (y+5)/100")
	print("   independencia:", f(2,3) == 7/100 * 5/100) 
	px = lambda x: (x+5)/100
	print("e) cov(X,Y) =", "%.3f"%cov(f,px,px, 0, 10))