from typing import List


class TSP:
    """
    Traveling Salesman Problem configuration for 15 cities.
    Data loaded from the provided CSV files.
    """

    # List of 15 cities
    cities: List[str] = [
        "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
        "C9", "C10", "C11", "C12", "C13", "C14", "C15",
    ]

    # Distance matrix (15x15) - symmetric matrix
    # distances[i][j] = distance from city i to city j
    distances: List[List[int]] = [
        [0, 12, 18, 25, 30, 22, 28, 35, 40, 26, 34, 45, 38, 42, 50],   # C1
        [12, 0, 14, 20, 24, 18, 22, 30, 34, 20, 28, 38, 32, 36, 44],   # C2
        [18, 14, 0, 16, 22, 15, 20, 28, 32, 18, 26, 36, 30, 34, 42],   # C3
        [25, 20, 16, 0, 14, 18, 16, 22, 26, 20, 24, 32, 28, 30, 38],   # C4
        [30, 24, 22, 14, 0, 12, 18, 20, 24, 22, 26, 30, 28, 26, 34],   # C5
        [22, 18, 15, 18, 12, 0, 10, 18, 22, 16, 20, 28, 24, 26, 32],   # C6
        [28, 22, 20, 16, 18, 10, 0, 12, 18, 14, 16, 24, 22, 24, 30],   # C7
        [35, 30, 28, 22, 20, 18, 12, 0, 14, 16, 18, 22, 20, 22, 26],   # C8
        [40, 34, 32, 26, 24, 22, 18, 14, 0, 12, 14, 20, 18, 20, 24],   # C9
        [26, 20, 18, 20, 22, 16, 14, 16, 12, 0, 10, 18, 16, 18, 22],   # C10
        [34, 28, 26, 24, 26, 20, 16, 18, 14, 10, 0, 14, 12, 14, 18],   # C11
        [45, 38, 36, 32, 30, 28, 24, 22, 20, 18, 14, 0, 10, 12, 16],   # C12
        [38, 32, 30, 28, 28, 24, 22, 20, 18, 16, 12, 10, 0, 8, 12],    # C13
        [42, 36, 34, 30, 26, 26, 24, 22, 20, 18, 14, 12, 8, 0, 10],    # C14
        [50, 44, 42, 38, 34, 32, 30, 26, 24, 22, 18, 16, 12, 10, 0],   # C15
    ]

    @classmethod
    def distance(cls, city1: str, city2: str) -> int:
        """Get the distance between two cities."""
        return cls.distances[cls.cities.index(city1)][cls.cities.index(city2)]
