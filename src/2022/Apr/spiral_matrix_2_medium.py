

def generate_matrix(n):
    i = j = 0
    def move_right(i, j):
        j += 1
        return i, j
    def move_down(i, j):
        i += 1
        return i, j
    def move_left(i, j):
        j -= 1
        return i, j
    def move_up(i, j):
        i -= 1
        return i, j
        
    order = [move_right, move_down, move_left, move_up]    
    order_i = 0
    mx = [[0 for i in range(n)] for j in range(n)]
    num = 1
    while num <= n**2:
        mx[i][j] = num
        num += 1
        if order_i == 0:
            if j + 1 == n or mx[i][j+1] != 0:
                order_i += 1
        elif order_i == 1:
            if i + 1 == n or mx[i+1][j] != 0:
                order_i += 1
        elif order_i == 2:
            if j - 1 < 0 or mx[i][j-1] != 0:
                order_i += 1
        elif order_i == 3:
            if i - 1 < 0 or mx[i-1][j] != 0:
                order_i = 0
                
        i, j = order[order_i](i, j)
        
    return mx

    
if __name__ == "__main__":
    ans = generate_matrix(3)
    ans
    