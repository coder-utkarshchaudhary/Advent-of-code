def read_from_file(file_path):
    _file = open(file_path, "r")

    first_col, second_col = [], []
    for line in _file:
        line = line.split()
        first_col.append(int(line[0]))
        second_col.append(int(line[1]))

    return first_col, second_col

def calc_similarity(first_array, second_array, n):
    similarity = 0
    assert(len(first_array) == len(second_array))

    for i in range(n):
        occurence = 0
        for j in range(n):
            if second_array[j] == first_array[i]:
                occurence+=1

        similarity+=first_array[i]*occurence

    return similarity

def test(actual, expected):
    if actual == expected:
        print("✅ Test pass")
    else:
        print(f"❌ Test fail, Expected: {expected}, Actual: {actual}")

if __name__ == "__main__":
    file_path = r"puzzle_inputs/day_1.txt"
    first_col, second_col = read_from_file(file_path)
    assert(len(first_col) == len(second_col))

    test(calc_similarity([3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3], 6), 31)

    print(calc_similarity(first_col, second_col, 1000))