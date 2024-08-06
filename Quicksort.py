#Quicksort
def partition(array,low,high):

    pivot = array[high]
    i = low -1

    for j in range(low , high):
        if array[j] <= pivot:
            i = j + 1

            (array[i],array[j]) = (array[j],array[i])
    (array[i + 1],array[high]) = (array[high],array[i + 1])
    return i + 1

def quicksort(array,high,low):
    if low < high:
        pi = partition(array,low,high)

        quicksort(array , low , pi - 1)
        quicksort(array , pi + 1, high)

data = [5,3,8,1,9,2]
print("unsorted array")
print(data)

size = len(data)

quicksort(data , 0 ,size - 1)

print('sorted array in ascending order: ')
print(data)