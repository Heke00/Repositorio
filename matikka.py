import math
#print(math.pi)

#potenssi on **

lukupi = 3.141596
sade = 4
mittayksikko = ("cm")
print("Ympyrän piiri on", lukupi*2*sade, mittayksikko)

print("Ympyrän pinta-ala on", sade*sade*lukupi, mittayksikko,"^2")

luku1 = 2
luku2 = '2'
luku3 = "2"
luku4 = 2.0
booli = True

print(type(luku1), type(luku2), type(luku3), type(booli), sep=" | ")

print(luku4 ** 5)