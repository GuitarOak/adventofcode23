import re
sum = 0
with open ("day1/input.txt", "r") as myfile:
    data = myfile.read().splitlines()
    for line in data:
        digits = re.findall(r'\d', line)
        if digits:
            first_digit = digits[0]
            last_digit = digits[-1]
            calibration_value = int(first_digit + last_digit)
            sum += calibration_value
print(f'Sum: {sum}')

