class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == None or len(grid) == 0:
            return 0
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):

                if grid[i][j] == "1":
                    num_islands += dfs(grid, i, j)
        return num_islands


def dfs(grid, i, j):
    if (i >= len(grid) or i < 0 or j < 0 or j >= len(grid[i]) or grid[i][j] == "0"):
        return 0
    grid[i][j] = "0"
    dfs(grid, i - 1, j)
    dfs(grid, i + 1, j)
    dfs(grid, i, j - 1)
    dfs(grid, i, j + 1)
    return 1