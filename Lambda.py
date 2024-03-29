from functools import reduce

def superpares(num):
    if num==0:
        return True
    else:
        if((num%10)%2==0):
            return True and superpares(int(num/10))
        else:
            return False

def MaxofList(L):
    return max(L)

def MinofList(L):
    return min(L)

def listaSuper(L):
    return [x for x in L if superpares(x)==True]

def NumberTriangular(num):
    return ((num*(num+1))/2)

def CabezaCola(l):
    return l[0],l[-1]

l=[123,224,313,426,512,648]
l2=[[1,3,5,8,48],[2,4,6,9,11],[4,5,7,10,12],[22,5,7,9,12,13]]
l3=[4,1,2,3,1024]
l4=[(1,3),(3,2),(21,6),(15,5)]
l6=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]


print("1.primer y ultimo elemento")
print(list(map(lambda x: CabezaCola(x),l6)))
print("2.superpares")
print(list(filter(lambda x: superpares(x)==True,l)))
print("3.maximos de lista de listas")
print(list(map(lambda x: MaxofList(x), l2)))
print("4.minimos de lista de listas que es superpares")
print(list(map(lambda x: MinofList(x),list(map(lambda x:listaSuper(x),l2)))))
print("5.menos a la potencia de 5 de la cabeza")
print(list(filter(lambda x: x<pow(l3[0],5),l3)))
print("6.suma numero triangular")
l5=list(reduce((lambda x,y: x+y),list(filter(lambda x: x[0]==NumberTriangular(x[1]),l4))))
print(reduce(lambda x,y: x+y,list(filter(lambda x: l5.index(x)%2==0,l5))))
