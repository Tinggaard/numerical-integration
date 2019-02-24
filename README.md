# Numerisk Integration
Her ligger kildekoden til det jeg har lavet i forbindelse med SO6 arbejdet om numerisk integration.

___

# Brug
Først og fremest kræver koden at man har matplotlib biblioteket installeret (tjekkes ved at køre `pip show matplotlib` i dit systems terminal).

Filen matematik.py er filen alting køres fra, den anden er blot funktionerne - jeg har adskilt dem, da jeg synes det virkede mere overskueligt.

Jeg vil anbefale at udkommentere nogle af kodeblokkene inden man kører programmet, da det ellers godt kan give lidt uventede outputs.

## Argumenter
Sum metoderne tager 5 (6) inputs, de første 3 er obligatoriske. De består af:
1. `func`, funktionsforskriften, angivet som `str`
2. `start`, en startværdi for integralet, angivet som `int` eller `float`.
3. `end`, en slutværdi for integralet, angivet som `int` eller `float`.
4. `n`, antal intervaller, angivet som `int`

   Hvis ikke andet er angivet, er antallet af intervaller `10`
5. `animate`, om metoden skal animeres til matplotlib.pyplot biblioteket, angivet som `bool`

   Hvis ikke andet er angivet, animeres metoden (værdi sat til `True`)
6. `plt`, hvilken "extension", funktionen skal kaldes til - er kun brugt idet der skal plottes mere end 1 plot i samme vindue, angivet som `module`

   Hvis ikke andet er angivet, er denne værdi lig med `plt`
   
Da Simpsons metoden ikke har `plt` som argument og jeg stort set ikke har brugt det, vil jeg sige at min funktion tager 5 argumenter.

## Returværdi
Alle sum metoderne returnerer en liste bestående af de forskellige arealer for intervallerne. (Ved Simpsons er der halvt så mange som `n`).
For at finde det samlede areal bruges blot funktionen `sum()`


## Eksempel brug
```python
from integration import *
start = 0
end = 8
n = 6
funktion = "x**2-5*x+7-math.sin(x)"

plot(funktion, start, end)
simpsons = simpsons(funktion, start, end, n)
grid()

print("Ved {} intervaller, får Simpsons metode arealet under {}, mellem {} og {} til at være {}".format(n, funktion, start, end, sum(simpsons)))

show()
```
Programmet returnerer derefer
```python
> Ved 6 intervaller, får Simpsons metode arealet under x**2-5*x+7-math.sin(x), mellem 0 og 8 til at være 65.49582610521499
```
Samt dette billede:

![Billede af et retur eksempel](https://github.com/Tinggaard/numerical-integration/blob/master/retur%20eksempel.png "Retur eksempel")

___

# Photos
Jeg har lagt alle billeder fra rapporten ind i mappen [photos](/photos), da jeg tænkte at det kan være rart nok at kunne se dem i stor størrelse.
___


# Licens
Koden er licenceret under [GPL-3.0](/LICENSE)
