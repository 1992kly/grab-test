def sumto(nums, tar):
    if len(nums):
        dic = {}
        for num in nums:
            dic[num] = num
        for num in nums:
            diff = tar - num
            if diff in dict.keys():
                print("[%d,%d]" % (num, diff))
            else:
                print("no exit")
    else:
        print("nums is empty")
nums = [1,2]
tar = 10
sumto(nums, tar)
