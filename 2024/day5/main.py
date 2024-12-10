with open("in.txt", "r") as f:
    rules= []
    seiten = []
    for line in f:
        line = line.strip()
        if "|" in line:
            left, right = line.split("|")
            rules.append([int(left), int(right)])
        elif "," in line:
            seiten.append([int(x) for x in line.split(",")])
        else:
            # Leere Zeilen ignorieren
            pass

    
    
    def is_valid(update_line, rules):
        for x,y in rules:
            if x in update_line and y in update_line:
                if update_line.index(x) > update_line.index(y):
                    return False
        return True

    invalid_lines = [] 
    for line in seiten:
        if not is_valid(line, rules):
            invalid_lines.append(line)

    result = 0 
    for line in invalid_lines:
        changed = True
        while changed:
            changed = False
            for x, y in rules:
                if x in line and y in line:
                    i1 = line.index(x)
                    i2 = line.index(y)
                    
                    if i1 > i2:
                        line[i1], line[i2] = line[i2], line[i1]
                        changed = True

        middle_index = int(len(line)//2)
        result += line[middle_index]

    
    print(result)