def twoSum(list, target):
    for x in range(len(list)):
        for y in range(len(list)):
            if list[x] + list[y] == target:
                return [x, y]

#print(twoSum([1, 5, 6, 23, 9, 4], 9))
