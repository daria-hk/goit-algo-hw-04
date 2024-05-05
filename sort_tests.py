import timeit

numbers = [5, 3, 8, 4, 2]
def insertion_sort(lst): #Сортування вставками
    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >=0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return lst

def test_insertion_sort():
   insertion_sort(numbers)

def merge_sort(arr):#Сортування злиттям
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
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

def test_merge_sort():
    merge_sort(numbers)


def timsort(): #Сортування Тіма
   sorted(numbers)

execution_time_insertion_sort = timeit.timeit(test_insertion_sort, number=100000)
print("Insertion-sort execution time:", execution_time_insertion_sort, "sek")

execution_time_merge_sort = timeit.timeit(test_merge_sort, number=100000)
print("Merge-sort execution time:", execution_time_merge_sort, "sek")

execution_time_timsort = timeit.timeit(timsort, number=100000)
print("Timsort-sort execution time:", execution_time_timsort, "sek")



