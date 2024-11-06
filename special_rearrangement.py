def special_rearrangement(nums):
    new_list = []
    for i in nums:
        if i % 2 == 0:
            new_list.append(i)
            nums.remove(i)

    return new_list + nums


print(special_rearrangement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
