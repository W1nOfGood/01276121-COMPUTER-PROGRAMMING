def bubble_sort(nums):
    numsbutlist = []
    for i in range(len(nums)):
        numsbutlist.append(nums[i])
    numsbutlist.sort()
    return numsbutlist

def sort_avoid_negative_num(nums):
    positive = []
    negative = []
    finalre = []
    pos = 0
    poslist = 0
    for i in range(len(nums)):
        if nums[i] >= 0:
            positive.append(nums[i])
        else:
            negative.append(nums[i])
        positive.sort()

    for numarr in nums:
        if numarr < 0:
            finalre.append(negative[poslist])
            poslist += 1
        else:
            finalre.append(positive[pos])
            pos += 1
    return finalre

print("*** Sort avoid negative number ***")
inp = input("Enter Input : ").split()
numsint = []
for i in range(len(inp)):
    numsint.append(int(inp[i]))

bubbled = bubble_sort(numsint)
sortnoneg = sort_avoid_negative_num(numsint)
print(f"Normal sort : \n{bubbled}\nsort avoid negative number : \n{sortnoneg}")
print("===== End of program =====")