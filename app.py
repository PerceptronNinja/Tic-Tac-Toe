from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

# Initialize game variables
game_board = [""] * 9
current_player = "X"
player1_name = ""
player2_name = ""
player1_score = 0
player2_score = 0
game_over = False
match_result = ""

@app.route("/", methods=["GET", "POST"])
def index():
    global player1_name, player2_name, player1_score, player2_score, game_board, current_player, game_over, match_result
    if request.method == "POST":
        player1_name = request.form["player1_name"]
        player2_name = request.form["player2_name"]
        return redirect(url_for("game"))
    return render_template("index.html", player1_name=player1_name, player2_name=player2_name)

@app.route("/game", methods=["GET", "POST"])
def game():
    global game_board, current_player, player1_score, player2_score, game_over, match_result

    if request.method == "POST":
        # Reset game board for a new game
        game_board = [""] * 9
        current_player = "X"
        game_over = False
        match_result = ""

    return render_template("game.html", board=game_board, current_player=current_player,
                           player1_name=player1_name, player2_name=player2_name,
                           player1_score=player1_score, player2_score=player2_score,
                           game_over=game_over, match_result=match_result)

@app.route("/move/<int:cell>")
def make_move(cell):
    global game_board, current_player, player1_score, player2_score, game_over, match_result

    if game_board[cell] == "" and not game_over:
        game_board[cell] = current_player
        if check_winner():
            if current_player == "X":
                player1_score += 1
            else:
                player2_score += 1
            match_result = f"Player {current_player} wins!"
            game_over = True
            return redirect(url_for("result"))
        elif check_draw():
            match_result = "Match Draw!"
            game_over = True
            return redirect(url_for("result"))
        current_player = "O" if current_player == "X" else "X"
    return redirect(url_for("game"))

@app.route("/result")
def result():
    return render_template("result.html", match_result=match_result, game_over=game_over)

@app.route("/reset")
def reset():
    global game_board, current_player, game_over, match_result
    game_board = [""] * 9
    current_player = "X"
    game_over = False
    match_result = ""
    return redirect(url_for("game"))

@app.route("/new_game")
def new_game():
    global game_board, current_player, player1_score, player2_score, game_over, match_result
    game_board = [""] * 9
    current_player = "X"
    player1_score = 0
    player2_score = 0
    game_over = False
    match_result = ""
    return redirect(url_for("index"))

def check_winner():
    win_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)              # Diagonals
    ]
    for combo in win_combinations:
        if game_board[combo[0]] == game_board[combo[1]] == game_board[combo[2]] and game_board[combo[0]] != "":
            return True
    return False

def check_draw():
    return "" not in game_board

if __name__ == "__main__":
    app.run(debug=True)
