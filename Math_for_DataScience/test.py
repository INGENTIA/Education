import math

n = 3 # número de lanzamientos
k = 3  # número de caras deseadas
p = 0.5  # probabilidad de obtener cara

# Calcular el coeficiente binomial
coef_binomial = math.comb(n, k)

# Calcular la probabilidad usando la fórmula de la distribución binomial
probabilidad = coef_binomial * (p ** k) * ((1 - p) ** (n - k))

print(f"La probabilidad de obtener 3 caras en 5 lanzamientos es: {probabilidad:.3f}")
