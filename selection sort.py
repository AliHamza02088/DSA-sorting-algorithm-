#selection sort
def selectionsort(array , size):

    for s in range(size):
        min_idx = s
        for i in range(s+1 , size):
            if array[i] < array [min_idx]:
                min_idx = i
                
        (array[s] , array[min_idx]) = (array[min_idx] , array[s])

data = [5,3,8,1,9,2]
size = len(data)
selectionsort(data , size)
print(data , size)
