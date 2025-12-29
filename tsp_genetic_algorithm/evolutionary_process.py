import random
from typing import List

from .individual import Individual
from .parameters import Parameters


class EvolutionaryProcess(object):
    population: List[Individual]
    generation: int
    best_individual: Individual
    best_generation: int

    def __init__(self) -> None:
        self.generation = 0
        self.best_generation = 0
        self.best_individual = None
        self.population = [
            Individual.construct_from_cities()
            for _ in range(Parameters.individuals_nb)
        ]

    def run(self) -> Individual:
        """Run the evolutionary process and return the best individual found."""
        print(f"Starting TSP genetic algorithm with {Parameters.individuals_nb} individuals")
        print(f"Maximum generations: {Parameters.generations_max_nb}")
        print("-" * 60)

        while self.generation < Parameters.generations_max_nb:
            # Evaluate all individuals
            for individual in self.population:
                individual.evaluate()

            # Sort by fitness (lower distance is better)
            self.population.sort(key=lambda ind: ind.fitness)

            # Track the best individual
            current_best = self.population[0]
            if self.best_individual is None or current_best.fitness < self.best_individual.fitness:
                self.best_individual = current_best
                self.best_generation = self.generation
                print(f"Generation {self.generation:4d}: New best found - {current_best.fitness} km")

            # Check if we reached the target fitness
            if Parameters.min_fitness > 0 and current_best.fitness <= Parameters.min_fitness:
                print(f"\nTarget fitness reached at generation {self.generation}!")
                break

            # Create next generation
            self.population = self.next_generation()
            self.generation += 1

        print("-" * 60)
        print(f"\nBest solution found at generation {self.best_generation}:")
        print(self.best_individual)

        return self.best_individual

    def next_generation(self) -> List[Individual]:
        """Create the next generation through selection and reproduction."""
        new_population = []

        # Elitism: keep the best individual
        new_population.append(self.population[0])

        # Fill the rest with offspring
        while len(new_population) < Parameters.individuals_nb:
            if random.random() < Parameters.crossover_rate:
                # Crossover: select two parents and create offspring
                father = self.select()
                mother = self.select()
                offspring = Individual.construct_from_parents(father, mother)
            else:
                # No crossover: just copy and mutate
                parent = self.select()
                offspring = Individual.construct_from_father(parent)

            new_population.append(offspring)

        return new_population

    def select(self) -> Individual:
        """
        Select an individual using tournament selection.
        Tournament selection is more suitable for larger problems than roulette wheel.
        """
        tournament_size = min(5, len(self.population))
        tournament = random.sample(self.population, tournament_size)
        tournament.sort(key=lambda ind: ind.fitness)
        return tournament[0]
