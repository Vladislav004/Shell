def shell(lst):
    gap = len(lst) // 2

    while gap > 0:
        for value in range(gap, len(lst)):
            current_value = lst[value]
            position = value

            while position >= gap and lst[position - gap] > current_value:
                lst[position] = lst[position - gap]
                position -= gap
                lst[position] = current_value

        gap //= 2
    return lst


'''
Проверка
'''
li = [12, 34, 25, 15, 67, 23, 11, 86]
print(li)
print(shell(li))


# Вриант от бинг
def shell_sort(arr):

    n = len(arr)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            temp = arr[i]

            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap = int(gap / 2)
arr = [ 12, 34, 54, 2, 3]

shell_sort(arr)
print(arr)