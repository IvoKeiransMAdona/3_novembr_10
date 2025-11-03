import math
# Ievade
a = float(input("Ievadi a: 1"))
b = float(input("Ievadi b: 1"))
c = float(input("Ievadi c: 1")) #trukst iekavas

# Diskriminants
D = b**2 - 4*a*c

# Sakņu aprēķins
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a) # nepareiza mainiga nosakums
    print(f"D = {D}, divas saknes: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2*a)
    print(f"D = {D}, viena sakne: x = {x}")  #iztrukst pedinas
else:
    print(f"D = {D}, nav reālu sakņu.")
