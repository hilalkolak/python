from turtle import *
N=int(input("Köşe sayısı girin:"))
aci=360/N
pensize(2)

for x in range(N):
    forward(100)
    left(aci)
