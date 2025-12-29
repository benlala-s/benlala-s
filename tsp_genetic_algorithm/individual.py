from __future__ import annotations
import random
from typing import List

from .gene import Gene
from .problem import TSP
from .parameters import Parameters


class Individual(object):
    fitness: int = -1      # F = f1 + f2
    distance: int = -1     # f1: total distance
    cost: int = -1         # f2: total cost
    genome: List[Gene]

    def __init__(self, genome: List[Gene], mutate: bool = False) -> None:
        self.genome = genome
        if mutate:
            self.mutate()

    @classmethod
    def construct_from_cities(cls) -> Individual:
        """Create a new individual with a random ordering of cities."""
        cities = TSP.cities[:]
        random.shuffle(cities)
        return cls(genome=[Gene(city) for city in cities])

    @classmethod
    def construct_from_father(cls, father: Individual) -> Individual:
        """Create a new individual by copying the father's genome with possible mutation."""
        return cls(genome=[Gene(gene) for gene in father.genome], mutate=True)

    @classmethod
    def construct_from_parents(cls, father: Individual, mother: Individual) -> Individual:
        """
        Create a new individual using two-point crossover.
        When a city appears more than once, it is replaced by a missing city.
        """
        size = len(father.genome)

        # Select two random crossover points
        point1 = random.randint(1, size - 2)
        point2 = random.randint(point1 + 1, size - 1)

        # Start with father's genome
        child_genome = [Gene(gene) for gene in father.genome]

        # Copy segment from mother between point1 and point2
        for i in range(point1, point2):
            child_genome[i] = Gene(mother.genome[i])

        # Find duplicates and missing cities
        cities_in_child = [str(g) for g in child_genome]
        all_cities = set(TSP.cities)

        # Find which cities appear more than once and which are missing
        seen = set()
        duplicates = []
        for i, city in enumerate(cities_in_child):
            if city in seen:
                duplicates.append(i)
            else:
                seen.add(city)

        missing = list(all_cities - seen)
        random.shuffle(missing)

        # Replace duplicates with missing cities
        for i, dup_idx in enumerate(duplicates):
            child_genome[dup_idx] = Gene(missing[i])

        return cls(genome=child_genome, mutate=True)

    def mutate(self) -> None:
        """Apply mutation by swapping two random genes (swap mutation)."""
        if random.random() < Parameters.mutations_rate:
            if len(self.genome) >= 2:
                i, j = random.sample(range(len(self.genome)), 2)
                self.genome[i], self.genome[j] = self.genome[j], self.genome[i]

    def evaluate(self) -> None:
        """
        Calculate the bi-objective fitness.
        f1 = total distance
        f2 = total cost
        F = f1 + f2
        """
        self.distance = 0  # f1
        self.cost = 0      # f2

        for i in range(len(self.genome) - 1):
            self.distance += self.genome[i].distance(self.genome[i + 1])
            self.cost += self.genome[i].cost(self.genome[i + 1])

        # Add return to starting city
        self.distance += self.genome[-1].distance(self.genome[0])
        self.cost += self.genome[-1].cost(self.genome[0])

        # Combined fitness F = f1 + f2
        self.fitness = self.distance + self.cost

    def get_tour_string(self) -> str:
        """Get the tour as a comma-separated string (for XML output)."""
        cities = [str(gene) for gene in self.genome]
        cities.append(cities[0])  # Return to start
        return ",".join(cities)

    def __str__(self) -> str:
        route = " -> ".join(str(gene) for gene in self.genome)
        start = str(self.genome[0])
        return f"F={self.fitness} (Distance={self.distance}, Cost={self.cost}) | {route} -> {start}"
