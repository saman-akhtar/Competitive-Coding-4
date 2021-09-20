class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # TC = O(mn)
        #SC = O(mn)
        if grid is None:
            return 0
        m = len(grid)
        n = len(grid[0])
        que = deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j ] == 2:
                    que.append([i,j])
                elif grid[i][j ] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        direc = [[0,1],[1,0],[-1,0],[0, -1]]
        lvl = 0
        while len(que) > 0:
            size = len(que)
            for i in range(size):  
                root = que.popleft()
                for d in direc:
                    r = root[0] + d[0]
                    c = root[1] + d[1]
                    
                    # Update orange is row col is valid and
                    # orange is fresh
                    if r >= 0 and r <m and c >= 0 and c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        que.append([r,c])
                        fresh -= 1
            lvl += 1
        if fresh == 0:
            return lvl - 1
        return -1
        
        
        return 1
        
