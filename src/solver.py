class Solver:
    def __init__(self) -> None:
        self.rows = 3 
        self.board = [[0] * self.rows for i in range(self.rows)]

    def is_valid(self):
        '''
        Determines if sudoku constraints are maintained for the following board
        - All the rows have only one number [1-9]
        - All the cols have only one number [1-9]
        - Within a 3x3 grid
            Only one number of [1-9] exits
        '''
        rows = [0] * (self.rows ** 2)
        cols = [0] * (self.rows ** 2)
        print(rows)
        print(cols)

if __name__ == '__main__':
    solver = Solver()
    solver.is_valid()