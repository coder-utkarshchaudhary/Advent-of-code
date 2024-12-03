def parse_array(array):
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

def main(file_path):
    safe = 0
    with open(file_path, "r") as _file:
        for line in _file:
            line = list(map(int, line.split()))
            if parse_array(line):
                safe+=1

    return safe

if __name__ == "__main__":
    file_path = "puzzle_inputs/day_2.txt"
    print(main(file_path))