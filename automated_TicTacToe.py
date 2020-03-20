import numpy as np
import time
board=[i for i in range(9)]
count=0
turn=0
print("The board positions are as given below. \nYou select one number where you want to mark O.\nThe computer is X.")
print(board[0:3])
print(board[3:6])
print(board[6:])
print('\n\n')
board=[2 for _ in range(9)]
def prod(b):
    return b[0]*b[1]*b[2]
def check():
    if(turn==0):
        print("Computer's turn:")
        if(prod(board[:3])==18):
            board[board[:3].index(2)]=3
            return -1
        elif(prod(board[3:6])==18):
            if board[3]==2:
                board[3]=3
            elif(board[4]==2):
                board[4]=3
            else:
                board[5]=3
            return -1
        elif(prod(board[6:])==18):
            if board[6]==2:
                board[6]=3
            elif(board[7]==2):
                board[7]=3
            else:
                board[8]=3
            return -1
        elif((board[1]*board[4]*board[7])==18):
            if(board[1]==2): 
                board[1]=3
            elif(board[4]==2):
                board[4]=3
            else:
                board[7]=3
            return -1
        elif((board[2]*board[5]*board[8])==18):
            if(board[2]==2): 
                board[2]=3
            elif(board[5]==2):
                board[5]=3
            else:
                board[8]=3
            return -1
        elif((board[0]*board[4]*board[8])==18):
            if(board[0]==2): 
                board[0]=3
            elif(board[4]==2):
                board[4]=3
            else:
                board[8]=3
            return -1
        elif((board[0]*board[3]*board[6])==18):
            if(board[0]==2): 
                board[0]=3
            elif(board[3]==2):
                board[3]=3
            else:
                board[6]=3
            return -1
        elif((board[2]*board[4]*board[6])==18):
            if(board[2]==2): 
                board[2]=3
            elif(board[4]==2):
                board[4]=3
            else:
                board[6]=3
            return -1
        else:
            r=np.random.randint(0,9)
            if(board[r]==2):
                board[r]=3
            else:
                board[board.index(2)]=3
            return 0
    elif(turn==1):
        if(prod(board[:3])==50):
            board[board[:3].index(2)]=5
            return -1
        elif(prod(board[3:6])==50):
            if board[3]==2:
                board[3]=5
            elif(board[4]==2):
                board[4]=5
            else:
                board[5]=5
            return -1
        elif(prod(board[6:])==50):
            if board[6]==2:
                board[6]=5
            elif(board[7]==2):
                board[7]=5
            else:
                board[8]=5
            return -1
        elif((board[1]*board[4]*board[7])==50):
            if(board[1]==2): 
                board[1]=5
            elif(board[4]==2):
                board[4]=5
            else:
                board[7]=5
            return -1
        elif((board[2]*board[5]*board[8])==50):
            if(board[2]==2): 
                board[2]=5
            elif(board[5]==2):
                board[5]=5
            else:
                board[8]=5
            return -1
        elif((board[0]*board[4]*board[8])==50):
            if(board[0]==2): 
                board[0]=5
            elif(board[4]==2):
                board[4]=5
            else:
                board[8]=5
            return -1
        elif((board[0]*board[3]*board[6])==50):
            if(board[0]==2): 
                board[0]=5
            elif(board[3]==2):
                board[3]=5
            else:
                board[6]=5
            return -1
        elif((board[2]*board[4]*board[6])==50):
            if(board[2]==2): 
                board[2]=5
            elif(board[4]==2):
                board[4]=5
            else:
                board[6]=5
            return -1
        else:
            r=np.random.randint(0,9)
            if(board[r]==2):
                board[r]=5
            else:
                board[board.index(2)]=5
            return 0
        
        
        
while(count!=9):
    count=count+1

    if(turn==0):
        a=check()
        turn=1
    else:
        a=check()
        turn=0
        #print("Your turn:")
        #a=int(input("Enter a position:"))
        #board[a]=5
        
    if(a==-1):
        print("Game Over!")
        board=['_' if ele==2 else ele for ele in board]
        board=['X' if ele==3 else ele for ele in board]
        board=['O' if ele==5 else ele for ele in board]
        print(board[0:3])
        print(board[3:6])
        print(board[6:])
        break
    else:
        print("Board State:")
        bo=board
        bo=['_' if ele==2 else ele for ele in bo]
        bo=['X' if ele==3 else ele for ele in bo]
        bo=['O' if ele==5 else ele for ele in bo]
        print(bo[0:3])
        print(bo[3:6])
        print(bo[6:])
        time.sleep(1)
