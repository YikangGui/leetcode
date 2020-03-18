def partition(arr, low, high):
    # add code here
    pivot = arr[high]
    i = low

    for j in range(low, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i - 1


def quickSort(arr, low, high):
    if low >= high:
        return

    pivot_index = partition(arr, low, high)

    quickSort(arr, low, pivot_index - 1)
    quickSort(arr, pivot_index + 1, high)