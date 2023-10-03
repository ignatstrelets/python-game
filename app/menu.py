class Menu:
    def __init__(self, args, help_table):
        self.args = args
        self.help_table = help_table

    def show_menu(self):
        n = len(self.args)
        print("Available moves:")
        for i in range(1, n+1, 1):
            print("{} - {}".format(i, self.args[i-1]))
        print("0 - exit")
        print("? - help")

