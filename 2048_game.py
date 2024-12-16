import random
import os


Grid = []  # this store 2048 grid
moved = True # if = false , player not move any block , then the game over
win = False

def clear_terminal():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


def init_state():
    global Grid  # Access the global variable Grid

    # Create 4x4 grid filled with 0
    Grid = [[0 for _ in range(4)] for _ in range(4)]  # Khởi tạo ma trận 4x4 chứa toàn số 0

    # Create first random number 2
    x1 = random.randint(0, 3)  # Chỉ số từ 0 đến 3
    y1 = random.randint(0, 3)
    Grid[x1][y1] = 2
    # # Create second random number 2, guarantee that it's not the same position
    # while True:
    #     x2 = random.randint(0, 3)
    #     y2 = random.randint(0, 3)
    #     if x2 != x1 or y2 != y1:  # Đảm bảo vị trí không trùng
    #         break
    # Grid[x2][y2] = 2
    #
    # """ DEBUG CASE"""
    # Grid = [[2048, 0, 0, 0],
    # [2, 0, 0, 0],
    # [0, 0, 0, 0],
    # [0, 0, 2, 0]]
def print_grid():
    for row in range (4):
        print(Grid[:][row])
def gen_new_num():
    while True:
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        if Grid[x][y] == 0:
            Grid[x][y]=2
            break
def handle_input( direction ):
    global moved
    global win
    global Grid
    stack = Stack()
    moved_in_input =False
    sum = True
    if direction == 'up':
        for j in range(0,4):
            for i in range(0,4):
                if Grid[i][j] == 0: continue
                elif Grid[i][j] == 2048:
                    win = True
                    return
                elif stack.is_empty() or stack.peek() != Grid[i][j] or not sum:
                    stack.push(Grid[i][j])
                    sum = True
                else:
                    sum = False
                    temp = stack.pop()
                    stack.push(temp*2)
                Grid[i][j] = 0
            while stack.size()<4:
                moved_in_input = True
                stack.push(0)
            for i in range(4):
                Grid[3-i][j] = stack.pop()


    elif direction == 'down':
        for j in range(4):
            for i in range(3,-1,-1):
                if Grid[i][j] == 0:
                    continue
                elif Grid[i][j] == 2048:
                    win = True
                    return
                elif stack.is_empty() or stack.peek() != Grid[i][j] or not sum:
                    stack.push(Grid[i][j])
                    sum = True
                else:
                    sum = False
                    temp = stack.pop()
                    stack.push(temp * 2)
                Grid[i][j] = 0
            while stack.size() < 4:
                moved_in_input = True
                stack.push(0)
            for i in range(4):
                Grid[i][j] = stack.pop()
    elif direction == 'left':
        for i in range( 4):
            for j in range( 4):
                if Grid[i][j] == 0:
                    continue
                elif Grid[i][j] == 2048:
                    win = True
                    return
                elif stack.is_empty() or stack.peek() != Grid[i][j] or not sum:
                    stack.push(Grid[i][j])
                    sum = True
                else:
                    sum = False
                    temp = stack.pop()
                    stack.push(temp * 2)
                Grid[i][j] = 0
            while stack.size() < 4:
                moved_in_input = True
                stack.push(0)
            for j in range(4):
                Grid[i][3-j] = stack.pop()
    elif direction == 'right':
        for i in range(4):
            for j in range(3,-1,-1):
                if Grid[i][j] == 0:
                    continue
                elif Grid[i][j] == 2048:
                    win = True
                    return
                elif stack.is_empty() or stack.peek() != Grid[i][j] or not sum:
                    stack.push(Grid[i][j])
                    sum = True
                else:
                    sum = False
                    temp = stack.pop()
                    stack.push(temp * 2)
                Grid[i][j] = 0
            while stack.size() < 4:
                moved_in_input = True
                stack.push(0)
            for j in range(4):
                Grid[i][ j] = stack.pop()
    else : raise ValueError("incorrect direction")
    if(moved_in_input ==False):moved = false
def game_loop():
    global moved
    global win
    while True:
        clear_terminal()
        gen_new_num()
        print_grid()
        command =input(" mời bạn nhập lệnh để di chuyển (1:up, 2:down, 3:left, 4:right) : ")
        if command == "1":
            handle_input("up")
        elif command == "2":
            handle_input("down")
        elif command == "3":
            handle_input("left")
        elif command == "4":
            handle_input("right")
        if not moved:
            print(" bạn đã thua khi không còn ô nào để di chuyển")
            return
        elif win:
            print(" bạn win r , hay á")
            return


def main():
    print(" Bắt đầu 2048 thoi :")
    init_state()
    game_loop()

main()
#
