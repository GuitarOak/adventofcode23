with open("day2/input.txt") as f:
    ls = f.read().splitlines()

total = 0
for l in ls:
    game_id, rounds = l.split(": ")
    game_id = int(game_id.split(" ")[-1])
    
    is_possible = all(
        (int(n) <= 12 if c == "red" else int(n) <= 13 if c == "green" else int(n) <= 14)
        for rs in rounds.split("; ")
        for n, c in (r.split(" ") for r in rs.split(", "))
    )
    
    if is_possible:
        total += game_id

print('Possible Games: ' + str(total))
