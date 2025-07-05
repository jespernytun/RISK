#Dette programmet er en simulasjon for å se om det er en fordel å være angriper
#eller forsvarer i RISK

from random import randint

def Kast(ArmeAngriper, ArmeForsvarer):
    while ArmeForsvarer >= 2 and ArmeAngriper >= 4:
        #simulrer forsvarers og angripers terningkast og sorterer de
        ForsvarerTerninger = sorted([randint(1,6),randint(1,6)])
        AngriperTerninger = sorted([randint(1,6),randint(1,6),randint(1,6)])
        ForsvarerTerninger.reverse()
        AngriperTerninger.reverse()

        VelykketForsvar = 0
        VelykketAngrep = 0

        Win = False
        
        if AngriperTerninger[0] > ForsvarerTerninger[0]:
            ArmeForsvarer = ArmeForsvarer - 1
        else:
            ArmeAngriper = ArmeAngriper -1
            VelykketForsvar = VelykketForsvar +1
        
        if AngriperTerninger[1] > ForsvarerTerninger[1]:
            ArmeForsvarer = ArmeForsvarer - 1
        else:
            ArmeAngriper = ArmeAngriper -1
            
    #Simulasjoner
    while ArmeForsvarer >= 2 and ArmeAngriper == 3:
        #simulrer forsvarers og angripers terningkast og sorterer de
        ForsvarerTerninger = sorted([randint(1,6),randint(1,6)])
        AngriperTerninger = sorted([randint(1,6),randint(1,6)])
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
 
    while ArmeForsvarer >= 2 and ArmeAngriper == 2:
        #simulrer forsvarers og angripers terningkast og sorterer de
        ForsvarerTerninger = sorted([randint(1,6),randint(1,6)])
        AngriperTerninger = sorted([randint(1,6)])
        ForsvarerTerninger.reverse()
        AngriperTerninger.reverse()

        VelykketForsvar = 0
        VelykketAngrep = 0

        if AngriperTerninger[0] > ForsvarerTerninger[0]:
            ArmeForsvarer = ArmeForsvarer - 1
        else:
            ArmeAngriper = ArmeAngriper - 1
        
    while ArmeForsvarer == 1 and ArmeForsvarer >= 1:
        ForsvarerTerninger = sorted([randint(1,6)])
        ForsvarerTerninger.reverse()
        
        if ArmeAngriper >= 4:
            AngriperTerninger = sorted([randint(1,6),randint(1,6),randint(1,6)])
            AngriperTerninger.reverse()
        elif ArmeAngriper == 3:
            AngriperTerninger = sorted([randint(1,6),randint(1,6)])
            AngriperTerninger.reverse()
        elif ArmeAngriper == 2:
            AngriperTerninger = sorted([randint(1,6)])
            AngriperTerninger.reverse()

        if AngriperTerninger[0] > ForsvarerTerninger[0]:
            ArmeForsvarer = 0
        else:
            ArmeAngriper = ArmeAngriper - 1

        if ArmeForsvarer == 0:
            Win = True

    print(Win)
    return Win

Kast(100,100)