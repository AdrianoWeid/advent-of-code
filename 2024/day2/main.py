with open("i.in", "r") as f:
    reports = []
    for line in f:
        reports.append(line.split())


def part1(reports):
    result = 0
    for report in reports:
        diffs = [int(report[i+1])-int(report[i]) for i in range(len(report)-1)]

        valid = all(1 <= abs(diff) <= 3 for diff in diffs)

        increasing = all(diff > 0 <= 3 for diff in diffs)
        decreasing = all(diff < 0 for diff in diffs)
        if valid and (increasing or decreasing): result += 1
    return result


def part2(reports):
    result = 0
    invalid = []

    def validate(report):

        diffs = [int(report[i+1])-int(report[i]) for i in range(len(report)-1)]
 
        valid = all(1 <= abs(diff) <= 3 for diff in diffs)

        increasing = all(diff > 0 <= 3 for diff in diffs)        
        decreasing = all(diff < 0 for diff in diffs)
        
        return valid and (increasing or decreasing) 

    for i,report in enumerate(reports):
        if validate(report): 
            result += 1
        else:
            invalid.append(i)

    for i in invalid:
        for j in range(len(reports[i])):
            copy = reports[i][:j] + reports[i][j+1:]
            if validate(copy):
                result += 1
                break

    return result

print(part2(reports))

    

