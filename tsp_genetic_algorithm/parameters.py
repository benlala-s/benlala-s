class Parameters(object):
    # Population and algorithm parameters
    individuals_nb: int = 100              # Number of individuals per generation (increased for 15 cities)
    generations_max_nb: int = 500          # Maximum number of generations (increased for 15 cities)
    initial_genes_nb: int = 15             # Initial number of genes (15 cities)
    min_fitness: int = 0                   # Target fitness value
    # Reproduction rates
    mutations_rate: float = 0.15           # Mutation rate (slightly increased for larger problem)
    mutations_add_rate: float = 0.20       # Gene addition rate
    mutation_delete_rate: float = 0.10     # Gene deletion rate
    crossover_rate: float = 0.70           # Crossover rate (slightly increased)
