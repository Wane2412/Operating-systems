# num = input("Enter a list of numb (separated by spaces): ").split()
# num = [eval(num) for num in num]
# order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")
# if order == 'asc':
#     num.sort()
# elif order == 'desc':
#     num.sort(reverse=True)
# else:
#     print("Invalid input! Please enter 'asc' or 'desc'.")
# print("Sorted numb:", num)


# ____________________________________


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def ascending_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)

def descending_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] < arr[j + 1]:
                swap(arr, j, j + 1)

numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [eval(num) for num in numbers]
order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")

if order == 'asc':
    ascending_sort(numbers)
elif order == 'desc':
    descending_sort(numbers)
else:
    print("Invalid input! Please enter 'asc' or 'desc'.")
print("Sorted numbers:", numbers)
