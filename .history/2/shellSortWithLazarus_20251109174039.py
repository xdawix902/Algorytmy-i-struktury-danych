def shellSort(arr):
    n = len(arr)
    iter = 1
    gap = 2*(n//pow(2, iter+1))+1
    while gap > 0:
        iter += 1
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i+gap] > arr[i]:
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                i = i - gap
            j += 1
        if gap == 1: break
        gap = 2 * (n//pow(2,iter+1))+1

arr = [5,4,1,20,30,2,7,8]
shellSort(arr)
print(arr)