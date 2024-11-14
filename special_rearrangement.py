def special_rearrangement(nums):
    new_list = []  # create a new list to rearrange the old list
    for i in nums:
        if (
            i % 2 == 0
        ):  # if the item is even add it to the new list and remove it from the old one
            new_list.append(i)
            nums.remove(i)

    return (
        new_list + nums
    )  # after that return the new list + the old list so the even numbers will came before the odd


print(special_rearrangement([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
