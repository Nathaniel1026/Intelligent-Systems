import random

# MDP: Simple 3-state Value Iteration
# States: 0 (start), 1 (middle), 2 (goal +10 reward)
rewards = {0: 0, 1: 0, 2: 10}
V = {0: 0, 1: 0, 2: 10}
gamma = 0.9

for _ in range(10):
    V[0] = max(V[0], rewards[1] + gamma * V[1])  # go from 0→1
    V[1] = max(V[1], rewards[2] + gamma * V[2])  # go from 1→2

print(f"State Values: S0={V[0]:.2f}, S1={V[1]:.2f}, S2={V[2]:.2f}")
print(f"Agent learns: S0→S1→S2 (goal) is optimal")
