import math
from scipy import integrate
from pynverse import inversefunc
from definiciones import *


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
	print("e) cov(X,Y) =", "%.3f"%cov(f, 0, 10))
	show_conjunta(f,0,10)

def ej4():
	p, fda, e, v = exp_dist(1)
	print("a) f(x,y) = exp(-x-y) si 0 < x,y")
	f = lambda x,y: p(x)*p(y)
	ans = integrate.dblquad(f,0,1,lambda x:0,lambda x:1)[0]
	print("b) P(X+Y<1) =", "%.3f"%ans)
	ans = integrate.dblquad(f,0,2,lambda x:0,lambda x:2-x)[0]
	print("c) P(X+Y<2) =", "%.3f"%ans)
	
	show_conjunta(f, 0, 2)
	
def ej9():
	pt, pta, e, v, d = binomial_dist(50, 0.4)
	print("a)")
	print("  valor exacto:", "%.3f"%(1 - pta[24]))
	print("  valor aproximado por normal:", "%.3f"%(1 - Zvalue(a=1.155)))
	print("b)")
	print("  valor exacto:", "%.3f"%(pta[25]-pta[15]))
	print("  valor aproximado por normal:", "%.3f"%(Zvalue(a=-1.44,b=1.44)))
	