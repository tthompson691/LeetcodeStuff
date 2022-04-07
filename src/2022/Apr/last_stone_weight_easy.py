from wrappers import time_it


def last_stone_weight(stones):
    def smash_em(a, b):
        return abs(a-b)
    
    while len(stones) > 1:
        stones.sort(reverse=True)
        leftover = smash_em(stones[0], stones[1])
        if leftover != 0:
            stones = stones[2:] + [leftover]
        else:
            stones = stones[2:]
        
    try:
        return stones[0]
    except IndexError:
        return 0


if __name__ == "__main__":
    stones = [2,7,4,1,8,1]
    ans = last_stone_weight(stones)
