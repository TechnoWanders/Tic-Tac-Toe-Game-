def value_checker(player1, player2, ground, x1, y1, x):
    #print(x1,y1)
    if(x1>2 or y1>2 or x1<0 or y1<0):
        print("ERROR::XXXX, OUT OF BOUNDS ")
        go(player1, player2, ground, x)
        
    elif(ground[x1][y1] != '-'):
        print("ERROR::XXXX, YOU CANNOT OVERWRITE THE VALUE ")
        go(player1, player2, ground, x)
    else:
        return 
    
def algo_check2(main, val):
    for item in main:
        count = 0
        for item2 in item:
            #print(item2)
            if(item2 == val):
                count = count+1
        #print(count)
        if(count==3):
            return True
        else:
            continue
    return False 
    
def algo_check(ground,val):
    row1 = [ground[0][0], ground[0][1], ground[0][2]]
    row2 = [ground[1][0], ground[1][1], ground[1][2]]
    row3 = [ground[2][0], ground[2][1], ground[2][2]]
    column1 = [ground[0][0], ground[1][0], ground[2][0]]
    column2 = [ground[0][1], ground[1][1], ground[2][1]]
    column3 = [ground[0][2], ground[1][2], ground[2][2]]
    diagonal1 = [ground[0][0], ground[1][1], ground[2][2]]
    diagonal2 = [ground[2][0], ground[1][1], ground[0][2]]
    main = [row1, row2, row3, column1, column2, column3, diagonal1, diagonal2]
    return algo_check2(main, val)

def gro(ground):
    print()
    for i in range(3):
        for j in range(3):
            print(ground[i][j],end=' ')
        print()
    print()
    
def go(player1, player2, ground,x):
    gro(ground)
    x1 = int(input("Enter the x-axis "))
    y1 = int(input("Enter the y-axis "))
    value_checker(player1, player2, ground, x1, y1, x)
    if(x==0):
        player = player1
        ground[x1][y1] = 'X'
        x = 1
    else:
        player = player2
        ground[x1][y1] = 'O'
        x = 0
    if(algo_check(ground,ground[x1][y1])==True):
        print(player," won")
        return main()
    go(player1,player2,ground,x)

def main():
    print()
    print("Welcome to the Tic Tac Toe Jungle")
    player1 = input("Enter the name of the first player ")
    player2 = input("Enter the name of the second player ")
    ground = [['-','-','-'],['-','-','-'],['-','-','-']]
    x = 0
    go(player1, player2, ground, x)
    
main()
