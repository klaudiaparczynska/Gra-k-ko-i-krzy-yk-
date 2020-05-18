from kik_ai_los import *

def sprawdz(plansza, czyj_ruch):
    if (plansza[0][0] + plansza[1][1] + plansza [2][2]==2*czyj_ruch):
        if plansza[0][0]==0:
            return (0,0)
        elif plansza[1][1]==0:
            return (1,1)
        elif plansza [2][2]==0:
            return (2,2)
        
    if (plansza[2][0] + plansza[1][1] + plansza[0][2] ==2*czyj_ruch):
        if plansza[2][0]==0:
            return (2,0)
        elif plansza[1][1]==0:
            return (1,1)
        elif plansza[0][2]==0:
            return (0,2)
        
    if (sum(plansza[0])==2*czyj_ruch):
        for i in range(3):
            if plansza[0][i]==0:
                return (0,i)
    if (sum(plansza[1])==2*czyj_ruch):
        for i in range(3):
            if plansza[1][i]==0:
                return (1,i)
    if (sum(plansza[2])==2*czyj_ruch):
        for i in range(3):
            if plansza[2][i]==0:
                return (2,i)
    if (plansza[0][0] + plansza[1][0]+ plansza[2][0]==2*czyj_ruch):
        for i in range(3):
            if plansza[i][0]==0:
                return (i,0)
    if (plansza[0][1] + plansza[1][1]+ plansza[2][1]==2*czyj_ruch):
        for i in range(3):
            if plansza[i][1]==0:
                return (i,1)
    if (plansza[0][2] + plansza[1][2]+ plansza[2][2]==2*czyj_ruch):
        for i in range(3):
            if plansza[i][2]==0:
                return (i,2)
            
def wybierz_ruch_int(plansza, czyj_ruch):
    wynik=sprawdz(plansza, czyj_ruch)
    if wynik!=None:
        return wynik
    wynik=sprawdz(plansza, 0-czyj_ruch)
    if wynik!=None:
        return wynik
    if plansza[1][1]==0:
        return (1,1)
    wynik=wybierz_ruch(plansza, czyj_ruch)
    return wynik
    
    
        
    
    
    
                        
            
        


    
