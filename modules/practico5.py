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
	
def ej8():
	za = Zvalue(3,2.65,0.85)
	print("a)","%.3f"%(aprox_prob(2.65,0.85,25,b=3)))
	print("  ","%.3f"%(aprox_prob(2.65,0.85,25,a=2.65,b=3)))

	n = 25
	while n<1000 and aprox_prob(2.65,0.85,n,b=3) < 0.99:
		n+=1
	print("b)", n)

def ej9():
	pt, pta, e, v, d = binomial_dist(50, 0.4)
	print("a)")
	print("  valor exacto:", "%.3f"%(1 - pta[24]))
	print("  valor aproximado por normal:", "%.3f"%(prob_norm(a=1.155)))
	print("b)")
	print("  valor exacto:", "%.3f"%(pta[25]-pta[15]))
	print("  valor aproximado por normal:", "%.3f"%(prob_norm(a=-1.44,b=1.44)))
	
def ej10():
	pt, pta, e, v, d = binomial_dist(200, 0.1)
	za = Zvalue(30, e, d)
	zcb = Zvalue(25, e, d)
	zca = Zvalue(15, e, d)

	print("a) ")
	print("  valor exacto:", "%.3f"%(pta[30]))
	print("  valor aproximado:", "%.3f"%(1 - prob_norm(a=za)))
	print("b) ")
	print("  valor exacto:", "%.3f"%(pta[29]))
	print("  valor aproximado:", "%.3f"%(1 - prob_norm(a=Zvalue(29, e, d))))
	print("c) ")
	print("  valor exacto:", "%.3f"%(pta[25]-pta[15]))
	print("  valor aproximado:", "%.3f"%(prob_norm(a=zca, b=zcb)))

def ej11():

	print("a)","%.3f"%aprox_prob(12.5,2.5,100,a=12,b=13))

	n = 30
	while n<1000 and aprox_prob(12.5,2.5,n,a=12.1,b=13.1) < 0.95:
		n+=1
	print("b)", n)

def ej12():
	print("a)")
	print("   X~N(106, "+ "%.3f"%(8**2 / 40)+")")
	print("   Y~N(104, "+"%.3f"%(6**2 / 35)+")")
	print("   E(X-Y) = 106 - 104 = 2")
	print("   V(X-Y) = V(X) + V(Y) = "+"%.3f"%(8**2 / 40 + 6**2 / 35))
	print("   (X-Y)~N(2, "+"%.3f"%(8**2 / 40 + 6**2 / 35)+")")

	print("b)", "%.3f"%aprox_prob(2, math.sqrt(2.629), 1, a=-1, b=1))
	print("c)", "%.3f"%aprox_prob(2, math.sqrt(2.629), 1, a=6))
def ej13():
	print(aprox_prob(3000, math.sqrt(52500),365,a=2950,b=3050))
	
