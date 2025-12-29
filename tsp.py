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

from tsp_genetic_algorithm import Parameters, EvolutionaryProcess, TSP, Individual


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
    print(f"\nSolution saved to {filename}")


def main():
    print("=" * 70)
    print("BI-OBJECTIVE TRAVELING SALESMAN PROBLEM")
    print("Minimize F = f1 (distance) + f2 (cost)")
    print("=" * 70)
    print()
    print(f"Problem: {len(TSP.cities)} cities")
    print(f"Cities: {', '.join(TSP.cities)}")
    print()

    # Configure parameters as per PDF requirements
    Parameters.individuals_nb = 300        # 300 random solutions
    Parameters.generations_max_nb = 500    # 500 iterations
    Parameters.mutations_rate = 0.15       # Swap mutation
    Parameters.crossover_rate = 0.70       # Two-point crossover

    # Run the genetic algorithm
    process = EvolutionaryProcess()
    best = process.run()

    # Save best solution to XML
    save_solution_xml(best, "solution.xml")

    # Print final summary
    print()
    print("=" * 70)
    print("FINAL RESULT")
    print("=" * 70)
    print(f"Best Tour: {best.get_tour_string()}")
    print(f"Distance (f1): {best.distance}")
    print(f"Cost (f2): {best.cost}")
    print(f"Fitness (F = f1 + f2): {best.fitness}")
    print("=" * 70)

    return best


if __name__ == "__main__":
    main()
