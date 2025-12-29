from typing import List


class TSP:
    """
    Traveling Salesman Problem configuration for 15 cities.

    This is a template - update the cities list and distances matrix
    with your actual data from the CSV files.
    """

    # List of 15 cities (to be updated with actual city names from CSV)
    cities: List[str] = [
        "City_01",
        "City_02",
        "City_03",
        "City_04",
        "City_05",
        "City_06",
        "City_07",
        "City_08",
        "City_09",
        "City_10",
        "City_11",
        "City_12",
        "City_13",
        "City_14",
        "City_15",
    ]

    # Distance matrix (15x15) - to be updated with actual distances from CSV
    # This is a symmetric matrix where distances[i][j] = distance from city i to city j
    distances: List[List[int]] = [
        [0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400],
        [100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300],
        [200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200],
        [300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100],
        [400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000],
        [500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800, 900],
        [600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700, 800],
        [700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600, 700],
        [800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500, 600],
        [900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400, 500],
        [1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300, 400],
        [1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200, 300],
        [1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100, 200],
        [1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0, 100],
        [1400, 1300, 1200, 1100, 1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 0],
    ]

    @classmethod
    def distance(cls, city1: str, city2: str) -> int:
        """Get the distance between two cities."""
        return cls.distances[cls.cities.index(city1)][cls.cities.index(city2)]

    @classmethod
    def load_from_csv(cls, cities_file: str, distances_file: str) -> None:
        """
        Load cities and distances from CSV files.

        Args:
            cities_file: Path to CSV file containing city names
            distances_file: Path to CSV file containing distance matrix
        """
        import csv

        # Load cities
        with open(cities_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            cls.cities = [row[0].strip() for row in reader if row]

        # Load distances
        with open(distances_file, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            cls.distances = [[int(float(val)) for val in row] for row in reader if row]
