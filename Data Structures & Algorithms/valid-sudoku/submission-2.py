class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])

        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)


        for r in range(9):
            for c in range(9):
                char = board[r][c]
        
                if char == '.':
                    continue

                if (char in rows[r]
                    or char in cols[c]
                    or char in squares[(r // 3, c // 3)]):
                        return False

                cols[c].add(char)
                rows[r].add(char)
                squares[(r//3,c//3)].add(char)
                
 
        return True




        # if n<9:
        #     return None

        # for r in range(n):
        #     seen = set()
        #     for char in board[r]:
        #         if char in seen and char!='.':
        #             return False
        #         seen.add(char)
        
        
        # for col in range(m):
        #     seen = set()
        #     for row in range(n):
        #         char = board[row][col]
        #         if char in seen and char!='.':
        #             return False
        #         seen.add(char)

        
        # for box in range(n):
        #     rstart = (box//3)*3
        #     cstart = (box%3)*3
        #     seen = set()
 
        #     for row in range(rstart, rstart+3):
        #         for col in range(cstart,cstart+3):
        #             char = board[row][col]
              
        #             if char in seen and char!='.':
        #                 return False
        #             seen.add(char)

                
        # return True
          
                


  

            # seen = set()
            # for 

# box = 0,1,2 - row [0,1,2], col [0,1,2]. [3,4,5]. [6,7,8]
# box = 3,4,5 - row [3,4,5], col [0,1,2]. [3,4,5]. [6,7,8]
# box - 6,7,8 - row [6,7,8], col [0,1,2]. [3,4,5]. [6,7,8]



        # return False



# go over the rows - O(nm)
# go over columns - O(nm)
# go over boxes - O(nm)


        