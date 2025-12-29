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


def load_solutions(filename: str = "solution.xml") -> tuple:
    """
    Load existing solutions from XML file.
    Returns (best_fitness, list of tours).
    """
    if not os.path.exists(filename):
        return -1, []

    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()

        # Get best fitness
        fitness_match = re.search(r'<BestFitness>(\d+)</BestFitness>', content)
        if not fitness_match:
            # Try old format
            fitness_match = re.search(r'<Fitness>(\d+)</Fitness>', content)

        if not fitness_match:
            return -1, []

        best_fitness = int(fitness_match.group(1))

        # Get all tours
        tours = re.findall(r'<Tour>([^<]+)</Tour>', content)

        return best_fitness, tours
    except Exception:
        return -1, []


def save_solutions_xml(fitness: int, distance: int, cost: int, tours: list, filename: str = "solution.xml") -> None:
    """Save all best solutions to an XML file."""
    solutions_xml = ""
    for i, tour in enumerate(tours, 1):
        solutions_xml += f'''
    <Solution id="{i}">
        <Tour>{tour}</Tour>
        <Distance>{distance}</Distance>
        <Cost>{cost}</Cost>
    </Solution>
'''

    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<TSP_Solutions>
    <BestFitness>{fitness}</BestFitness>
    <TotalSolutions>{len(tours)}</TotalSolutions>
{solutions_xml}
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

    # Load previous best solutions
    previous_best, existing_tours = load_solutions("solution.xml")
    if previous_best > 0:
        print(f"Previous best fitness: {previous_best}")
        print(f"Existing solutions with this fitness: {len(existing_tours)}")
        print()

    # Configure parameters as per PDF requirements
    Parameters.individuals_nb = 300        # 300 random solutions
    Parameters.generations_max_nb = 500    # 500 iterations
    Parameters.mutations_rate = 0.15       # Swap mutation
    Parameters.crossover_rate = 0.70       # Two-point crossover

    # Run the genetic algorithm
    process = EvolutionaryProcess()
    best = process.run()

    new_tour = best.get_tour_string()

    # Determine what to do with the result
    print()
    print("=" * 70)

    if previous_best < 0:
        # First run - save the solution
        save_solutions_xml(best.fitness, best.distance, best.cost, [new_tour])
        print("FIRST SOLUTION SAVED")
        print("=" * 70)
        print(f"Tour: {new_tour}")
        print(f"Distance (f1): {best.distance}")
        print(f"Cost (f2): {best.cost}")
        print(f"Fitness (F): {best.fitness}")

    elif best.fitness < previous_best:
        # New best found - replace all previous solutions
        save_solutions_xml(best.fitness, best.distance, best.cost, [new_tour])
        print(f"NEW BEST FOUND! (improved from {previous_best} to {best.fitness})")
        print("=" * 70)
        print(f"Tour: {new_tour}")
        print(f"Distance (f1): {best.distance}")
        print(f"Cost (f2): {best.cost}")
        print(f"Fitness (F): {best.fitness}")

    elif best.fitness == previous_best:
        # Same fitness - check if it's a new tour
        if new_tour not in existing_tours:
            existing_tours.append(new_tour)
            save_solutions_xml(best.fitness, best.distance, best.cost, existing_tours)
            print(f"NEW TOUR FOUND WITH SAME FITNESS ({best.fitness})!")
            print("=" * 70)
            print(f"New tour: {new_tour}")
            print(f"Total solutions with F={best.fitness}: {len(existing_tours)}")
        else:
            print(f"TOUR ALREADY EXISTS (F={best.fitness})")
            print("=" * 70)
            print(f"Total solutions with F={best.fitness}: {len(existing_tours)}")

    else:
        # Worse than previous best
        print(f"NO IMPROVEMENT (current: {best.fitness}, best: {previous_best})")
        print("=" * 70)
        print(f"This run: F={best.fitness} (Distance={best.distance}, Cost={best.cost})")
        print(f"Keeping {len(existing_tours)} solution(s) with F={previous_best}")

    print("=" * 70)

    return best


if __name__ == "__main__":
    main()
