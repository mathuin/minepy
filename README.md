Minesweeper in Python
=====================

As an exercise before an interview, I decided to implement Minesweeper in Python.

A refresher, summarized from [Wikipedia](https://en.wikipedia.org/wiki/Minesweeper_(video_game)):
* The game is played on a grid with a number of hidden mines.
* The player selects a cell on the grid, which is revealed.
* If the revealed cell is a mine, the game ends.
* Otherwise, the cell is replaced by a number, or a space.
* The number representing the number of mines (if any) in the eight neighboring cells.

The board dimensions default to 15 by 12 and the number of mines defaults to 33% of the available cells.  Both dimensions and number of mines can be set via command-line flags.
