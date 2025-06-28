import tkinter as tk

# Initialize the board with all empty cells
board = [['' for _ in range(11)] for _ in range(11)]
score_checker = [['' for _ in range(len(board))] for _ in range(len(board))]
moves = 0


def initialize_board():
    for row in range(len(board)):
        for col in range(len(board)):
            if row % 2 == 0 and col % 2 == 0:
                board[row][col] = 'o'
            else:
                board[row][col] = ' '


def print_check_scorer():
    for row in score_checker:
        print(' '.join(row))


def copy_board():
    for row in range(len(board)):
        for col in range(len(board)):
            score_checker[row][col] = board[row][col]


def print_board():
    for row in board:
        print(' '.join(row))


def check_point2(player):
    scored = False
    score_counter = 0
    r1 = -1;
    c1 = -1;
    r2 = -1;
    c2 = -1;
    for row in range(len(board)):
        for col in range(len(board)):
            if row % 2 == 1 and col % 2 == 1 and board[row][col] == ' ':
                x1 = row;
                y1 = col - 1;
                x2 = row - 1;
                y2 = col;
                x3 = row;
                y3 = col + 1;
                x4 = row + 1;
                y4 = col;
                if board[x1][y1] == '|' and board[x3][y3] == '|' and board[x2][y2] == '_' and board[x4][y4] == '_':
                    board[row][col] = player;
                    scored = True;
                    score_counter += 1;
                    if score_counter == 1:
                        r1 = row;
                        c1 = col;
                    elif score_counter == 2:
                        r2 = row;
                        c2 = col;
    return scored, r1, c1, r2, c2


def scores():
    score1 = 0;
    score2 = 0;
    for i in range(len(board)):
        for j in range(len(board)):
            if i % 2 == 1 and j % 2 == 1:  # only check the box slots where both coordinates are odd.
                if board[i][j] == '1':
                    score1 += 1
                elif board[i][j] == '2':
                    score2 += 1
    return score1, score2


def check_score():
    score1, score2 = scores()

    maxscore = int(len(board) / 2)
    maxscore = maxscore * maxscore
    halfscore = int(
        maxscore / 2)  # in 5 by 5 board the max number of points are 16, so if a player gets more than 8 they win.
    # if (score1>halfscore): return -100
    # elif (score2>halfscore): return 100
    return (score2 - score1)


def check_hard_score(player, difficulty):  ###
    score = 0
    score1 = 0
    score2 = 0
    for row in range(len(board)):
        for col in range(len(board)):
            score = 0
            if row % 2 == 1 and col % 2 == 1:
                if board[row][col] == '1' and score_checker[row][col] == ' ':
                    score1 += 10
                elif board[row][col] == '2' and score_checker[row][col] == ' ':
                    score2 += 10
                else:
                    x1 = row;
                    y1 = col - 1;
                    if board[x1][y1] == '|': score += 1
                    x2 = row - 1;
                    y2 = col;
                    if board[x2][y2] == '_': score += 1
                    x3 = row;
                    y3 = col + 1;
                    if board[x3][y3] == '|': score += 1
                    x4 = row + 1;
                    y4 = col;
                    if board[x4][y4] == '_': score += 1
            if player == '1':
                if score == 3:
                    score2 += 5;
                elif score == 2:
                    score2 += 1
            if player == '2':
                if score == 3:
                    score1 += 5;
                elif score == 2:
                    score1 += 1

    return score2 - score1


def make_a_move(row, col, direction):
    move_made = False
    r = row;
    c = col  # saving a copy before changing the values because we will have to pass these values in the check_point function
    # calculate the coordinate of where to plce the line:-
    row = row * 2;
    col = col * 2
    if direction == 'u':
        row = row - 1
    elif direction == 'd':
        row = row + 1
    elif direction == 'r':
        col = col + 1
    else:  # direction == 'l'
        col = (col - 1)

    if board[row][col] == ' ':
        if direction == 'l' or direction == 'r':
            board[row][col] = '_';
        elif direction == 'u' or direction == 'd':
            board[row][col] = '|'
        move_made = True
    else:
        move_made = False
    return move_made


