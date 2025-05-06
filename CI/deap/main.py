import random
import numpy as np
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

# Define the evaluation function (maximize x * sin(x))
def eval_func(individual):
    x = individual[0]
    return x * np.sin(x),  # Comma makes it a tuple (required by DEAP)

# Set up DEAP framework
creator.create("FitnessMax", base.Fitness, weights=(1.0,))  # Maximize
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()

# Attribute generator: float between 0 and 10
toolbox.register("attr_float", random.uniform, 0, 10)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, 1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the genetic operators
toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.1)
toolbox.register("select", tools.selTournament, tournsize=3)

# Genetic Algorithm parameters
population = toolbox.population(n=50)
NGEN = 30
CXPB = 0.7  # Crossover probability
MUTPB = 0.2  # Mutation probability

# Statistics to observe progress
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("avg", np.mean)
stats.register("max", np.max)

# Run the Genetic Algorithm
pop, log = algorithms.eaSimple(population, toolbox, cxpb=CXPB, mutpb=MUTPB,
                               ngen=NGEN, stats=stats, verbose=True)

# Print the best solution
top_ind = tools.selBest(pop, 1)[0]
print(f"\nBest Individual: {top_ind}")
print(f"Best Fitness (x * sin(x)): {top_ind.fitness.values[0]}")

# Optional: plot fitness over generations
gen = log.select("gen")
fit_max = log.select("max")

plt.plot(gen, fit_max, label='Max Fitness')
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Fitness over Generations")
plt.grid()
plt.legend()
plt.show()
