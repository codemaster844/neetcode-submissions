class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numofIslands=0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col]=='1':
                    self.dfs(row,col,grid)
                    numofIslands+=1
        return numofIslands



    def dfs(self,row,col,grid:[List[List[str]]])->None:
        if row>=len(grid) or row<0 or col>=len(grid[0]) or col < 0 or grid[row][col]=='0':
            return 
        if grid[row][col]=='1':
            grid[row][col]='0'
        self.dfs(row+1,col,grid)
        self.dfs(row-1,col,grid)
        self.dfs(row,col+1,grid)
        self.dfs(row,col-1,grid)

        
        