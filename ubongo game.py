import numpy as np
# the board matrix
arr = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] 
# array representing the four puzzle pieces 
arr1=[[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] ,  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]] , [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]     ]
# the waight of each puzzle piece  (the area of piece times its index)
length= [0,0,0,0]
summ=0
## this function checks all the indecies of the puzzle pieces to see wether it fit in the remainig space of grid or not
def check (s,x,y,k) :
    global summ
    global arr
    global arr1
    if (k==0):
        for i in range(0,4):
            if ((i-x)<0 ) : 
                continue 
            for j in range(0,4):
                if ((j-y)<0 or arr[i][j]!=1) :
                    continue 
                ## editing the board with the new value after adding the waight of the peices
                arr[i][j]+=np.rot90(arr1[s],0)[i-x][j-y]
                ## updated the sum by adding the waight of the puzzle peices
                summ+=np.rot90(arr1[s],0)[i-x][j-y]

    if (k==1):
        for i in range(0,4):
            if ((i-x)<0 ) : 
                continue 
            for j in range(0,4):
                if ((j-y)<0 or arr[i][j]!=1) :
                    continue 
                arr[i][j]+=np.rot90(arr1[s],3)[i-x][j-y]
                summ+=np.rot90(arr1[s],3)[i-x][j-y]

    if (k==2):
        for i in range(0,4):
            if ((i-x)<0 ) : 
                continue 
            for j in range(0,4):
                if ((j-y)<0 or arr[i][j]!=1) :
                    continue 
                arr[i][j]+=np.rot90(arr1[s],2)[i-x][j-y]
                summ+=np.rot90(arr1[s],2)[i-x][j-y]

    if (k==3):
        for i in range(0,4):
            if ((i-x)<0 ) : 
                continue 
            for j in range(0,4):
                if ((j-y)<0 or arr[i][j]!=1) :
                    continue 
                arr[i][j]+=np.rot90(arr1[s],1)[i-x][j-y]
                summ+=np.rot90(arr1[s],1)[i-x][j-y]

def undo (s,x,y,k) :
    global summ
    global arr
    global arr1
    if (k==0):
        for i in range(0,4):
            if ((i-x)<0) : 
                continue 
            for j in range(0,4):
                if ((j-y<0) or arr[i][j]!=s+3 ) :
                    continue 
                ## editing the board with the new value after subtracting the waight of the puzzle peices                
                arr[i][j]-=np.rot90(arr1[s],0)[i-x][j-y]
                ## updating the sum by subtracting the wiegh of the peice                
                summ-=np.rot90(arr1[s],0)[i-x][j-y] 

    if (k==1):
        for i in range(0,4):
            if ((i-x)<0) : 
                continue 
            for j in range(0,4):
                if ((j-y<0) or arr[i][j]!=s+3 ) :
                    continue 
                arr[i][j]-=np.rot90(arr1[s],3)[i-x][j-y]
                summ-=np.rot90(arr1[s],3)[i-x][j-y]
    if (k==2):
        for i in range(0,4):
            if ((i-x)<0) : 
                continue 
            for j in range(0,4):
                if ((j-y<0) or arr[i][j]!=s+3 ) :
                    continue 
                arr[i][j]-=np.rot90(arr1[s],2)[i-x][j-y]
                summ-=np.rot90(arr1[s],2)[i-x][j-y]

    if (k==3):
        for i in range(0,4):
            if ((i-x)<0) : 
                continue 
            for j in range(0,4):
                if ((j-y<0) or arr[i][j]!=s+3 ) :
                    continue 
                arr[i][j]-=np.rot90(arr1[s],3)[i-x][j-y]
                summ-=np.rot90(arr1[s],3)[i-x][j-y]


def BackTrack (s) : 
    for k in range (0,4) :
        for i in range (0,4) :
            for j in range (0,4) :
                temp=summ
                check  (s , i ,j ,k)  
                if (summ == temp+length[s] ) :

                    if ( s==3 ) :
                        print (arr[0])
                        print (arr[1])
                        print (arr[2])
                        print (arr[3])
                        quit()
                    else : BackTrack (s+1)
                undo (s, i , j ,0)


### inputting the board matrix
print ("please, input the board shape ")
for i in range(0,4):
    arr[i][0],arr[i][1],arr[i][2],arr[i][3]= (map (int,input ().split ()))
    summ+=arr[i][3]+arr[i][2]+arr[i][1]+arr[i][0] 

## inputting the four puzzle pieces
print ("please, input the 4 puzzle peices shapes ")

##giving each puzzle piece a special indication number
for i in range(0,4):
    arr1[0][i][0],arr1[0][i][1],arr1[0][i][2],arr1[0][i][3]= (map (int,input ().split ()))
    if (arr1[0][i][0]):arr1[0][i][0]+=1
    if (arr1[0][i][1]):arr1[0][i][1]+=1
    if (arr1[0][i][2]):arr1[0][i][2]+=1
    if (arr1[0][i][3]):arr1[0][i][3]+=1
    length[0]+=arr1[0][i][3]+arr1[0][i][2]+arr1[0][i][1]+arr1[0][i][0]                

for i in range(0,4):
    arr1[1][i][0],arr1[1][i][1],arr1[1][i][2],arr1[1][i][3]= (map (int,input ().split ()))
    if (arr1[1][i][0]):arr1[1][i][0]+=2
    if (arr1[1][i][1]):arr1[1][i][1]+=2
    if (arr1[1][i][2]):arr1[1][i][2]+=2
    if (arr1[1][i][3]):arr1[1][i][3]+=2
    length[1]+=arr1[1][i][3]+arr1[1][i][2]+arr1[1][i][1]+arr1[1][i][0]        

for i in range(0,4):
    arr1[2][i][0],arr1[2][i][1],arr1[2][i][2],arr1[2][i][3]= (map (int,input ().split ()))
    if (arr1[2][i][0]):arr1[2][i][0]+=3
    if (arr1[2][i][1]):arr1[2][i][1]+=3
    if (arr1[2][i][2]):arr1[2][i][2]+=3
    if (arr1[2][i][3]):arr1[2][i][3]+=3       
    length[2]+=arr1[2][i][3]+arr1[2][i][2]+arr1[2][i][1]+arr1[2][i][0]        


for i in range(0,4):
    arr1[3][i][0],arr1[3][i][1],arr1[3][i][2],arr1[3][i][3]= (map (int,input ().split ()))
    if (arr1[3][i][0]):arr1[3][i][0]+=4
    if (arr1[3][i][1]):arr1[3][i][1]+=4
    if (arr1[3][i][2]):arr1[3][i][2]+=4
    if (arr1[3][i][3]):arr1[3][i][3]+=4
    length[3]+=arr1[3][i][3]+arr1[3][i][2]+arr1[3][i][1]+arr1[3][i][0]




## start to check .....



BackTrack(0)


