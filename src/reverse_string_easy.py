from wrappers import time_it
"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

s = ["h","e","l","l","o"]
cheat = False

@time_it
def reverse_string(s, cheat):
    print("asdf")
    if cheat:
        s.reverse()
        return

    l = 0
    r = len(s) - 1
    while l < r:
        lc = s[l]
        rc = s[r]
        s[l] = rc
        s[r] = lc
        
        l += 1
        r -= 1
    
    
reverse_string(s, cheat)
         
