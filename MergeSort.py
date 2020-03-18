def mergeSort(arr):
    mergeSort_(arr, [0] * len(arr), 0, len(arr) - 1)

    # add code here


def mergeSort_(arr, temp, left_start, right_end):
    if left_start >= right_end:
        return
    middle = (left_start + right_end) // 2

    mergeSort_(arr, temp, left_start, middle)
    mergeSort_(arr, temp, middle + 1, right_end)
    merge(arr, temp, left_start, right_end)


def merge(arr, temp, left_start, right_end):
    middle = (left_start + right_end) // 2
    left = left_start
    right = middle + 1
    temp_index = left_start

    while left <= middle and right <= right_end:
        if arr[left] <= arr[right]:
            temp[temp_index] = arr[left]
            left += 1
        else:
            temp[temp_index] = arr[right]
            right += 1
        temp_index += 1
    if arr[left:middle+1]:
        temp[temp_index:right_end + 1] = arr[left:middle + 1]
    else:
        temp[temp_index:right_end + 1] = arr[right:right_end + 1]
    arr[left_start: right_end + 1] = temp[left_start: right_end + 1]

a=[1,5,2,3,6,8,4,2,6,8,4,5]
mergeSort(a)
print(a)