from wrappers import time_it
import copy

def shift_grid(grid, k):
    def shift1(_grid):
        next_grid = copy.deepcopy(_grid)
        for i, x in enumerate(_grid):
            for j, y in enumerate(x):
                try:
                    next_grid[i][j+1] = _grid[i][j]
                except IndexError:
                    next_grid[i][0] = _grid[i][j]
                
        return next_grid
                
    def shift2(_grid, n):
        next_grid = copy.deepcopy(_grid)
        for i, x in enumerate(_grid):
            for j, y in enumerate(x):
                try:
                    next_grid[i+1][0] = _grid[i][n-1]
                except IndexError:
                    next_grid[0][0] = _grid[i][n-1]
                
        return next_grid
    
    def shift3(_grid, m, n):
        next_grid = copy.deepcopy(_grid)
        next_grid[0][0] = _grid[m-1][n-1]
        return next_grid
    
    
    next_grid = copy.deepcopy(grid)
    for i in range(k):
        next_grid = shift1(next_grid)
        next_grid = shift2(next_grid, len(next_grid[0]))
        next_grid = shift3(next_grid, len(next_grid), len(next_grid[0]))
        
    next_grid
        

if __name__ == "__main__":
    grid = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    
    ans = shift_grid(grid, k)
    ans