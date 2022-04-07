from wrappers import time_it

## CURRENTLY RETURNS CORRECT SOLUTION BUT TOO SLOW
@time_it
def trap(height):
    def check_for_walls(_d, _i) -> bool:
        left = height[0:_i]
        right = height[(_i + 1):]
        if any([l >= _d for l in left]) and any(r >= d for r in right):
            return True
        else:
            return False
        # check for left_wall
        # l_i = _i - 1
        # while height[l_i] < _d and l_i > 0:
        #     l_i -= 1
            
        # if l_i < 0:
        #     return False
        # # check for right wall
        # r_i = _i + 1
        # try:
        #     while height[r_i] < _d:
        #         r_i += 1
        # except IndexError:
        #     return False
        
        # return True
            
    filled = 0
    depth = range(min(height), max(height) + 1)

    for d in depth:
        for i, h in enumerate(height):
            if d > h:
                if check_for_walls(d, i):
                    filled += 1

    return filled
                
        
        
if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    ans = trap(height)
    print(ans)