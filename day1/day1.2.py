DIGITS = "one two three four five six seven eight nine"

def go(content):
    def extract(line):
        for index, word in enumerate(DIGITS.split(), 1):
            line = line.replace(word, f"{word}{index}{word}")
        return int([d for d in line if d.isdigit()][:1][0]+[d for d in line if d.isdigit()][-1:][0])
    print(sum(extract(line) for line in content.splitlines()))

with open('day1/input.txt', 'r') as file:
    go(file.read())