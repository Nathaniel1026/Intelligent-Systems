import random

# GA Real-Life Example: Optimize a work schedule
# Find the best split of 8 work hours between 3 tasks to maximize productivity
# Task productivity: coding=5/hr, meetings=2/hr, emails=3/hr

def productivity(hours):
    return hours[0]*5 + hours[1]*2 + hours[2]*3  # coding, meetings, emails

pop = [[random.randint(0,8), random.randint(0,4), random.randint(0,4)] for _ in range(6)]

for gen in range(15):
    pop.sort(key=lambda h: productivity(h), reverse=True)
    pop = pop[:2]
    for _ in range(4):
        child = [pop[0][0], pop[1][1], pop[0][2]]  # crossover
        child[random.randint(0,2)] += random.choice([-1, 1])  # mutate
        child = [max(0, min(8, h)) for h in child]  # clamp
        pop.append(child)

best = max(pop, key=productivity)
print(f"Best schedule: Coding={best[0]}h, Meetings={best[1]}h, Emails={best[2]}h")
print(f"Total productivity score: {productivity(best)}")
