import numpy as np
from itertools import combinations, islice
from multiprocessing import Pool, cpu_count
import progressbar

def volume_of_tetrahedron(p1, p2, p3, p4):
    # Convert points to numpy arrays
    p1, p2, p3, p4 = map(np.array, [p1, p2, p3, p4])
    
    # Vectors from p1 to p2, p3, and p4
    AB = p2 - p1
    AC = p3 - p1
    AD = p4 - p1

    # Cross product of AB and AC
    cross_product = np.cross(AB, AC)

    # Scalar triple product
    scalar_triple_product = np.dot(cross_product, AD)

    # The volume of the tetrahedron
    volume = abs(scalar_triple_product) / 6.0
    return volume

def convert_to_tuple(line):
    line = line.strip().strip('()')
    parts = line.split(',')
    return (float(parts[0]), float(parts[1]), float(parts[2]), int(parts[3]))

def parse_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines if line.strip()]
    return {convert_to_tuple(line): idx for idx, line in enumerate(lines)}

def test_func(tetra):
    p1, p2, p3, p4 = tetra
    if p1[-1] + p2[-1] + p3[-1] + p4[-1] == 100:
        volume = volume_of_tetrahedron(p1[:-1], p2[:-1], p3[:-1], p4[:-1])
        return (tetra, volume)
    return (tetra, float('inf'))

def get_smallest_volume(data):
    points = list(data.keys())
    combo = combinations(points, 4)

    min_volume = float('inf')
    min_points = None

    num_combinations = len(points) * (len(points) - 1) * (len(points) - 2) * (len(points) - 3) // 24
    chunk_size = 1000  # Adjust the chunk size based on your system's memory capacity

    with progressbar.ProgressBar(max_value=num_combinations) as bar:
        with Pool(cpu_count()) as pool:
            processed = 0
            while processed < num_combinations:
                chunk = list(islice(combo, chunk_size))
                if not chunk:
                    break

                results = pool.map(test_func, chunk)

                for tetra, volume in results:
                    if volume < min_volume:
                        min_volume = volume
                        min_points = tetra

                processed += len(chunk)
                bar.update(processed)

    return min_points

def challenge(filepath):
    data = parse_file(filepath)
    min_points = get_smallest_volume(data)

    if min_points is None:
        return []

    indices = {tuple(p[:-1]): idx for p, idx in data.items()}

    result = [
        indices[tuple(min_points[0][:-1])],
        indices[tuple(min_points[1][:-1])],
        indices[tuple(min_points[2][:-1])],
        indices[tuple(min_points[3][:-1])]
    ]

    return result

if __name__ == '__main__':
    c1 = challenge('./points_small.txt')
    print(f"Small Text Indices: {c1}")

    c2 = challenge('./points_large.txt')
    print(f"Large Text Indices: {c2}")
