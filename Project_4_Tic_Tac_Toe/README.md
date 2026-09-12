# Tic-Tac-Toe Game with Minimax AI

A simple **Tic-Tac-Toe** game built in Python where a human player competes against the computer. The computer uses the **Minimax algorithm** to choose its moves.

## Features

- Human player uses **X** and the computer uses **O**.
- 3×3 Tic-Tac-Toe board displayed in the terminal after every move.
- Human input uses positions **1–9**.
- Input validation prevents invalid positions and occupied-cell moves.
- Win detection checks all rows, columns, and diagonals.
- Draw detection is handled when the board is full.
- Computer opponent uses **Minimax**, allowing it to make optimal decisions for Tic-Tac-Toe.
- Clear messages indicate a human win, computer win, or draw.

## Project Structure

```text
Tic-Tac-Toe-Game/
├── Tic_Tac_Toe_Game.ipynb   # Original Jupyter/Google Colab notebook
├── tic_tac_toe.py            # Standalone Python version
├── README.md                 # Project overview and setup guide
├── DOCUMENTATION.md          # Detailed technical documentation
└── Tic_Tac_Toe_Setup_Guide.pptx  # Presentation for setup and project explanation
```

## Requirements

- Python 3.8 or newer
- Jupyter Notebook or Google Colab (only if using the `.ipynb` file)
- No external Python packages are required for the game logic.

## How to Run

### Option 1: Run the Python file

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python tic_tac_toe.py
```

On some systems you may need:

```bash
python3 tic_tac_toe.py
```

### Option 2: Run the notebook

1. Open `Tic_Tac_Toe_Game.ipynb` in Jupyter Notebook or Google Colab.
2. Run the code cell.
3. Enter a number from **1 to 9** when prompted.

## Board Positions

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

For example, entering `5` places **X** in the center.

## How the AI Works

The computer uses the **Minimax algorithm**.

- A computer win returns a score of `+1`.
- A draw returns `0`.
- A human win returns `-1`.
- On the computer's turn, Minimax selects the move with the highest score.
- On the human's simulated turn, Minimax selects the move with the lowest score.
- The algorithm recursively explores possible future moves until it reaches a win, loss, or draw.

Because Tic-Tac-Toe has a small search space, this basic Minimax implementation can evaluate the possible game states directly without additional libraries.

## Main Components

### `TicTacToe`
Stores the board and controls the complete game.

### `display_board()`
Prints the current board in a readable 3×3 format.

### `check_winner(player)`
Checks whether the supplied player has completed any winning row, column, or diagonal.

### `is_draw()`
Returns `True` when all nine positions are occupied.

### `game_over()`
Checks whether either player has won or the board is full.

### `human_move()`
Accepts and validates the user's move.

### `minimax(maximizing)`
Recursively evaluates possible future states and returns a score from the computer's perspective.

### `computer_move()`
Tests available moves with Minimax and plays the best-scoring move.

### `play()`
Runs the main game loop and checks the result after each move.

## Example Gameplay

```text
==============================
       TIC-TAC-TOE
==============================

You are X.
Computer is O.
Choose positions using numbers 1-9:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Enter your move (1-9): 2

   | X |
---+---+---
   |   |
---+---+---
   |   |

Computer is thinking...

 O | X |
---+---+---
   |   |
---+---+---
   |   |
```

The provided notebook also demonstrates input validation when an occupied position is selected and correctly reports a computer win.

## Learning Objectives

This project demonstrates:

1. Python classes and methods.
2. Lists and indexing.
3. Loops and conditional statements.
4. User input validation and exception handling.
5. Game-state management.
6. Recursive algorithms.
7. The Minimax decision-making algorithm.
8. Win and draw detection.

## Future Improvements

- Add a graphical interface using Tkinter, Pygame, or a web frontend.
- Add difficulty levels.
- Add score tracking across multiple rounds.
- Allow the user to choose X or O.
- Add automated unit tests.
- Improve Minimax with depth-based scoring so faster wins are preferred.

## License

This project is intended as a student/project demonstration and can be adapted for educational use.
