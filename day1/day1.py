import re

map = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9
}

def normalize(s):
	if s.isdigit(): return int(s)

	return map[s]

def p1(line):
	if not line: return 0
	match = re.findall(r'\d', line)
	return (int(match[0]) * 10) + int(match[-1])

def p2(line):
    if not line:
        return 0
    matches = re.findall(rf'{"|".join(map.keys())}', line)
    return sum(normalize(match) for match in matches)

with open("day1/input.txt", "r") as f:
	input_data = f.read()
	p1c = sum([p1(line) for line in input_data.split("\n")])
	print(f"Part 1: {p1c}")
	p2c = sum([p2(line) for line in input_data.split("\n")])
	print(f"Part 2: {p2c}")