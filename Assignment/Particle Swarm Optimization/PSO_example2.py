import random

# PSO Real-Life Example: Find cheapest store location
# Customers at positions: (2,3), (5,1), (8,6), (1,7)
# Minimize total distance from store to all customers

customers = [(2,3), (5,1), (8,6), (1,7)]

def total_distance(pos):
    return sum(((pos[0]-cx)**2 + (pos[1]-cy)**2)**0.5 for cx, cy in customers)

particles = [[random.uniform(0,10), random.uniform(0,10)] for _ in range(5)]
gbest = min(particles, key=total_distance)[:]

for _ in range(30):
    for p in particles:
        if total_distance(p) < total_distance(gbest):
            gbest = p[:]
        p[0] += random.uniform(-0.3, 0.3) * (gbest[0] - p[0])
        p[1] += random.uniform(-0.3, 0.3) * (gbest[1] - p[1])

print(f"Best store location: ({gbest[0]:.2f}, {gbest[1]:.2f})")
print(f"Total distance to all customers: {total_distance(gbest):.2f}")
