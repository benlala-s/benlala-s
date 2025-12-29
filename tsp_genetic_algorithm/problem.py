import csv
from typing import List


class TSP:
    """
    Bi-objective Traveling Salesman Problem for 15 cities.
    Minimizes both distance (f1) and cost (f2).
    Fitness F = f1 + f2

    Data is loaded from CSV files.
    """

    cities: List[str] = []
    distances: List[List[int]] = []
    costs: List[List[int]] = []

    @classmethod
    def load_data(cls, distances_file: str = "distances.csv", costs_file: str = "cities.csv") -> None:
        """Load cities, distances and costs from CSV files."""
        # Load distances matrix
        with open(distances_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)  # First row contains: Ville,C1,C2,...,C15
            cls.cities = header[1:]  # Extract city names from header

            cls.distances = []
            for row in reader:
                if row:
                    cls.distances.append([int(val) for val in row[1:]])  # Skip first column (city name)

        # Load costs matrix
        with open(costs_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # Skip header

            cls.costs = []
            for row in reader:
                if row:
                    cls.costs.append([int(val) for val in row[1:]])  # Skip first column (city name)

    @classmethod
    def distance(cls, city1: str, city2: str) -> int:
        """Get the distance between two cities."""
        return cls.distances[cls.cities.index(city1)][cls.cities.index(city2)]

    @classmethod
    def cost(cls, city1: str, city2: str) -> int:
        """Get the cost between two cities."""
        return cls.costs[cls.cities.index(city1)][cls.cities.index(city2)]


# Auto-load data when module is imported
TSP.load_data()
