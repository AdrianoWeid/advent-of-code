text = []
with open("in.txt", "r") as f:
    for line in f:
        text.append(line)


def part1(grid, word="XMAS"):
    rows = len(text) 
    cols = len(text[0])
    word_len = len(word)
    directions = [
        (0, 1), # nach rechts
        (0, -1), # nach links
        (1, 0), # nach unten
        (-1, 0), # nach oben
        (1, 1), # oben rechts
        (-1, -1), # unten links
        (1, -1), # unten links
        (-1, 1) # oben rechts 
    ]

    def in_bound(x, y):
        return 0 <= x < rows and 0 <= y < cols

    count = 0
    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for k in range(word_len):
                    nr, nc = r + k * dr, c + k * dc
                    if not in_bound(nr, nc) or grid[nr][nc] != word[k]:
                        found = False
                if found:
                    count += 1
    return count

def part2(grid, word="MAS"):
    rows = len(text) 
    cols = len(text[0])

    def in_bound(x, y):
        return 0 <= x < rows and 0 <= y < cols

    count = 0
    for r in range(rows):
        for c in range(cols):
            if in_bound(r+1, c+1) and in_bound(r+1, c-1) and in_bound(r-1, c-1) and in_bound(r-1, c+1):
                diag_mas1 = grid[r-1][c-1] == "M" and grid[r][c] == "A" and grid[r+1][c+1] == "S" 
                diag_sam1 = grid[r-1][c-1] == "S" and grid[r][c] == "A" and grid[r+1][c+1] == "M" 

                diag_mas2 = grid[r-1][c+1] == "S" and grid[r][c] == "A" and grid[r+1][c-1] == "M" 
                diag_sam2 = grid[r-1][c+1] == "M" and grid[r][c] == "A" and grid[r+1][c-1] == "S"

                if (diag_mas1 or diag_sam1) and (diag_mas2 or diag_sam2):
                    count += 1
    return count

print(part2(text))