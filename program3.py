win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)

def game(player):
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))

    while True:
        try:
            ch = int(input(f"Enter player {player}'s choice: "))
            if ch < 1 or ch > 9 or str(mesh[ch - 1]) in ['X', 'O']:
                raise ValueError
            mesh[ch - 1] = player
            break
        except ValueError:
            print("Invalid position number. Please try again.")

    for wp in win_positions:
        if all(mesh[pos] == player for pos in wp):
            return wp
    return None

player1 = "X"
player2 = "O"
player = player1
mesh = list("123456789")

for i in range(9):
    won = game(player)
    print("\n", " | ".join(mesh[:3]))
    print("---+---+---")
    print("", " | ".join(mesh[3:6]))
    print("---+---+---")
    print("", " | ".join(mesh[6:]))

    if won:
        print(f"*** Player {player} won! ***")
        break
    player = player1 if player == player2 else player2
else:
    print("Game ends in a draw.")
1
2
4
5
