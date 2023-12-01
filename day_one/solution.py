

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
item_numbers = []
final_values = []

with open ('puzzle_input.txt', 'r') as file:
    input = file.readlines()

for line in input:
    number_holder = []
    for char in line:
        if char in numbers:
            number_holder.append(char)
    if len(number_holder) < 2:
        number_holder.append(number_holder[0])
    cal_value = number_holder[0] + number_holder[-1]
    final_values.append(int(cal_value))

answer = sum(final_values)
print(answer)