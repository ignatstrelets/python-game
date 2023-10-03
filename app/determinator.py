class CircularList:
    def __init__(self, arr):
        self.arr = arr
        self.root = array_to_circular_list(arr)

    def search(self, index):
        for _ in self.arr:
            if self.root.index == index:
                return self.root
            else:
                self.root = self.root.next


class Node:
    def __init__(self, value):
        self.index = None
        self.value = value
        self.prev = None
        self.next = None


def get_node():
    return Node(0)


def array_to_circular_list(arr):
    n = len(arr)
    root = arr[0]
    new_node = None
    temp = None
    i = 0
    while i < n:
        new_node = get_node()
        new_node.value = arr[i]
        new_node.index = i
        if i == 0:
            root = new_node
            new_node.prev = root
            new_node.next = root
        else:
            temp = (root).prev
            temp.next = new_node
            new_node.next = root
            new_node.prev = temp
            temp = root
            temp.prev = new_node
        i = i + 1
    return root


class DeterminatorOfWin:
    def __init__(self, arr, index):
        self.index = index
        self.arr = arr
        self.circular_list = CircularList(arr)
        self.node = self.circular_list.search(index)
        self.half_arr_length = int((len(arr)-1)/2)
        self.lower_values = [0 for _ in range(self.half_arr_length)]
        prev_node = self.node
        for j in range(0, self.half_arr_length):
            prev_node = prev_node.prev
            self.lower_values[j] = prev_node.value

    def determine_win(self, computer_move):
        player_move = self.index
        if player_move == computer_move:
            return "Draw!"
        elif self.arr[computer_move] in self.lower_values:
            return "You win!"
        else:
            return "Computer wins!"


