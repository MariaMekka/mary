
#empty_list = []
#empty_list = list()

#numbers = list(1, 2, 3, 4, 5, 6, 7, 8, 9)

#print(numbers)

#for element in numbers:
#    print(element)

numbers = [11, 221, 73, 65, 89, 18]

numbers.insert(0, 100)
numbers.append(1000)
print(numbers)

for index in range(0, len(numbers), 2):
#    print(str(index + " - " + str(element[intex])))
    print(f"{index} - {numbers[index]}")


