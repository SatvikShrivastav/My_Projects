# Tic-Tac-Toe Game — Technical Documentation

## 1. Project Overview

This project implements a console-based Tic-Tac-Toe game in Python. A human player competes against a computer opponent. The human plays **X**, while the computer plays **O**.

The uploaded project is implemented as a Python 3 Jupyter/Google Colab notebook. The game uses a 9-element list to represent the board and the Minimax algorithm for the computer's decisions.

## 2. Objectives

The project satisfies the following requirements:

- Build a Tic-Tac-Toe game where the computer plays against the user.
- Implement an AI opponent using the Minimax algorithm.
- Display the board after every move.
- Detect wins and draws correctly.
- Validate user input and occupied positions.

## 3. Technology Used

- **Language:** Python
- **Environment:** Python 3 / Jupyter Notebook / Google Colab
- **External libraries:** None required
- **AI technique:** Minimax

The notebook metadata specifies a Python 3 kernel.

## 4. Board Representation

The board is stored as a list containing nine strings:

```python
self.board = [" "] * 9
```

The positions correspond to:

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

Internally, the program uses indexes `0` through `8`, while the user enters positions `1` through `9`.

## 5. Game Logic

### 5.1 Displaying the Board

`display_board()` prints the nine board values in three rows separated by horizontal and vertical lines. The method is called after both the human and computer moves.

### 5.2 Detecting a Winner

`check_winner(player)` checks eight winning combinations:

- Three rows
- Three columns
- Two diagonals

A player wins when all three positions in any one combination contain that player's symbol.

### 5.3 Detecting a Draw

`is_draw()` returns true when there are no empty spaces remaining:

```python
return " " not in self.board
```

The game therefore ends as a draw when the board is full and no player has won.

### 5.4 Detecting Game Over

`game_over()` combines winner and draw checks. It returns true if either the human or computer has won, or if the board is full.

## 6. Human Move Handling

The `human_move()` method repeatedly asks:

```text
Enter your move (1-9):
```

The input is converted to an integer and adjusted to the internal zero-based index.

The method rejects:

- Values below 1 or above 9.
- Positions that are already occupied.
- Non-numeric input.

The notebook example shows an occupied-position message:

```text
That position is already occupied.
```

## 7. AI Design — Minimax

The computer uses the Minimax algorithm rather than random moves.

The scoring system is:

| Result | Score |
|---|---:|
| Computer wins | +1 |
| Draw | 0 |
| Human wins | -1 |

### Maximizing Turn

When `maximizing=True`, the algorithm simulates each available computer move and selects the maximum score.

### Minimizing Turn

When `maximizing=False`, the algorithm simulates each available human move and selects the minimum score.

### Recursive Evaluation

For each simulated move:

1. Place the symbol.
2. Recursively call Minimax.
3. Undo the simulated move.
4. Compare the returned score with the best score found so far.

This continues until the simulated position reaches a terminal state: computer win, human win, or draw.

## 8. Computer Move

`computer_move()` evaluates every currently empty position using Minimax.

The move with the highest returned score is selected and placed on the board as `O`.

## 9. Main Game Flow

The `play()` method performs the following sequence:

1. Print the game title and instructions.
2. Show the numbered board.
3. Ask the human for a move.
4. Display the updated board.
5. Check for a human win or draw.
6. Ask the computer to calculate its move.
7. Display the updated board.
8. Check for a computer win or draw.
9. Repeat until the game ends.

## 10. Program Entry Point

The notebook ends with:

```python
if __name__ == "__main__":
    main()
```

The `main()` function creates a `TicTacToe` object and starts the game using `game.play()`.

## 11. Testing Demonstrated in the Notebook

The notebook output demonstrates:

- Successful human input.
- Board updates after moves.
- Computer move generation.
- Rejection of an already occupied position.
- Continued gameplay after invalid input.
- Correct detection and announcement of a computer win.

Example final result shown by the notebook:

```text
💻 Computer wins!
```

## 12. Complexity

For a basic Minimax implementation, the worst-case search grows exponentially with the depth of the game tree. Tic-Tac-Toe is small enough that this direct recursive approach is practical.

No external AI framework is needed.

## 13. Limitations

- The interface is terminal-based.
- There is no graphical UI.
- There are no difficulty settings.
- There is no persistent score/history.
- The current Minimax score does not explicitly include search depth, so equally scored winning paths are not ranked by how quickly they finish.

## 14. Possible Enhancements

1. Add a GUI.
2. Add player-name and score tracking.
3. Add difficulty levels.
4. Add a restart option.
5. Add unit tests for all winning combinations and draw states.
6. Add depth-aware Minimax scoring.
7. Allow the player to choose whether to play first.

## 15. Conclusion

The project provides a compact demonstration of game development fundamentals and artificial intelligence. It combines input handling, board-state management, rule checking, recursion, and Minimax decision-making in a single Python program.
