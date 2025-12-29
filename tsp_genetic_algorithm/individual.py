from __future__ import annotations
import random
from typing import List

from .gene import Gene
from .problem import TSP
from .parameters import Parameters


class Individual(object):
    fitness: int = -1
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
        Create a new individual by crossing over two parents' genomes.
        Uses order crossover (OX) to maintain valid permutations.
        """
        size = len(father.genome)

        # Select a random crossover segment
        start = random.randint(0, size - 1)
        end = random.randint(start + 1, size)

        # Start with empty genome
        child_genome = [None] * size

        # Copy the segment from father
        for i in range(start, end):
            child_genome[i] = Gene(father.genome[i])

        # Fill remaining positions with mother's genes in order
        mother_genes = [Gene(gene) for gene in mother.genome]
        child_set = {str(g) for g in child_genome if g is not None}

        # Get genes from mother that aren't already in child
        remaining = [g for g in mother_genes if str(g) not in child_set]

        # Fill in the blanks
        j = 0
        for i in range(size):
            if child_genome[i] is None:
                child_genome[i] = remaining[j]
                j += 1

        return cls(genome=child_genome, mutate=True)

    def mutate(self) -> None:
        """Apply mutation by swapping two random genes."""
        if random.random() < Parameters.mutations_rate:
            if len(self.genome) >= 2:
                i, j = random.sample(range(len(self.genome)), 2)
                self.genome[i], self.genome[j] = self.genome[j], self.genome[i]

    def evaluate(self) -> None:
        """Calculate the fitness (total distance) of this individual."""
        self.fitness = 0
        for i in range(len(self.genome) - 1):
            self.fitness += self.genome[i].distance(self.genome[i + 1])
        # Add distance to return to the starting city
        self.fitness += self.genome[-1].distance(self.genome[0])

    def __str__(self) -> str:
        route = " -> ".join(str(gene) for gene in self.genome)
        return f"Distance: {self.fitness} km | Route: {route}"
