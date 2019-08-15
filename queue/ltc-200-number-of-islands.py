class Solution:

    def num_islands_bfs(self, grid):
        """
        Initialize your data structure here
        :param grid: list[list[str]]
        :return: int
        """

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0

        count = 0
        n = len(grid)
        m = len(grid[0])

        queue = []
        for i in range(n):

            for j in range(m):

                if grid[i][j] == "1":

                    count += 1
                    queue.append((i, j))

                    while queue:

                        x, y = queue[0]
                        queue = queue[1:]

                        if x > 0 and grid[x - 1][y] == "1":
                            queue.append((x - 1, y))
                            grid[x - 1][y] = "0"
                        if x < n - 1 and grid[x + 1][y] == "1":
                            queue.append((x + 1, y))
                            grid[x + 1][y] = "0"
                        if y > 0 and grid[x][y - 1] == "1":
                            queue.append((x, y - 1))
                            grid[x][y - 1] = "0"
                        if y < m - 1 and grid[x][y + 1] == "1":
                            queue.append((x, y + 1))
                            grid[x][y + 1] = "0"

        return count


# driver script
if __name__ == "__main__":

    # initialize grid
    input = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
        ]

    # run solution
    solution = Solution()

    # run test cases
    print(solution.num_islands_bfs(input))

