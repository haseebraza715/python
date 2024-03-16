


def twoSum(nums, target):
    new_list = []
    for i in range(0, len(target) - 1):
        for j in range(i + 1 , len(target)): 
            if target[i] + target[j] == nums:
                return [i,j]
    return new_list

list = twoSum(9, [2,7,11,15])   
print(list)



