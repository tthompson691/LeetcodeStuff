

def sort_array_by_parity(nums):
    evens = []
    odds = []
    for n in nums:
        if n % 2 == 0:
            evens.append(n)
        else:
            odds.append(n)


    return evens + odds
            
    
    

if __name__ == "__main__":
    nums = [3, 1, 2, 4]

    ans = sort_array_by_parity(nums)

    ans