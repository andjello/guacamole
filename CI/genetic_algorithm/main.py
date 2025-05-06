import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
from deap import base, creator, tools, algorithms
import matplotlib.pyplot as plt

import warnings
from sklearn.exceptions import ConvergenceWarning
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Dummy Dataset (Replace with real coconut milk spray drying data)
X = np.random.rand(100, 4)
y = np.random.rand(100)

# GA will optimize weights for a single hidden layer: (4 inputs * 5 neurons) + 5 biases = 25 genes
N_INPUT = 4
N_HIDDEN = 5
GENE_SIZE = (N_INPUT * N_HIDDEN) + N_HIDDEN

# Evaluation function
def evaluate(individual):
    model = MLPRegressor(hidden_layer_sizes=(N_HIDDEN,), max_iter=1, warm_start=True)
    
    # Run one initial training to initialize weights
    try:
        model.fit(X, y)
        
        # Assign weights
        weights_input_hidden = np.array(individual[:N_INPUT * N_HIDDEN]).reshape(N_INPUT, N_HIDDEN)
        bias_hidden = np.array(individual[N_INPUT * N_HIDDEN:]).reshape(N_HIDDEN)
        
        model.coefs_[0] = weights_input_hidden
        model.intercepts_[0] = bias_hidden
        
        # Leave output weights as-is (optional: optimize those too with more genes)
        preds = model.predict(X)
        mse = mean_squared_error(y, preds)
        return mse,
    except Exception as e:
        return 1e6,

# DEAP setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, -1.0, 1.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=GENE_SIZE)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=0.1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# GA Parameters
POP_SIZE = 30
NGEN = 20
CXPB = 0.7
MUTPB = 0.2

# Track best fitness
best_fitnesses = []

def main():
    population = toolbox.population(n=POP_SIZE)
    print("Starting Genetic Algorithm Optimization...\n")
    
    for gen in range(NGEN):
        offspring = algorithms.varAnd(population, toolbox, cxpb=CXPB, mutpb=MUTPB)
        fits = list(map(toolbox.evaluate, offspring))
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        population = toolbox.select(offspring, k=len(population))
        top_ind = tools.selBest(population, 1)[0]
        best_fitnesses.append(top_ind.fitness.values[0])
        print(f"Generation {gen + 1}: Best MSE = {top_ind.fitness.values[0]:.6f}")
    
    # Final result
    best = tools.selBest(population, 1)[0]
    print("\nBest individual:", best)
    print("Best MSE:", best.fitness.values[0])

    # Plot MSE over generations
    plt.plot(range(1, NGEN + 1), best_fitnesses, marker='o')
    plt.title("Best MSE over Generations")
    plt.xlabel("Generation")
    plt.ylabel("MSE")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
