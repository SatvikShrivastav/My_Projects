from typing import List, Optional


class TicTacToe:
    def __init__(self) -> None:
        self.board: List[str] = [" "] * 9
        self.human = "X"
        self.computer = "O"

    def display_board(self) -> None:
        """Display the current Tic-Tac-Toe board."""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("\n")

    def check_winner(self, player: str) -> bool:
        """Return True if the given player has won."""
        winning_combinations = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]

        return any(
            all(self.board[index] == player for index in combination)
            for combination in winning_combinations
        )

    def is_draw(self) -> bool:
        """Return True if the board is full and nobody has won."""
        return " " not in self.board

    def game_over(self) -> bool:
        """Return True if the game has ended."""
        return (
            self.check_winner(self.human)
            or self.check_winner(self.computer)
            or self.is_draw()
        )

    def human_move(self) -> None:
        """Get a valid move from the user."""
        while True:
            try:
                position = int(input("Enter your move (1-9): ")) - 1

                if position < 0 or position > 8:
                    print("Please enter a number between 1 and 9.")
                    continue

                if self.board[position] != " ":
                    print("That position is already occupied.")
                    continue

                self.board[position] = self.human
                break

            except ValueError:
                print("Please enter a valid number.")

    def minimax(self, maximizing: bool) -> int:
        """
        Minimax algorithm.

        Returns:
            +1  -> computer wins
             0  -> draw
            -1  -> human wins
        """

        if self.check_winner(self.computer):
            return 1

        if self.check_winner(self.human):
            return -1

        if self.is_draw():
            return 0

        if maximizing:
            best_score = -float("inf")

            for index in range(9):
                if self.board[index] == " ":
                    self.board[index] = self.computer

                    score = self.minimax(False)

                    self.board[index] = " "

                    best_score = max(best_score, score)

            return int(best_score)

        best_score = float("inf")

        for index in range(9):
            if self.board[index] == " ":
                self.board[index] = self.human

                score = self.minimax(True)

                self.board[index] = " "

                best_score = min(best_score, score)

        return int(best_score)

    def computer_move(self) -> None:
        """Find and play the best move using Minimax."""
        best_score = -float("inf")
        best_move: Optional[int] = None

        for index in range(9):
            if self.board[index] == " ":
                self.board[index] = self.computer

                score = self.minimax(False)

                self.board[index] = " "

                if score > best_score:
                    best_score = score
                    best_move = index

        if best_move is not None:
            self.board[best_move] = self.computer

    def play(self) -> None:
        """Run the game."""
        print("=" * 30)
        print("       TIC-TAC-TOE")
        print("=" * 30)

        print("\nYou are X.")
        print("Computer is O.")
        print("Choose positions using numbers 1-9:\n")

        print(" 1 | 2 | 3 ")
        print("---+---+---")
        print(" 4 | 5 | 6 ")
        print("---+---+---")
        print(" 7 | 8 | 9 ")

        while not self.game_over():
            # Human turn
            self.human_move()
            self.display_board()

            if self.check_winner(self.human):
                print("🎉 You win!")
                return

            if self.is_draw():
                print("🤝 It's a draw!")
                return

            # Computer turn
            print("Computer is thinking...")
            self.computer_move()
            self.display_board()

            if self.check_winner(self.computer):
                print("💻 Computer wins!")
                return

            if self.is_draw():
                print("🤝 It's a draw!")
                return


def main() -> None:
    game = TicTacToe()
    game.play()


if __name__ == "__main__":
    main()
