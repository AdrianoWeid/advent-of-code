with open("in.txt", "r") as f:
    L = []
    R = []
    for line in f:
        L.append(int(line.split()[0]))
        R.append(int(line.split()[1]))


def part1(l, r):
    l.sort(), r.sort()
    result = 0
    for i in range(len(l)):
       result += abs(r[i] - l[i])

    return result

def part2(L, R):
    score = {}
    result = 0
    for number in R:
        if number in L:
            if number not in score:
                score[number] = 0
            score[number] += 1

    for number in L:
        if number in score:
             result += number * score[number]
    
    return result



print(part2(L,R)) 