"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4

"""

def numIslands(grid):
    # code here
    row = len(grid)
    column = len(grid[0])
    count = 0
    for r in range(row) :
        for c in range(column):
            if grid[r][c] == "L":
                dfs(grid, r, c)
                count+=1
                
    return count

def dfs(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len (grid[0]) or grid[i][j] != "L":
        return
        
    grid[i][j] = "#"
    dfs(grid, i+1, j)
    dfs(grid, i-1, j)
    dfs(grid, i, j+1) 
    dfs(grid, i, j-1)
    dfs(grid, i+1, j+1)
    dfs(grid, i+1, j-1)
    dfs(grid, i-1, j+1)
    dfs(grid, i-1, j-1)
   
   
    


if __name__ == "__main__":
    grid = [
        ['L', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'L'],
        ['L', 'W', 'W', 'L', 'L'],
        ['W', 'W', 'W', 'W', 'W'],
        ['L', 'W', 'L', 'L', 'W']
    ]

    result = numIslands(grid)
    print("Number of islands:", result)