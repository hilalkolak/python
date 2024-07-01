def alan(u,g):
    A=u*g
    return A
def cevre(u,g): #ALT PROGRAM
    C=2*(u+g)
    return C

u=int(input("dikdörtgenin uzun kenarını gir:"))
g=int(input("dikdörtgenin kısa kenarını gir:")) #ANA PROGRAM
print("Dikdörtgenin Alanı=",alan(u,g),"m^2")
print("Dikdörtgenin Çevresi=",cevre(u,g),"m")
