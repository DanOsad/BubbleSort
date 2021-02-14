import random

array = [random.randint(0, 10) for x in range(10)]


def bubblesort(array):
    i = 0

    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                sorted = False
                array[i], array[i + 1] = array[i + 1], array[i]
    return array


print(f'Unsorted: {array}')
bubblesort(array)
print(f'Sorted: {array}')
