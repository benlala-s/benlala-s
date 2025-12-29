#!/usr/bin/env python3
"""
Bi-objective Traveling Salesman Problem (TSP) Solver using Genetic Algorithm
Adapted for 15 cities

Minimizes:
- f1: Total distance
- f2: Total cost
- F = f1 + f2

Usage:
    python tsp.py

Original project: https://github.com/gregory-chatelier/tsp
"""

import os
import re
from tsp_genetic_algorithm import Parameters, EvolutionaryProcess, TSP, Individual


def load_best_fitness(filename: str = "solution.xml") -> int:
    """Load the best fitness from an existing XML file. Returns -1 if file doesn't exist."""
    if not os.path.exists(filename):
        return -1

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            match = re.search(r'<Fitness>(\d+)</Fitness>', content)
            if match:
                return int(match.group(1))
    except Exception:
        pass

    return -1


def save_solution_xml(individual: Individual, filename: str = "solution.xml") -> None:
    """Save the best solution to an XML file."""
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<TSP_Solutions>

    <Solution id="best">
        <Tour>{individual.get_tour_string()}</Tour>
        <Distance>{individual.distance}</Distance>
        <Cost>{individual.cost}</Cost>
        <Fitness>{individual.fitness}</Fitness>
    </Solution>

</TSP_Solutions>
'''
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(xml_content)


def main():
    print("=" * 70)
    print("BI-OBJECTIVE TRAVELING SALESMAN PROBLEM")
    print("Minimize F = f1 (distance) + f2 (cost)")
    print("=" * 70)
    print()
    print(f"Problem: {len(TSP.cities)} cities")
    print(f"Cities: {', '.join(TSP.cities)}")
    print()

    # Load previous best fitness
    previous_best = load_best_fitness("solution.xml")
    if previous_best > 0:
        print(f"Previous best fitness: {previous_best}")
        print()

    # Configure parameters as per PDF requirements
    Parameters.individuals_nb = 300        # 300 random solutions
    Parameters.generations_max_nb = 500    # 500 iterations
    Parameters.mutations_rate = 0.15       # Swap mutation
    Parameters.crossover_rate = 0.70       # Two-point crossover

    # Run the genetic algorithm
    process = EvolutionaryProcess()
    best = process.run()

    # Save only if better than previous best
    print()
    print("=" * 70)
    if previous_best < 0 or best.fitness < previous_best:
        save_solution_xml(best, "solution.xml")
        if previous_best > 0:
            print(f"NEW BEST FOUND! (improved from {previous_best} to {best.fitness})")
        else:
            print("RESULT SAVED")
        print("=" * 70)
        print(f"Best Tour: {best.get_tour_string()}")
        print(f"Distance (f1): {best.distance}")
        print(f"Cost (f2): {best.cost}")
        print(f"Fitness (F = f1 + f2): {best.fitness}")
    else:
        print(f"NO IMPROVEMENT (current: {best.fitness}, best: {previous_best})")
        print("=" * 70)
        print(f"This run: F={best.fitness} (Distance={best.distance}, Cost={best.cost})")
        print(f"Keeping previous best: F={previous_best}")
    print("=" * 70)

    return best


if __name__ == "__main__":
    main()
