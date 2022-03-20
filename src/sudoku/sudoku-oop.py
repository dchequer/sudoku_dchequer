from __future__ import annotations
from random import choice


# class cell()
# parameters:
# num options: list possible numbers within cell
# num it cointains: def None

# funcs:
# check row row and col, if cell has a num: remove it from its row and col possible numbers
# check col
# check square
# if cell has number: remove it from possible in other cells


# loop starts at center sudoku cell:
# random number from options (should be 1-9)
# eliminate said number from its row, col and square possibilities
# keep track of the cells with the lowest number of possibilities
# choose a random cell from with the lowest number of options
# re do loop
# grid = 9x9 matrix of Cell()s

MAXSIZE = 5
rows = 9
cols = 9

def printSubseed(subseed):
    return [print(subseed[i*3:(i+1)*3]) for i in range(3)]

class Matrix:
    def __init__(self):
        self.board = [[Cell(pos=(row, col)) for col in range(cols)]
                      for row in range(rows)]

        self.cellStack: list[Cell] = []

        # flatten board into a 1d list of all cells
        self.cells = sum(self.board, [])

    def __repr__(self) -> str:
        result = ""
        for row in range(rows):
            result += "\n"
            for col in range(cols):
                cell = matrix.board[row][col]
                result += f'[{row}][{col}]={cell.num}'
        return result
    
    @staticmethod
    def seedToMatrix(seed: str, substring_length=9, num_rows=9):
        return [list(map(int, seed[substring_length*row: (substring_length*row)+substring_length].split()[0])) for row in range(num_rows)]

    @staticmethod
    def printMatrix(matrix: Matrix):
        for row in range(rows):
            print("\n")
            for col in range(cols):
                print(matrix.board[row][col].num, end=" ")
        print()

    def sortOptions(self) -> list[Cell]:
        self.cells.sort(key=lambda cell: len(cell.options))
        return self.cells

    def toSeed(self) -> str:
        return "".join(["".join(map(str, self.board[row])) for row in range(rows)])

    def getSquare(self, row: int, col: int) -> tuple[int, int]:
        return (row // 3, col // 3)

    def squareCheck(self, row: int, col: int) -> set[int]:
        # cell cords of top left corner of square
        square_cords = self.getSquare(row, col)
        top_left_row, top_left_col = square_cords[0]*3, square_cords[1]*3

        seed = self.toSeed()
        # start is (row * 9) + col, row and col are cell cords of square top left corner
        subseed_start = (top_left_row * 9) + top_left_col
        subseed = "".join(
            [seed[subseed_start + 9*i: subseed_start + 9*i + 3] for i in range(3)])

        # return numbers in square
        square_exclude = set(map(int, subseed))

        #print(f'{seed = }')
        #print(f'{subseed = }')
        #print(f'{top_left_row * 9} + {top_left_col} = {subseed_start}')
        return square_exclude

    def crossCheck(self, row: int, col: int) -> set[int]:
        t_matrix = list(zip(*self.board))  # transpose matrix
        row_exclude = set(map(int, self.board[row])) - {0}
        col_exclude = set(map(int, t_matrix[col])) - {0}

        return row_exclude.union(col_exclude)

    def backtrack(self, history = []):
        #go to least old cell in stack
        #check if its possible to generate a different random num (i.e options has more than 1 option/number)
        #yes:
            #get a different num and get back on track
        #no:
            #backtrack again repeat
        lastCell = self.cellStack
        if (len(lastCell.options) > 1):
            #theres another option
            self.cells.append(lastCell)
            lastCell.options -= {lastCell.num}
            for cell in history:
                matrix.changeBoard(cell)
            matrix.changeBoard(lastCell)
        else:
            #backtrack again
            history.insert(0, lastCell)
            self.backtrack()


    def changeBoard(self, cell: Cell):
        if not cell.options: #if options set is empty
            #need to backtrack 
            self.backtrack(cell)
        
        new_num  = choice(list(cell.options))
        self.board[cell.row][cell.col].setNum(new_num)

        if (len(self.cellStack)>MAXSIZE):
            self.cellStack.pop()#pop oldest cell
        self.cellStack.insert(0, cell)

        # update "neighbour" cell options
        self.updateCellOptions()

        # remove itself from cells
        self.cells.remove(cell)

    def updateCellOptions(self):
        # update options in row of last change
        lastCell = self.cellStack[0]
        row = lastCell.row
        for col in range(cols):
            if col == lastCell.col: #skip itself
                continue
            matrix.board[row][col].exclude(self)

        # update options in col of last change
        col = lastCell.col
        for row in range(rows):
            if row == lastCell.row: #skip itself
                continue
            matrix.board[row][col].exclude(self)
        self.sortOptions()


class Cell:
    def __init__(self, pos: tuple(int, int)):
        self.row, self.col = pos
        self.options = set(range(1, 10))
        self.num = 0

    def __str__(self) -> str:
        return str(self.num)

    def __int__(self) -> int:
        return self.num

    def __repr__(self) ->str:
        return f'Cell[{self.row}][{self.col}] = {self.num}'

    def exclude(self, matrix: Matrix) -> set:
        self.options = set(range(1, 10)) - matrix.crossCheck(self.row,
                                                             self.col) - matrix.squareCheck(self.row, self.col)
        return self.options

    def setNum(self, new_num: int) -> int:
        self.num = new_num
        self.options = set()

        return self.num


if __name__ == '__main__':
    matrix = Matrix()
    matrix.changeBoard(matrix.board[4][4])  # generate center
    # generate board loop:
    # center has been created
    # cells options have been updated as of center
    # select a random cell with the lowest number of options, ignore 0s
    # select a random number for selected cell, empty its options
    # update new cells
    # repeat there are available cells
    while (matrix.cells):  # while it contains cells
        least_choices = len(matrix.cells[0].options)
        possible_cells = [cell for cell in matrix.cells if len(cell.options)==least_choices]
        try: selected_cell = choice(possible_cells) 
        except IndexError: Matrix.printMatrix(matrix)
        matrix.changeBoard(selected_cell)
        #Matrix.printMatrix(matrix)
    Matrix.printMatrix(matrix)