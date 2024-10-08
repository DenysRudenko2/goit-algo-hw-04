import random
import timeit


# Генерація тестових наборів даних
def get_number_list(n):
    return random.sample(range(n), n), list(range(n)), list(range(n, 0, -1))


# Функція для вимірювання часу виконання
def measure_time(sort_func, arr):
    return timeit.timeit(lambda: sort_func(arr.copy()), number=1)


def merge_sort(arr) -> list:
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right) -> list:
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(lst) -> list:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


sizes = [10, 100, 1000]
for size in sizes:
    random_data, sorted_data, reversed_data = get_number_list(size)
    print(f"\nData size: {size}")

    # Випадкові дані
    print(f"Random data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, random_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, random_data):.6f} seconds")

    # Відсортовані дані
    print(f"Sorted data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, sorted_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, sorted_data):.6f} seconds")

    # Реверсні дані
    print(f"Reversed data:")
    print(f"Insertion Sort: {measure_time(insertion_sort, reversed_data):.6f} seconds")
    print(f"Merge Sort: {measure_time(merge_sort, reversed_data):.6f} seconds")
