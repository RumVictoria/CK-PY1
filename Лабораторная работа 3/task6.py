list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_last_number = list_numbers[0]
max_last_number_index = 0
last_number = list_numbers[-1]

for index, current_number in enumerate(list_numbers):
    if current_number >= max_last_number:
        max_last_number = list_numbers[index]
        max_last_number_index = index

list_numbers[max_last_number_index], list_numbers[-1] = last_number, max_last_number

print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
