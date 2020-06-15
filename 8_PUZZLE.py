import numpy as np
initial=[int(ele) for ele in input("Enter the initial state:").split(' ')]
#initial=[initial[:3],initial[3:6],initial[6:]]
final=[int(ele) for ele in input("Enter the goal state:").split(' ')]

def print_state():
    print(initial[:3])
    print(initial[3:6])
    print(initial[6:])
print_state()

def move(ch,pos):
    if ch=='A':
        initial[pos-1],initial[pos]=initial[pos],initial[pos-1]
    elif ch=='W':
        initial[pos-3],initial[pos]=initial[pos],initial[pos-3]
    elif ch=='D':
        initial[pos+1],initial[pos]=initial[pos],initial[pos+1]
    elif ch=='S':
        initial[pos+3],initial[pos]=initial[pos],initial[pos+3]
while(initial!=final):
    ch=input('Enter:\nW - Up\nA - Left\nS - Down\nD - Right\n')
    pos=initial.index(0)
    avail_moves=[]
    if(pos==0):
        avail_moves=['D','S']
    elif pos==1:
        avail_moves=['A','S','D']
    elif pos==2:
        avail_moves=['S','A']
    elif pos==3:
        avail_moves=['W','S','D']
    elif pos==4:
        avail_moves=['A','S','D','W']
    elif pos==5:
        avail_moves=['W','S','A']
    elif pos==6:
        avail_moves=['W','D']
    elif pos==7:
        avail_moves=['W','A','D']
    elif pos==8:
        avail_moves=['W','A']
    
    if(ch in avail_moves):
        move(ch,pos)
        print_state()
        
        if(initial==final):
            print("Final State reached!")
            break;
        print('\n')
            
    else:
        print("Wrong Move")
