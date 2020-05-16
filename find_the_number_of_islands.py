class Solution:
    def num_islands(self, grid):
        if not grid:
            return 0

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                islands += self.dfs(grid, i, j)

        return islands

    def dfs(self, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == '0':
            return 0

        grid[i][j] = '0'

        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

        return 1


def main():
    """
    Uma ilha é formada por um '1' ou um cojutno de '1' (land) cercados por água 
    Podendo ser horizonalmente ou verticalmente 
    """
    _input = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    s = Solution()
    islands = s.num_islands(_input)
    print(islands)


if __name__ == "__main__":
    main()
