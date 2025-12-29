#!/usr/bin/env python3
"""
Traveling Salesman Problem (TSP) Solver using Genetic Algorithm
Adapted for 15 cities

Usage:
    python tsp.py                           # Run with default placeholder data
    python tsp.py cities.csv distances.csv  # Run with data from CSV files

Original project: https://github.com/gregory-chatelier/tsp
"""

import sys
from tsp_genetic_algorithm import Parameters, EvolutionaryProcess, TSP


def main():
    # Check if CSV files are provided as arguments
    if len(sys.argv) == 3:
        cities_file = sys.argv[1]
        distances_file = sys.argv[2]
        print(f"Loading data from CSV files:")
        print(f"  Cities: {cities_file}")
        print(f"  Distances: {distances_file}")
        print()
        TSP.load_from_csv(cities_file, distances_file)
    elif len(sys.argv) != 1:
        print("Usage: python tsp.py [cities.csv distances.csv]")
        sys.exit(1)

    print(f"TSP Problem: {len(TSP.cities)} cities")
    print(f"Cities: {', '.join(TSP.cities)}")
    print()

    # Configure parameters for 15 cities
    # These can be adjusted for better performance
    Parameters.individuals_nb = 100
    Parameters.generations_max_nb = 500
    Parameters.mutations_rate = 0.15
    Parameters.crossover_rate = 0.70

    # Run the genetic algorithm
    process = EvolutionaryProcess()
    best = process.run()

    return best


if __name__ == "__main__":
    main()
