from random import sample


def get_unique_list_numbers() -> list[int]:
    from_ = -10
    to_ = 10
    count_ = 15
    list_numbers = sample(range(from_, to_), count_)
    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
# task3
