def create_cases(test_values):
    def helper(index, expression):
        # Base case: If at the end of the list, store the expression
        if index == len(test_values):
            expressions.append(expression)
            return
        
        helper(index + 1, f"{expression}*{test_values[index]}")
        helper(index + 1, f"{expression}+{test_values[index]}")
        helper(index + 1, f"{expression}|{test_values[index]}")

    
    # Initialize the list to store expressions
    expressions = []
    helper(1, str(test_values[0]))
    return expressions

def solve_expressions(expression):
    tokens = []
    num = ""
    
    for char in expression:
        if char.isdigit():
            num += char
        else:
            tokens.append(int(num))
            tokens.append(char)
            num = ""
    tokens.append(int(num))
    
    result = tokens[0]
    i = 1
    while i < len(tokens):
        operator = tokens[i]
        operand = tokens[i + 1]
        if operator == "+":
            result += operand
        elif operator == "*":
            result *= operand
        elif operator == "|":
            result = int(str(result) + str(operand))
        i += 2
    
    return result

def valid_calibration(expected_val, test_values):
    expressions = create_cases(test_values)
    for expression in expressions:
        if solve_expressions(expression) == expected_val:
            return True
        
    return False

def main(file_path):
    _file = open(file_path, "r").readlines()
    _sum = 0
    for line in _file:
        line = line.strip().split()
        line[0] = line[0][:-1]
        line = list(map(int, line))
        if valid_calibration(line[0], line[1:]):
            _sum+=line[0]

    return(_sum)

if __name__ == "__main__":
    file_path = "puzzle_inputs/day_7.txt"
    print(main(file_path))