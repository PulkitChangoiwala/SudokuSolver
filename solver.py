




def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range (1,10): #1 inclusive 10 exclusive
       if valid(bo, i, (row,col)):
           bo[row][col] = i
           if solve(bo):
               return True
           bo[row][col] = 0


    return False








def valid(bo, num, pos):
    # check row
    for j in range(len(bo[0])):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False
    #check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # check square box
    box_x = pos[1] // 3 #integer division
    box_y = pos[0] // 3
    for i in range (box_y*3, box_y*3+3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j]==num and (i,j) != pos:
                return False

    return True




def print_board(bo):
    for i in range(len(bo)):
        if i%3 == 0 and i!=0:
            print("- - - - - - - - - - - -")
        for j  in range(len(bo[0])):
            if j%3==0 and j!=0:
                print(" | ", end="") #with print default new line is printed
            if j == 8 :
                print(bo[i][j])
            else :
                print(str(bo[i][j])+ " ", end="")





def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) #row, column
    return None

