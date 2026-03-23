import random

# Genetic Algorithm: Find maximum of f(x) = -x^2 + 5 (answer: x=0)
population = [random.uniform(-10, 10) for _ in range(5)]

for gen in range(10):
    population.sort(key=lambda x: -(-x**2 + 5))  # sort by fitness
    parent1, parent2 = population[0], population[1]
    population = [parent1, parent2] + [
        (parent1 + parent2) / 2 + random.uniform(-0.5, 0.5) for _ in range(3)
    ]

best = min(population, key=lambda x: abs(x))
print(f"Best x: {best:.4f}, f(x): {-best**2 + 5:.4f}")
