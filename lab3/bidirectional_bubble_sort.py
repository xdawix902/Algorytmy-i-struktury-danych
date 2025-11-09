def bidirectional_bubble_sort(arr):
    n = len(arr)
    start = 0
    end = n - 1
    swapped = True

    while swapped:
        swapped = False

        for i in range(start, end):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        
        if not swapped: break

        swapped = False

        for i in range(end, start, -1):
            if arr[i-1] > arr[i]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
                swapped = True
        start+= 1
    return arr

arr = [3,2,5,1,4,6]
print(bidirectional_bubble_sort(arr))