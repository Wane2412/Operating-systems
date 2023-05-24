# x=eval(input())
# y=eval(input())
# z=x+y
# print(z)





# # Python3 implementation of First-Fit algorithm
# # Function to allocate memory to
# # blocks as per First fit algorithm
# def firstFit(blockSize, m, processSize, n):
#     # Stores block id of the
#     # block allocated to a process
#     allocation = [-1] * n
#     # Initially no block is assigned to any process
#     # pick each process and find suitable blocks
#     # according to its size ad assign to it
#     for i in range(n):
#         for j in range(m):
#             if blockSize[j] >= processSize[i]:
#                 # allocate block j to p[i] process
#                 allocation[i] = j
#                 # Reduce available memory in this block.
#                 blockSize[j] = processSize[i]
#                 break 
#     print(" Process No. Process Size      Block no.")
#     for i in range(n):
#         print(" ", i + 1, "         ", processSize[i],
#                           "         ", end = " ")
#         if allocation[i] != -1:
#             print(allocation[i] + 1)
#         else:
#             print("Not Allocated")
# # Driver code
# if __name__ == '__main__':
#     blockSize = [100, 500, 200, 300, 600]
#     processSize = [212, 417, 112, 426]
#     m = len(blockSize)
#     n = len(processSize)
 
#     firstFit(blockSize, m, processSize, n)


# ________________________


# Python3 implementation of First-Fit algorithm
# Function to allocate memory to
# blocks as per First fit algorithm
def firstFit(blockSize, m, processSize, n):
    # Stores block id of the block allocated to a process
    allocation = [-1] * n
    # Create a flag list to track allocated blocks
    remove = [False] * m
    # Initially no block is assigned to any process
    # pick each process and find suitable blocks
    # according to its size and assign to it
    for i in range(n):
        for j in range(m):
            if not remove[j] and blockSize[j] >= processSize[i]:
                # Allocate block j to process i
                allocation[i] = j
                remove[j] = True
                # Reduce available memory in this block
                blockSize[j] = processSize[i]
                break
    print("Process No.   Process Size   Block no.")
    for i in range(n):
        print(" ", i + 1, "         ", processSize[i], "         ", end=" ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
# Driver code
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
    firstFit(blockSize, m, processSize, n)




# def bubble_sort(arr, ascending=True):
#     n = len(arr)
#     for i in range(n - 1):
#         for j in range(n - 1 - i):
#             if (arr[j] > arr[j + 1] and ascending) or (arr[j] < arr[j + 1] and not ascending):
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# numbers = input("Enter a list of numbers (separated by spaces): ").split()
# numbers = [int(num) for num in numbers]
# order = input("Enter 'asc' for ascending order or 'desc' for descending order: ")
# if order == 'asc':
#     bubble_sort(numbers)
# elif order == 'desc':
#     bubble_sort(numbers, ascending=False)
# else:
#     print("Invalid input! Please enter 'asc' or 'desc'.")
# print("Sorted numbers:", numbers)

