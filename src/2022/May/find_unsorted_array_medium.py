

def find_unsorted_array(nums):
    sorted_nums = list(enumerate(sorted(nums)))
    nums = list(enumerate(nums))
    
    l = 0
    r = len(nums) - 1
    
    while sorted_nums[l][1] == nums[l][1] and l < ((len(nums) - 1)):
        l += 1
        
    while sorted_nums[r][1] == nums[r][1] and r > 0:
        r -= 1
        
    if l < r:    
        return r - l + 1
    else:
        return 0



if __name__ == "__main__":
    nums = [2,6,4,8,10,9,15]
    # nums = [1,2,3,4]
    
    ans = find_unsorted_array(nums)

    ans