def minimax(player, alpha, beta, depth, difficulty):  ###
    # if depth==3 or (check_score()==100 and depth==1) or (check_score()==-100 and depth==1):
    if depth == 0:
        if difficulty == "h":
            score = check_hard_score(player, difficulty)
        else:
            score = check_score() * (depth + 1)
        return score, None, None

    if player == '2':
        bestscore = -100000;
        row = None;
        col = None;
        for i in range(len(board)):
            for j in range(len(board)):
                if i % 2 == 0 and j % 2 == 1 and board[i][j] == ' ':
                    board[i][j] = '_'
                elif i % 2 == 1 and j % 2 == 0 and board[i][j] == ' ':
                    board[i][j] = '|'
                else:
                    continue
                _, r1, c1, r2, c2 = check_point2(player)
                if r1 > -1 or r2 > -1:
                    score, _, _ = minimax('2', alpha, beta, depth - 1, difficulty)
                else:
                    score, _, _ = minimax('1', alpha, beta, depth - 1, difficulty)
                board[i][j] = ' '
                if r1 > -1: board[r1][c1] = ' '
                if r2 > -1: board[r2][c2] = ' '
                if (score > bestscore):
                    bestscore = score;
                    row = i;
                    col = j;
                alpha = max(alpha, bestscore);
                if (alpha >= beta): break
        return bestscore, row, col

    if player == '1':
        bestscore = 100000;
        row = None;
        col = None;
        for i in range(len(board)):
            for j in range(len(board)):
                if i % 2 == 0 and j % 2 == 1 and board[i][j] == ' ':
                    board[i][j] = '_'
                elif i % 2 == 1 and j % 2 == 0 and board[i][j] == ' ':
                    board[i][j] = '|'
                else:
                    continue
                _, r1, c1, r2, c2 = check_point2(player)
                if r1 > -1 or r2 > -1:
                    score, _, _ = minimax('1', alpha, beta, depth - 1, difficulty)
                else:
                    score, _, _ = minimax('2', alpha, beta, depth - 1, difficulty)
                board[i][j] = ' '
                if r1 > -1: board[r1][c1] = ' '
                if r2 > -1: board[r2][c2] = ' '
                if (score < bestscore):
                    bestscore = score;
                    row = i;
                    col = j;
                beta = min(beta, bestscore);
                if (alpha >= beta): break
        return bestscore, row, col


