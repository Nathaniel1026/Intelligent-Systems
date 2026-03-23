import random

# MDP Real-Life Example: Robot delivery in a small office
# States: Reception(0) → Hallway(1) → Office(2, deliver +10)
#         Hallway(1) can also lead to Kitchen(3, wrong room -5)
# Agent learns: always go toward Office, avoid Kitchen

V = {0: 0, 1: 0, 2: 10, 3: -5}  # state values
gamma = 0.9

# Value Iteration: propagate rewards backward
for _ in range(10):
    V[1] = max(V[2], V[3]) * gamma        # from hallway: choose office or kitchen
    V[0] = V[1] * gamma                    # from reception: go to hallway

policy = {0: "go to Hallway", 1: "go to Office" if V[2] > V[3] else "go to Kitchen"}

print(f"State values: Reception={V[0]:.2f}, Hallway={V[1]:.2f}, Office={V[2]:.2f}, Kitchen={V[3]:.2f}")
print(f"Optimal policy:")
print(f"  At Reception → {policy[0]}")
print(f"  At Hallway   → {policy[1]}")
