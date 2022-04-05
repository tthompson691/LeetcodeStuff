from wrappers import time_it


def max_area(height) -> int:
    l = 0
    r = len(height) - 1
    max_area = 0
    
    while l < r:
        area = min([height[l], height[r]]) * (r - l)
        if area > max_area:
            max_area = area
        
        if height[l] > height [r]:
            r -= 1
        else:
            l += 1
            
    return max_area
        
    
    
if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,25,7]
    ans = max_area(height)
    ans