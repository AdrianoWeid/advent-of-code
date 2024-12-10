import re
with open("in.txt", "r") as f:
    text = f.read()

def part1(text):
    numbers = re.findall(r"mul\((\d+),(\d+)\)", text)

    sum = sum(int(x) * int(y) for x,y in numbers)
    return sum


def part2(text):
    pattern = re.compile(r"mul\((?P<x>\d+),(?P<y>\d+)\)|(?P<do>do\(\))|(?P<dont>don't\(\))")
    instructions = pattern.finditer(text)
    enabled = True
    result = 0
    
    for instruction in instructions:
        if instruction.group("dont"):
            enabled = False

        elif instruction.group("do"):
            enabled = True

        else:
            if enabled and instruction.group("x") and instruction.group("y"):
                result += int(instruction.group("x")) * int(instruction.group("y"))
        print(instruction.groupdict())
    return result

print(part2(text))