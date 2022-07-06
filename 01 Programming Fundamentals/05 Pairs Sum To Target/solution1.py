def pairs_sum_to_target(list1, list2, target):
    sums = []
    for index1, num1 in enumerate(list1):
        for index2, num2 in enumerate(list2):
            if num1 + num2 == target:
                sums.append([index1, index2])
    return sums
