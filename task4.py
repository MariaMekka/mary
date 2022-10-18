def get_max(numbers):
    max = numbers[0]

    for element in numbers:
        if element > max:
            max = element

    return max


def get_min(numbers):
    min = numbers[0]

    for element in numbers:
        if element < min:
            min = element

    return min



def get_last_max_value_index(numbers):
    max_index = 0

    for index in range(-len(numbers), 0):
        if numbers[index] >= numbers[max_index]:
            max_index = index

    return max_index