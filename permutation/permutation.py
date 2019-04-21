from math import factorial

def permutation(nums):

    res = 0

    for index, num in enumerate(nums):
#        res += (num-index-1) *factorial(len(nums) -index - 1)

    return res

if __name__ =='__main__':

    nums = [2,1,3,4,5]
    print(permutation(nums))

