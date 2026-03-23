# Intelligent Systems — Assignment

## Algorithms Overview

### 1. Genetic Algorithm (GA)
- **Inspired by**: Natural evolution (survival of the fittest)
- **How it works**: Maintains a population of candidate solutions. The best ones are selected, combined (crossover), and randomly tweaked (mutation) to produce the next generation. Over time, the population evolves toward better solutions.
- **Good for**: Optimization problems (finding max/min of functions, evolving patterns)

### 2. Particle Swarm Optimization (PSO)
- **Inspired by**: Flocking birds / schooling fish
- **How it works**: A group of "particles" fly around the search space. Each particle remembers its personal best position and is attracted toward the global best found by any particle. Over time, the swarm converges on the optimal solution.
- **Good for**: Continuous optimization (finding coordinates that minimize/maximize a function)

### 3. Markov Decision Process (MDP)
- **Inspired by**: Sequential decision-making under uncertainty
- **How it works**: Defines states, actions, rewards, and transitions. Uses Value Iteration to compute the best action at each state by propagating future rewards backward. The result is an optimal policy (a map of "what to do" at every state).
- **Good for**: Navigation, robotics, game AI, any problem with a sequence of decisions

```
