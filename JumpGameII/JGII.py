# -*- coding:cp936 -*-
#Every step, jump to the farest index(the larger index+value is , the farther it will be).
#每步都跳至最远，索引与值的和越大，则越远
def index_plus_value(A):
    array=[]
    for k in range(len(A)):
        array.append(k+A[k])
    return array

#Creat a list that is the result of index + value    
def next_index(i):
    s= array[(i+1):(i+1+A[i])]
    for k in range(len(s)):
        if s[k]==max(s) and A[k]!= 0:
            i=k+1+i
            return i

#judge if this index can jump to the end
def judge(i):
    if i+A[i]+1 >=len(A):
        return True

#make a jump, calculate the steps
def jump():
    global array
    array=index_plus_value(A)
    steps=1
    global i
    try:
        while not judge(i):
            i=next_index(i) 
            steps+=1
    except TypeError:
        print """YOU SHALL NOT PASS!!!
Well maybe you don't want to stay.
I mean you are in a zero-trap, :)"""
    return steps

def main():
    global A, i
    A=[2,3,1,1,4]
    i=0
    return jump()
    
if __name__== '__main__':
    main()
