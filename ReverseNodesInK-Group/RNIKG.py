#Select the nodes , and reverse and delete it from list every selecting.
list=[1,2,3,4,5]
k=2
def rev(k,list):
    modified=[]
    while k < len(list):              
        temp= list[0:k]           #select
        temp.sort(reverse=True)   #reverse
        for k0 in temp:           #append and remove from list
            list.remove(k0) 
            modified.append(k0)
    for k in list:                #append the remaing
        modified.append(k)
    return modified

m= rev(k,list)

    