# Function to get the screen width and height
def get_screen_size(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    return screen_width, screen_height


# Center the window on the screen
def center_window(window):
    screen_width, screen_height = get_screen_size(window)
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    x_coordinate = (screen_width - window_width) // 2
    y_coordinate = (screen_height - window_height) // 2
    window.geometry(f"+{x_coordinate}+{y_coordinate}")


class DifficultySelection(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Difficulty Selection")
        self.geometry("300x200")  # Set window size
        center_window(self)  # Center the window on the screen

        # Define colors for buttons
        easy_color = "green"
        medium_color = "orange"
        hard_color = "red"

        # Create buttons
        self.easy_button = tk.Button(self, text="Easy", command=lambda: self.select_difficulty("Easy"))
        self.easy_button.config(bg=easy_color, width=10, height=2)  # Set background color and size
        self.easy_button.pack(pady=10)

        self.medium_button = tk.Button(self, text="Medium", command=lambda: self.select_difficulty("Medium"))
        self.medium_button.config(bg=medium_color, width=10, height=2)  # Set background color and size
        self.medium_button.pack(pady=10)

        self.hard_button = tk.Button(self, text="Hard", command=lambda: self.select_difficulty("Hard"))
        self.hard_button.config(bg=hard_color, width=10, height=2)  # Set background color and size
        self.hard_button.pack(pady=10)

    def select_difficulty(self, difficulty):
        print(f"Selected difficulty: {difficulty}")
        self.destroy()  # Close the difficulty selection window
        app = DotsAndBoxes(difficulty)
        app.mainloop()


class DotsAndBoxes(tk.Tk):
    def __init__(self, difficulty):
        super().__init__()
        self.title("Dots and Boxes: " + difficulty)
        self.size = 6
        self.cell_size = 50
        self.dot_radius = 4
        self.canvas_width = self.cell_size * (self.size + 1)
        self.canvas_height = self.cell_size * (self.size + 1) + 20  # Added 20 for the label
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.turn_label = tk.Label(self.canvas, text="Player 1's Turn", font=("Arial", 12))
        self.canvas.create_window(self.canvas_width // 2, self.canvas_height - 40, window=self.turn_label)
        self.score_label1 = tk.Label(self.canvas, text="P1 score: 0", font=("Arial", 12), fg="red")
        self.score_label2 = tk.Label(self.canvas, text="P2 score: 0", font=("Arial", 12), fg="blue")
        self.canvas.create_window(self.canvas_width // 4, self.canvas_height - 10, window=self.score_label1)
        self.canvas.create_window(3 * self.canvas_width // 4, self.canvas_height - 10, window=self.score_label2)
        center_window(self)  # Center the window on the screen
        self.dots_layer = self.canvas.create_oval(0, 0, 0, 0)  # Layer for dots
        self.lines_layer = self.canvas.create_line(0, 0, 0, 0)  # Layer for lines
        self.lines = []
        self.draw_grid()
        self.selected_dot = None
        self.row1 = -1
        self.col1 = -1
        self.player = '1'
        initialize_board()  # Call initialize_board at the start of the program
        self.size = int(len(board) / 2)
        self.moves = self.size * (
                    self.size + 1) * 2  # Total number of possible moves that can be made when the game starts
        print("Moves left: ", self.moves)
        print()
        self.difficulty = "e"
        if difficulty == "Medium":
            self.difficulty = "m"
        elif difficulty == "Hard":
            self.difficulty = "h"
        print(self.difficulty)

    # Draw the grid for the GUI
    def draw_grid(self):
        for row in range(self.size):
            for col in range(self.size):
                x0, y0 = col * self.cell_size + 10, row * self.cell_size + 10
                dot = self.canvas.create_oval(x0 - self.dot_radius, y0 - self.dot_radius,
                                              x0 + self.dot_radius, y0 + self.dot_radius,
                                              fill="black")
                self.canvas.tag_bind(dot, "<Button-1>", lambda event, dot=(row, col): self.on_dot_click(dot))

    # Define label at the bottom of the Grid
    def update_turn_label(self):
        player_name = "Player 1" if self.player == '1' else "Player 2"
        self.turn_label.config(text=f"{player_name}'s Turn")

    def update_score_label(self, player):
        if player == '1':
            score1, _ = scores()
            self.score_label1.config(text="P1 score: " + str(score1))
        else:
            _, score2 = scores()
            self.score_label2.config(text="P2 score: " + str(score2))

    # Color around a dot
    def circle_dot(self, row, col, color):
        x0, y0 = col * self.cell_size + 10, row * self.cell_size + 10
        self.canvas.create_oval(x0 - self.dot_radius - 2, y0 - self.dot_radius - 2,
                                x0 + self.dot_radius + 2, y0 + self.dot_radius + 2,
                                outline=color, width=2)

    # Color around a selected dot red
    def highlight_dot(self, row, col):
        self.circle_dot(row, col, "red")

    # Unselecting a dot by coloring around it white
    def unhighlight_dot(self, row, col):
        self.circle_dot(row, col, "white")

    # Decrement moves
    def decrement_moves(self):
        self.moves -= 1
        print("Moves left: ", self.moves)
        print()
        if self.moves == 0:
            self.end_game()

    # Writes the player number that made the bow in it
    def write_player_number_in_box(self, row, col):
        row = row - ((row + 1) // 2)
        col = col - ((col + 1) // 2)
        x = col * self.cell_size + self.cell_size // 2
        y = row * self.cell_size + self.cell_size // 2
        self.canvas.create_text(x, y, text=self.player, font=("Arial", 12))

    # Ends the game, makes it unclickable and displays the result
    def end_game(self):
        self.canvas.unbind("<Button-1>")  # Disable further clicks
        # self.turn_label.config(text="Game Over")
        score = check_score()
        halfscore = int((self.size * self.size) / 2)
        if score < 0:
            print("player 1 wins")
            self.turn_label.config(text="Game Over, P1 wins!")
        elif score > 0:
            print("player 2 wins")
            self.turn_label.config(text="Game Over, P2 wins!")
        else:
            print("Draw")
            self.turn_label.config(text="Game Over, Draw!")

    # Called when a dot is clicked, facilitates the player to draw a line
    def on_dot_click(self, dot):
        if self.moves == 0:
            self.end_game()
            return
        row, col = dot
        if self.row1 != -1:
            if self.row1 == row and self.col1 == col:
                self.row1 = -1
                self.col1 = -1
                self.unhighlight_dot(row, col)
            else:
                if abs(self.row1 - row) + abs(self.col1 - col) == 1:
                    x0, y0 = col * self.cell_size + 10, row * self.cell_size + 10
                    x1, y1 = self.col1 * self.cell_size + 10, self.row1 * self.cell_size + 10
                    # color = "red" if self.player == '1' else "blue"
                    direction = ""
                    if row == self.row1 - 1:
                        direction = "u"
                    elif row == self.row1 + 1:
                        direction = "d"
                    elif col == self.col1 - 1:
                        direction = "l"
                    elif col == self.col1 + 1:
                        direction = "r"

                    valid_move = make_a_move(self.row1, self.col1, direction)
                    if valid_move:
                        line = self.canvas.create_line(x0, y0, x1, y1, fill="red", width=2)
                        self.canvas.lower(line)  # Move the line to the bottom layer
                        self.lines.append(line)
                        print(f"P{self.player}: {self.row1}, {self.col1}, {direction}")
                        self.unhighlight_dot(self.row1, self.col1)
                        self.row1 = -1
                        self.col1 = -1
                        copy_board()
                        print_board()
                        self.decrement_moves()
                        scored, rr, cc, _, _ = check_point2(self.player)
                        if scored == False and self.moves > 0:
                            self.player = '2'
                            self.update_turn_label()
                            while True and self.moves > 0:
                                depth = 3
                                if self.moves < depth:
                                    depth = self.moves
                                _, r, c = minimax(self.player, -10000, 10000, depth, self.difficulty)
                                if r % 2 == 0:
                                    board[r][c] = '_'
                                    d = 'r'
                                else:
                                    board[r][c] = '|'
                                    d = 'd'
                                r = int(r / 2)
                                c = int(c / 2)
                                print("Computer: ", r, ",", c, ",", d)
                                if d == 'r':
                                    r2 = r
                                    c2 = c + 1
                                else:  # d == 'd'
                                    r2 = r + 1
                                    c2 = c
                                x0, y0 = c2 * self.cell_size + 10, r2 * self.cell_size + 10
                                x1, y1 = c * self.cell_size + 10, r * self.cell_size + 10
                                line = self.canvas.create_line(x0, y0, x1, y1, fill="blue", width=2)
                                self.canvas.lower(line)  # Move the line to the bottom layer
                                self.lines.append(line)
                                copy_board()
                                print_board()
                                self.decrement_moves()
                                scored, rr, cc, _, _ = check_point2(self.player)
                                if scored == False:
                                    self.player = '1'
                                    self.update_turn_label()
                                    break
                                else:
                                    self.write_player_number_in_box(rr, cc)
                                    self.update_score_label(self.player)
                        else:
                            self.write_player_number_in_box(rr, cc)
                            self.update_score_label(self.player)
                    else:
                        print("Sorry this position is taken")
                else:
                    print("Invalid move. Please select a neighboring dot.")
        else:
            self.row1 = row
            self.col1 = col
            self.highlight_dot(row, col)


if __name__ == "__main__":
    app = DifficultySelection()
    app.mainloop()
