def read_from_file(file_path):
    _file = open(file_path, "r")

    first_col, second_col = [], []
    for line in _file:
        line = line.split()
        first_col.append(int(line[0]))
        second_col.append(int(line[1]))

    return first_col, second_col

def calc_distance(first_array, second_array):
    dist = 0

    first_array.sort()
    second_array.sort()

    assert(len(first_array) == len(second_array))

    for a,b in zip(first_array, second_array):
        dist += abs(a-b)

    return dist

def test(actual, expected):
    if actual == expected:
        print("✅ Test pass")
    else:
        print(f"❌ Test fail, Expected: {expected}, Actual: {actual}")

if __name__ == "__main__":
    file_path = r"puzzle_inputs/day_1.txt"
    first_col, second_col = read_from_file(file_path)
    assert(len(first_col) == len(second_col))

    test(calc_distance([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]), 11)

    print(calc_distance(first_col, second_col))