# Beginner Object Oriented Sudoku Board Generator

## Matrix Class
This class keeps track of the board with an instance variable called self.board
It is responsible for checking the rules of sudoku in order to make a move, it check to see which numbers to exclude from a cell's row, column and 3x3 square

The variable self.cellStack is a list of the last 5 cells that were changed in order to backtrack in case of the algorithm cornering itself

Finally, self.cells is just a flattened version of self.board for easy traversing.

## Cell Class
Each Cell gets initialized with 4 instance variables:
* self.row and self.col keep track of cell's position in the board
* self.options contains all the possible numbers that the cell could be
* self.num is the actual number it contains


## Main
The main function of the program is an example of how to create a board
* Create a Matrix Object
* Set the center cell (located at 4,4) to a random number utilizing `Matrix.changeBoard(self, cell:Cell)`  
  * Parameter cell is retrieved from using `Matrix.self.board[4][4]`
* Start a while loop that runs if `Matrix.cells` contains anything
* Get least number of choices of cell closest to being solved
  * Important to mention that each time `Matrix.changeBoard()` is called, it sorts `self.cells` to have the cells closest to being done in front
* Create a list of all cells that have *least number* amount of choices
* Randomly choose one cell from this list
* Call `Matrix.changeBoard()` with the random cell as the argument

## End
To use this module all you have to do is set `var_name = sudoku-oop.generateBoard()` and it will return a Matrix Object with your board