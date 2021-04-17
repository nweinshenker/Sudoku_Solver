from collections import defaultdict

"""
    This call will handle all the functionalities that are associated with board
    solving the given board.

    For examples: 
        - Passing in a 9x9 sudoku board will allow this 
        board = [[ '1', '', '' ...],
                 [ '6', '', '7', ...],
                 .
                 .
                 .
                ]
    sudoku = BoardSolver(board)
    isValidBoard(sudoku) => return a boolean value
"""

class BoardSolver:
    def __init__(self, board) -> None:
        self.board = [[x for x in row] for row in board]
    
    def __repr__(self) -> str:
        return {{self.__class__.__name__}.format(self=self)}

    def is_valid(self) -> bool:
        '''
        Determines if sudoku constraints are maintained for the following board
        - All the rows have only one number [1-9]
        - All the cols have only one number [1-9]
        - Within a 3x3 grid
            Only one number of [1-9] exits
        '''
        n = len(self.board) # The number of rows and cols
        
        # HashSet for the rows, cols & grid of the sudoku puzzle
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        mMat = [set() for i in range(9)]
        
        n = len(self.board)

        for i in range(n):
            for j in range(n):
                cur = self.board[i][j]
                if cur != '.':
                    
                    k = (i // 3 ) * 3 + j // 3
                
                    # Check the given row is valid
                    if (cur not in rows[i]):
                         rows[i].add(cur)
                    else: 
                        return False
                    
                    # Check the given col is valid
                    if (cur not in cols[j]): 
                        cols[j].add(cur)
                    else: 
                        return False
                
                    # Check the given grid is valid
                    if (cur not in mMat[k]):
                        mMat[k].add(cur)
                    else:
                        return False
        return True
