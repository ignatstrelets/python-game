from tabulate import tabulate
from app.determinator import *



class HelpTable:
    def __init__(self, arr):
        n=len(arr)+1
        table = [["" for _ in range(n)] for _ in range(n)]
        table[0][0] = " v PC\\User > "
        for i in range(1,n):
            table[0][i]=arr[i-1]
            table[i][0]=arr[i-1]
            for j in range(1,n):
                result = DeterminatorOfWin(arr, j-1).determine_win(i-1)
                if result == "You win!":
                    table[i][j] = "Win"
                elif result == "Computer wins!":
                    table[i][j] = "Lose"
                else:
                    table[i][j] = "Draw"


        self.ready_table = table

    def print(self):
        print(tabulate(self.ready_table, tablefmt="grid"))
