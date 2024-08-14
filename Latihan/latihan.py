import random

# Fungsi untuk menghitung nilai fitness
def fitness_function(x):
    return -(x**2) + 10

# Fungsi untuk membuat populasi awal
def create_initial_population(population_size):
    return [random.uniform(0, 31) for _ in range(population_size)]

# Fungsi untuk melakukan seleksi orangtua berdasarkan turnamen
def selection(population, fitness_values, tournament_size):
    selected_parents = []
    for _ in range(len(population)):
        tournament = random.sample(list(zip(population, fitness_values)), tournament_size)
        winner = max(tournament, key=lambda x: x[1])
        selected_parents.append(winner[0])
    return selected_parents

# Fungsi crossover satu titik
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Fungsi mutasi
def mutation(child, mutation_rate):
    for i in range(len(child)):
        if random.random() < mutation_rate:
            child[i] = random.uniform(0, 31)
    return child

# Algoritma genetika
def genetic_algorithm(population_size, num_generations, tournament_size, mutation_rate):
    population = create_initial_population(population_size)
    for _ in range(num_generations):
        fitness_values = [fitness_function(x) for x in population]

        # Seleksi
        selected_parents = selection(population, fitness_values, tournament_size)

        # Crossover
        next_generation = []
        for i in range(0, population_size, 2):
            child1, child2 = crossover(selected_parents[i], selected_parents[i+1])
            next_generation.extend([child1, child2])

        # Mutasi
        next_generation = [mutation(child, mutation_rate) for child in next_generation]

        population = next_generation

    # Mengembalikan solusi terbaik dari populasi terakhir
    best_solution = max(population, key=fitness_function)
    return best_solution

# Parameter algoritma genetika
population_size = 100
num_generations = 100
tournament_size = 5
mutation_rate = 0.1

# Menjalankan algoritma genetika
best_solution = genetic_algorithm(population_size, num_generations, tournament_size, mutation_rate)
print("Solusi terbaik:", best_solution)
print("Nilai maksimum fungsi fitness:", fitness_function(best_solution))
