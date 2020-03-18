def loadBalancer(loads):
    n = len(loads)
    if n < 5:
        return False
    total_sum = sum(loads)
    left_pointer = 1
    right_pointer = n-2
    left_sum = sum(loads[:left_pointer])
    right_sum = sum(loads[right_pointer+1:])
    drop_sum = loads[left_pointer] + loads[right_pointer]
    medium_sum = total_sum - left_sum - right_sum - drop_sum
    if left_sum == right_sum == medium_sum:
        return True

    while left_pointer < right_pointer and medium_sum > right_sum and medium_sum > left_sum:
        if left_sum < right_sum:
            left_pointer += 1
            left_sum += loads[left_pointer-1]
        else:
            right_pointer -= 1
            right_sum += loads[right_pointer+1]
        drop_sum = loads[left_pointer] + loads[right_pointer]
        medium_sum = total_sum - left_sum - right_sum - drop_sum
        if left_sum == right_sum == medium_sum:
            return True
    return False

loads = [1, 3, 4, 2, 2, 2, 1, 1, 2]
loads = [1,1,1,1,1]
loads = [1,1,1,1,1,1]
loads = [1, 2] * 10000
loads=[1,1,1,1]
print(loadBalancer(loads))
