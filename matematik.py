# Alle funktionerne
from integration import *
# Brugt til at lave lidt tweaks som titel på et plot osv.
from matplotlib import pyplot as plt

############### Subplots - billede til forside ##############
start, end, n = 0, 10, 5
func = "0.2*x**2"
p, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')

plots = [ax1, ax2, ax3, ax4]
funktioner = [sum_left, sum_right, sum_middle, sum_trapez]
navne = ["Venstresum: ", "Højresum: ", "Midtsum: ", "Trapezsum: "]

for plottet, funktion, navn in zip(plots, funktioner, navne):
    plot(func, start, end, "r-", plt=plottet)
    summen = funktion(func, start, end, n=n, plt=plottet)
    plottet.set_title(navn + str(sum(summen)))
    plottet.grid()  
show()



####################### Enkelte plots #######################
# 0..10 = 66.67
poly = "0.2*x**2"
# 2..5 = 7.4
expo = "(2**x)-(x**2)+2"
# 0..5 = 8.19
sin = "math.sin((x**2)/2)+1.5"
# 0..10 = 30
eks = "(math.pi**2/20)*x*math.sin((math.pi/20)*x)+1"
# 0..2 = math.pi
cirkel = "math.sqrt(4-x**2)"
# 0..9 = 18
sqrt = "math.sqrt(x)"
# 0..8 = 26.81512308
advanced = "math.e*math.sin(x)**2 + x / 5 + math.log(math.pi * x + 2) - 0.1*math.sqrt(math.e**x)"


######################## plot af integral ########################
plot(advanced, start, end)
simp = simpsons(advanced, start, end, n)
plt.text(0.5 * (start + end), 1.3, r"$\int_0^8 e \cdot \sin^2({x}) + \frac {x} {5} + \ln ({\pi \cdot x + 2}) - \frac {\sqrt {e^x}} {10}  \mathrm{d}x$",horizontalalignment='center', fontsize=14)
x_eq(advanced, start)
x_eq(advanced, end)



###################### Sammenligning af metoderne #################
start, end, n = 0, 8, 10
actual = 26.81512308
decimaler = 10
funktion = advanced

left = sum_left(funktion, start, end, n, False)
right = sum_right(funktion, start, end, n, False)
middle = sum_middle(funktion, start, end, n, False)
trap = sum_trapez(funktion, start, end, n, False)
simp = simpsons(funktion, start, end, n, False)

###### Brugt til at visualisere en enkelt funktion, hvis jeg har følt behovet.
# plot(funktion, start, end)
# grid()
# show()


navne = ["Venstresum", "Højresum", "Midtsum", "Trapezsum", "Simpsons"]

alle = [sum(left), sum(right), sum(middle), sum(trap), sum(simp)]
afvigelser = [actual-metode for metode in alle]
procenter = [abs((afvigelse/actual)*100) for afvigelse in afvigelser]


print("De forskellige metoder ved {} intervaller for funktionen '{}', ved intervallerne {} til {}\n".format(n, funktion, start, end))

for navn, afvigelse, procent in zip(navne, afvigelser, procenter):
    print("{} har en afvigelse på {}, hvilket svarer til {}%".format(navn, round(afvigelse,decimaler), round(procent,decimaler)))

