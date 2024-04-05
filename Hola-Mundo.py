import matplotlib.pyplot as plt
#caracter = input("Ingrese un caracter:")
#C = caracter
def plot_queens(queens):
    board = [[' 'for _ in range(4)] for _ in range(4)]
    for i, j in enumerate(queens):
        board[i][j] = " "

    plt.figure(figsize=(5, 5))
    plt.imshow([[0 if (i + j) % 2 == 0 else 1 for j in range(4)] for i in range(4)], cmap='binary')
    for i in range(4):
        for j in range(4):
            plt.text(j, i, board[i][j], ha='center', va='center', color='green' if board[i][j] == " " else 'black')

    plt.xticks([])
    plt.yticks([])
    plt.title('4 reynas')
    plt.show()

# Ejemplo de uso
queens_solution = [1, 3, 0, 2]  # Colocación de las reinas en el tablero
plot_queens(queens_solution)