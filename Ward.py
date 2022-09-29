from math import *
from re import M
import numpy as np
from itertools import combinations
from itertools import product
#Funcion Algoritmo Ward
def Ward(D):
    #Crea matriz para algoritmo
    W=[]
    for i in range(n):
        W.append([0]*n)
    for i in range(n):
        for j in range(n):
            if i==j:
                W[i][j]=0
            if j<i:
                W[i][j]=((N[i]*N[j])/(N[i]+N[j]))*D[i][j]
            else:
                W[i][j]=0
    m=W[1][0]
    #Busca el mismo
    for j in range(1,n):
        for i in range(j):
            if W[j][i]<m:
                m=W[j][i]
                fijarclus=j
                fijari=i
                maxx=max(fijarclus,fijari)
                minn=min(fijarclus,fijari)
            break
    #Guarda los clusters por unir
    N[maxx]=N[maxx]+1
    N[minn]=0
    clus=n-1
    #Crea nueva matriz de distancias
    Dcopy=[]
    for i in range(n):
        Dcopy.append([0]*n)
    for i in range(n):
        for j in range(n):
            if j!=fijari and i!=fijarclus:
                Dcopy[i][j]=D[i][j]
            if i==maxx and j<minn:
                Dcopy[i][j]=min(D[i][j],D[minn][j])
            if i==maxx and j==minn: 
                Dcopy[i][j]=0    
            if j>minn and i!=maxx:
                Dcopy[i][j]=D[i][j]
            if i==maxx and j>minn and j<i:
                Dcopy[i][j]=min(D[i][j],D[j][minn])
    return Dcopy
#Funcion para concatenar
def concatena(x1, x2):
    y = []
    for i in x1:
        y.append(i) #Append une elementos a vectores
    for j in x2:
        y.append(j)
    return y

#Funcion para impriir matrices
def imp(C):
    for i in C:
        for e in i:
            print("{:12.5f}".format(e), end=" ")
        print()
#Euclidiana
def Sum(A,B):
    V=[]
    s=0
    for i in len(A):
        V[i]=A[i]-B[i]
    for i in len(A):
        s=s+V[i]**2
    return sqrt(s)


#Pedir n, p y k
n = eval(input("Número de observciones: "))
p = eval(input("Número de variables: "))
k = eval(input("Número deseado de clusters: "))

#--------------------------------------------------------------------------------
#Crea la matriz vacia
A = []
for i in range(n):
    A.append([0]*p) #Aqui añadimos p espacios vacios a cada entrada de A
#Llena la matriz vacia    
for i in range(n):
    for j in range(p):
        A[i][j] = eval(input())

imp(A)
#---------------------------------------------------------------------------------

#Matriz de distancias
D=[]
for i in range(n):
    D.append([0]*n)
for i in range(n):
    for j in range(i):
        if i==j:
            D[i][j]=0
        if j<i:
            s=0
            for k in range(p):
                s=s+(A[i][k]-A[j][k])**2
            D[i][j]=sqrt(s)
for i in range(n):
    for j in range(n):
        if j>i:
            D[i][j]=D[j][i]
print("La matriz de distancias es ")
imp(D)
print("")
# ---------------------------------------------------------------------------
# Vector que guarda las cardinalidades
N= []*n
for i in range(n):
    N[i]=1

#Guarda los clusters originales
clus=n
#Primera itereacion de ward
p=0
if k==1:
    D=Ward(D)
    print(D)

else:
    for i in range(k):
        if p+1<k:
            D=Ward(D)
        p=p+1
        if p==k:
            break
print()
print("La configuracion es ")
imp(D)
