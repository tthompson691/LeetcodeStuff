from wrappers import time_it
from collections import Counter

@time_it
def three_sum(arr, target):
    l = 0
    r = len(arr) - 1
    
    counts = dict(Counter(arr))
    
    counts


if __name__ == "__main__":
    arr = [1,1,2,2,3,3,4,4,5,5]
    target = 8
    ans = three_sum(arr, target)