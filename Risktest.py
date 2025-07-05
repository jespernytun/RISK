#Dette programmet er en simulasjon for å se om det er en fordel å være angriper
#eller forsvarer i RISK

from random import randint
import matplotlib.pyplot as plt

#definisjoner
N = 10000
ArmeForsvarer = N
ArmeAngriper = N


#Win/Loss/Tie counter
Win = 0
Loss = 0
Tie = 0


while ArmeForsvarer >= 4 and ArmeAngriper >= 3:
    #simulrer forsvarers og angripers terningkast og sorterer de
    ForsvarerTerninger = sorted([randint(1,6),randint(1,6)])
    AngriperTerninger = sorted([randint(1,6),randint(1,6),randint(1,6)])
    ForsvarerTerninger.reverse()
    AngriperTerninger.reverse()

    VelykketForsvar = 0
    VelykketAngrep = 0
    
    if AngriperTerninger[0] > ForsvarerTerninger[0]:
        ArmeForsvarer = ArmeForsvarer - 1
    else:
        ArmeAngriper = ArmeAngriper -1
        VelykketForsvar = VelykketForsvar +1
    
    if AngriperTerninger[1] > ForsvarerTerninger[1]:
        ArmeForsvarer = ArmeForsvarer - 1
    else:
        ArmeAngriper = ArmeAngriper -1
        VelykketForsvar = VelykketForsvar +1

    if VelykketForsvar == 0:
        Win += 1
    elif VelykketForsvar == 1:
        Tie += 1
    elif VelykketForsvar == 2:
        Loss += 1

Total = Win+Tie+Loss
xplot = ["Attacker Win", "Tie", "Attacker Loss"]
yplot = [Win*100/Total, Tie*100/Total, Loss*100/Total]


plt.bar(xplot,yplot)
plt.title("risk defender/attacker simulation N = 10000")
plt.xlabel("result")
plt.ylabel("percentage chance of given result")
plt.show()