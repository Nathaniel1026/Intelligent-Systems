import random

# PSO: Find minimum of f(x,y) = x² + y² (answer: 0,0)
particles = [[random.uniform(-5, 5), random.uniform(-5, 5)] for _ in range(3)]
gbest = particles[0][:]

for _ in range(5):
    for p in particles:
        if (p[0]**2 + p[1]**2) < (gbest[0]**2 + gbest[1]**2):
            gbest = p[:]
        p[0] += random.uniform(-0.1, 0.1)
        p[1] += random.uniform(-0.1, 0.1)

print(f"Best 2D Coord: ({gbest[0]:.4f}, {gbest[1]:.4f}), Distance from origin: {(gbest[0]**2+gbest[1]**2)**0.5:.4f}")
