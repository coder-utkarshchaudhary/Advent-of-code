def safe_hai(array):
    dec = False
    if array[0] - array[1] in [1,2,3]:
        dec = True
    elif array[0] - array[1] in [-1,-2,-3]:
        dec = False
    else:
        return False
    
    if dec:
        for i in range(1,len(array)-1):
            if array[i] - array[i+1] in [1,2,3]:
                continue
            else:
                return False
            
        return True
    
    else:
        for i in range(1,len(array)-1):
            if array[i] - array[i+1] in [-1,-2,-3]:
                continue
            else:
                return False
            
        return True
    
def sahi_mein_safe_hai(array):
    if safe_hai(array):
        return True
    for i in range(len(array)):
        if safe_hai(array[:i] + array[i+1:]):
            return True
    return False
    
def test(test_case_ip, test_case_op):
    safe = 0
    with open(test_case_ip, "r") as _file:
        for line in _file:
            line = list(map(int, line.split()))
            if sahi_mein_safe_hai(line):
                safe+=1
                print(line)

    return safe == test_case_op

def main(file_path):
    safe = 0
    with open(file_path, "r") as _file:
        for line in _file:
            line = list(map(int, line.split()))
            if sahi_mein_safe_hai(line):
                safe+=1

    return safe

if __name__ == "__main__":
    file_path = "puzzle_inputs/day_2.txt"
    test_case_ip = "puzzle_inputs/day_2_2_test.txt"
    print(test(test_case_ip, 4))
    print(main(file_path))