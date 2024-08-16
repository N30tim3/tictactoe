from random import randrange

def display_board(board):
    """ Muestra el tablero en la consola """
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

def enter_move(board):
    """ Solicita al usuario su movimiento y actualiza el tablero """
    while True:
        try:
            move = int(input("Elige un número de 1 a 9 para colocar tu O: ")) - 1
            if move < 0 or move > 8:
                print("Número fuera del rango. Por favor elige un número entre 1 y 9.")
                continue
            row, col = divmod(move, 3)
            if board[row][col] in 'XO':
                print("Ese espacio ya está ocupado. Elige otro.")
                continue
            board[row][col] = 'O'
            break
        except ValueError:
            print("Entrada inválida. Por favor ingresa un número entero.")

def make_list_of_free_fields(board):
    """ Devuelve una lista de índices de campos libres """
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in 'XO':
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    """ Verifica si el jugador con el signo 'sign' ha ganado """
    winning_combinations = [
        # Filas
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columnas
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonales
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]
    return any(all(board[row][col] == sign for row, col in combo) for combo in winning_combinations)

def draw_move(board):
    """ La máquina hace su movimiento aleatorio y actualiza el tablero """
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = free_fields[randrange(len(free_fields))]
        board[row][col] = 'X'

def tic_tac_toe():
    """ Función principal para ejecutar el juego """
    board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    
    # Primer movimiento de la máquina
    #board[1][1] = 'X'
    draw_move(board)
    display_board(board)
    
    while True:
        # Verificar si hay un ganador
        if victory_for(board, 'X'):
            display_board(board)
            print("¡La máquina gana!")
            break
        if victory_for(board, 'O'):
            display_board(board)
            print("¡Felicidades, ganas!")
            break
        if not make_list_of_free_fields(board):
            display_board(board)
            print("¡Empate!")
            break
        
        # Movimiento del usuario
        enter_move(board)
        display_board(board)
        
        # Movimiento de la máquina
        if not make_list_of_free_fields(board):
            display_board(board)
            print("¡Empate!")
            break
        draw_move(board)
        display_board(board)

if __name__ == "__main__":
    tic_tac_toe()
