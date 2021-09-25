import numpy as np 

goal_combination=np.array([[1,2,3],[4,5,6],[7,8,0]])

class state:
    def __init__(self,matno,parentno,mat):
        self.matno=matno
        self.parentno=parentno
        self.mat=mat
matrix_number=0
matrix=[]

n=int(input("How many matrix you want to take : "))


for i in range(n):
    mat=[[int(input()) for i in range(3)] for j in range(3)]
    matrix_number=matrix_number+1
    parentno=1
    start=np.array(mat)
    obj=state(matrix_number,parentno,start)
    matrix.append(obj)
    print(matrix[i].matno,matrix[i].parentno,matrix[i].mat)

while(matrix!=[]):
    popped_state=matrix[0]
    goal_flag=np.array_equal(popped_state.mat,goal_combination)
    matrix.pop(0)
    if(goal_flag==True):
        print("Goal Found")
        break

def checkgoal(p,g):
    if(np.array_equal(p,g)):
        return True
    return False   
       
checkgoal(popped_state.mat,goal_combination)







   



 




