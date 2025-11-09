def shellSort(arr):
    n = len(arr)
    iter = 0;
    k = n
    while k > 1:
        iter += 1
        k = k//2
    
    gap = 2 ** iter - 1

    while gap > 0:
        iter -= 1
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
        gap = 2**iter - 1

arr = [5,4,1,20,30,2,7,8]
shellSort(arr)
print(arr)


