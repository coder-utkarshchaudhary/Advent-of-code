import re

def main(file_path):
    with open(file_path, "r") as _file:
        line = _file.read().strip()

        matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", line)
        enabled = True

        ans = 0
        for match in matches:
            if match[2] == "" and enabled:
                ans += int(match[0]) * int(match[1])
            else:
                if match[2] == "do()":
                    enabled = True
                else:
                    enabled = False

        return ans
    
if __name__ == "__main__":
    file_path = "puzzle_inputs/day_3.txt"
    print(main(file_path))