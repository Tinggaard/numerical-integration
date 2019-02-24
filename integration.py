import math
import matplotlib.pyplot as plt


# x-værdier fordelt på et interval
def linspace(start, end, n=100):
	width = (end-start)/n
	return [start+(i*width) for i in range(n)]


# Plot en funktion
def plot(func, start, end, color="b-", axes=True ,plt=plt):

	f = lambda x: eval(func)

	width = (end-start)/500
	xs = linspace(start, end, n=500)
	xs.append(xs[-1]+width)
	
	ys = [f(x) for x in xs]
	plt.plot(xs, ys, color)

	# Mulighed for at printe x=0 og y=0
	if axes:
		y = 0
		if min(ys) < 0:
			y = min(ys)
		x = 0
		if start < 0:
			x = start

		#Akserne
		plt.plot([x, end+(25*width)], [0, 0], "k-")
		plt.plot([0, 0], [y, max(ys)+(max(ys)/25)], "k-")
		#Pile
		plt.plot(end+(25*width), 0, "k>")
		plt.plot(0, max(ys)+(max(ys)/25), "k^")



# Nulpunkt - i et givet interval
def zero(func, start, end, animate=True, plt=plt):

	f = lambda x: eval(func)

	for i in range(100):
		mid = (start+end)/2
		if f(mid) * f(start) > 0:
			start = mid
		else:
			end = mid

	if animate:
		plt.plot([mid], [0], "kx")

	return mid


# Venstresum
def sum_left(func, start, end, n=10, animate=True, plt=plt):

	f = lambda x: eval(func)
	
	width = (end-start)/n
	left = [f(width*i+start)*width for i in range(n)]

	if animate:
		xs = linspace(start, end, n)
		for i in xs:
			plt.plot([i, i], [0, f(i)], "ko--")
			plt.plot([i+width, i+width], [0, f(i)], "ko--")
			plt.plot([i, i+width], [f(i), f(i)], "ko--")

		for i in range(n):
			plt.text(width*(i+0.5)+start, f(width*i+start)/2, str(round(left[i],2)), horizontalalignment="center")

	return left


# Højresum
def sum_right(func, start, end, n=10, animate=True, plt=plt):

	f = lambda x: eval(func)

	width = (end-start)/n
	right = [f(width*i+start)*width for i in range(1, n+1)]

	if animate:
		xs = linspace(start, end, n)
		for i in xs:
			plt.plot([i, i], [0, f(i+width)], "ko--")
			plt.plot([i+width, i+width], [0, f(i+width)], "ko--")
			plt.plot([i, i+width], [f(i+width), f(i+width)], "ko--")
		for i in range(n):
			plt.text(width*(i+0.5)+start, f(width*(i+1)+start)/2, str(round(right[i],2)), horizontalalignment="center")

	return right


# Midtsum
def sum_middle(func, start, end, n=10, animate=True, plt=plt):

	f = lambda x: eval(func)

	width = (end-start)/n
	half = width/2
	middle = [f(width*(i+0.5)+start)*width for i in range(n)]

	if animate:
		xs = linspace(start, end, n)
		for i in xs:
			plt.plot([i, i], [0, f(i+half)], "ko--")
			plt.plot([i+width, i+width], [0, f(i+half)], "ko--")
			plt.plot([i, i+width], [f(i+half), f(i+half)], "ko--")
		for i in range(n):
			plt.text(width*(i+0.5)+start, f(width*(i+0.5)+start)/2, str(round(middle[i],2)), horizontalalignment="center")

	return middle

# Trapezsum
def sum_trapez(func, start, end, n=10, animate=True, plt=plt):

	f = lambda x: eval(func)

	width = (end-start)/n
	trapez = [(f(width*i+start) + f(width*i+start+width))*(width/2) for i in range(n)]
	if animate:
		xs = linspace(start, end, n)
		for i in xs:
			plt.plot([i, i], [0, f(i)], "ko--")
			plt.plot([i+width, i+width], [0, f(i+width)], "ko--")
			plt.plot([i, i+width], [f(i), f(i+width)], "ko--")
		for i in range(n):
			plt.text(width*(i+0.5)+start, f(width*(i+0.5)+start)/2, str(round(trapez[i],2)), horizontalalignment="center")

	return trapez

# Simpsons metode
def simpsons(func, start, end, n=10, animate=True):
	assert n % 2 == 0

	f = lambda x: eval(func)

	xs = linspace(start, end, n)
	width = (end-start)/n
	xs.append(xs[-1]+width)

	simp = [(width/3)*(f(xs[i])+4*f(xs[i+1])+f(xs[i+2])) for i in range(0, n, 2)]

	if animate:
		for i in range(0, n, 2):
			x1 = xs[i]
			x2 = xs[i+1]
			x3 = xs[i+2]
			y1 = f(xs[i])
			y2 = f(xs[i+1])
			y3 = f(xs[i+2])

			# lavet vha solve i Maple
			A = -(x1*y2 - x1*y3 - x2*y1 + x2*y3 + x3*y1 - x3*y2) / (x1*x1*x2 - x1*x1*x3 - x1*x2*x2 + x1*x3*x3 + x2*x2*x3 - x2*x3*x3)
			B = (x1*x1*y2 - x1*x1*y3 - x2*x2*y1 + x2*x2*y3 + x3*x3*y1 - x3*x3*y2) / ((x1-x2) * (x1*x2 - x1*x3 - x2*x3 + x3*x3))
			C = (x1*x1*x2*y3 - x1*x1*x3*y2 - x1*x2*x2*y3 + x1*x3*x3*y2 + x2*x2*x3*y1 - x2*x3*x3*y1) / ((x1-x2) * (x1*x2 - x1*x3 - x2*x3 + x3*x3))
			def g(x):
				return A*x*x + B*x + C

			xer = linspace(x1, x3, 30)
			xer.append(xer[-1] + (xer[-1]-xer[-2]))
			funk = [g(x) for x in xer]
		
			
			plt.plot([x1, x1], [0, y1], "ko--")
			plt.plot([x3, x3], [0, y3], "ko--")
			plt.plot([x1, x2, x3], [y1, y2, y3], "ko")
			plt.plot(xer, funk, "k--")

			plt.text(width*(i+1)+start, g(width*(i+1)+start)/2,str(round(simp[int(i/2)], 2)), horizontalalignment="center")

	return simp


# Vis gitter 
def grid():
	plt.grid()

# Vis 
def show():
	plt.show()

# Tegn en linje op til f(x) ved x (brugt til billede i rapport)
def x_eq(func, x):
	f = lambda x: eval(func)
	plt.plot([x, x], [0, f(x)], "y-")

