import math

rayon = float(input("Entrer le rayon"));

surface =  3.14 * rayon ** 2

perimetre =  3.14 * rayon * 2


surface_exact =  math.pi * rayon ** 2

perimetre_exact =  math.pi * rayon * 2


print ("le surface est : ", surface, "\n");
print ("le perimetre est : ", perimetre, "\n");

print ("le surface exact est : ", surface_exact, "\n");
print ("le perimetre exact est : ", perimetre_exact, "\n");