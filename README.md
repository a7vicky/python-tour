"""
Given a grid of size n*m (n is the number of rows and m is the number of columns in the grid) consisting of 'W's (Water) and 'L's (Land). Find the number of islands.

Note: An island is either surrounded by water or the boundary of a grid and is formed by connecting adjacent lands horizontally or vertically or diagonally i.e., in all 8 directions.

Examples:

Input: grid[][] = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]
Output: 4
"""

def numIslands(self, grid):
    # code here
    row = len(grid)
    column = len(grid[0])
    count = 0
    for r in row :
        for c in columm:
            if grid[r][c] == "L":
                count+=1
                self.dfs(grid,r,c)
    return count

def dfs(self, grid, i, j):
    if i < 0 or i > len(grid) or j < 0 or j > len (grid[0]) or grid[i][j] != "L":
    return
        
    grid[i][j] = "#"
    self.dfs(grid[i-1][j])
    self.dfs(grid[i+1][j])
    self.dfs(grid[i][j-1])
    self.dfs(grid[i][j+1])
    self.dfs(grid[i-1][j-1])
    self.dfs(grid[i-1][j+1])
    self.dfs(grid[i+1][j-1])
    self.dfs(grid[i+1][j+1])