from functools import reduce

def superpares(num):
    if num==0:
        return True
    else:
        if((num%10)%2==0):
            return True and superpares(num/10)
        else:
            return False

def MaxofList(L):
    return max(L)

def MinofList(L):
    return min(L)

def NumberTriangular(num):
    return ((num*(num+1))/2)

l=[123,224,313,426,512,648]
l2=[[1,3,5,8,48],[2,4,6,9,11],[4,5,7,10,12],[5,7,9,12,13]]
l3=[4,1,2,3,1024]
l4=[(1,3),(3,2),(21,6),(15,5)]


print("1.primer y ultimo elemento")
print(list(filter(lambda x: (x==l[0] or x==l[-1]),l)))
print("2.superpares")
print(list(filter(lambda x: superpares(x)==True,l)))
print("3.maximos de lista de listas")
print(list(map(lambda x: MaxofList(x), l2)))
print("4.minimos de lista de listas que es superpares")
print(list(filter(lambda x:superpares(x)==True,list(map(lambda x: MinofList(x),l2)))))
print("5.menos a la potencia de 5 de la cabeza")
print(list(filter(lambda x: x<pow(l3[0],5),l3)))
print("6.suma numero triangular")
l5=list(reduce((lambda x,y: x+y),list(filter(lambda x: x[0]==NumberTriangular(x[1]),l4))))
print(reduce(lambda x,y: x+y,list(filter(lambda x: l5.index(x)%2==0,l5))))