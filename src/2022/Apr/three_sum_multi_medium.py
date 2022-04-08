# UNFINISHED
from wrappers import time_it

@time_it
def three_sum(arr, target):
    l = 0
    r = len(arr) - 1
    tupes = 0
    
    missing = target - arr[l] - arr[r]
    if target in arr[(l+1):r]:
        tupes += 1
    
    counts


if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    ans = three_sum(arr, target)