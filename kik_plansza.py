
def nowa_pusta_plansza():
    return ([[0,0,0], [0,0,0], [0,0,0]])
   
#zwraca nową tablicę zawierającą reprezentację pustej planszy;
def wykonaj_ruch(plansza, czyj_ruch, wiersz, kolumna):
    if plansza[wiersz][kolumna]==0:
        wykonalny=True
        
    else:
        wykonalny=False
     
    if wykonalny==True:
        plansza[wiersz][kolumna]=czyj_ruch
        czyj_ruch=0-czyj_ruch
    return(wykonalny, plansza, czyj_ruch)
            
#zwraca:
#odpowiedź na pytanie, czy ruch jest wykonalny (prawda lub fałsz),
#stan planszy po wykonaniu ruchu (lub planszę bez zmian, jeśli był niewykonalny),
#1 lub -1 w zależności od tego czyj teraz będzie ruch (jeśli poprzedni był niewykonalny, to pozostaje ten sam);
def koniec_gry(plansza):
    if (([1,1,1] in plansza) or (plansza[0][0]==1 and plansza[0][1]==1 and plansza[0][2]==1) or
        (plansza[0][0]==1 and plansza[1][0]==1 and plansza[2][0]==1) or
        (plansza[1][0]==1 and plansza[1][1]==1 and plansza[1][2]==1) or
        (plansza[2][0]==1 and plansza[2][1]==1 and plansza[2][2]==1) or
        (plansza[0][1]==1 and plansza[1][1]==1 and plansza[2][1]==1) or
        (plansza[0][2]==1 and plansza[1][2]==1 and plansza[2][2]==1)):
            wygral=1
    elif (([-1,-1,-1] in plansza) or (plansza[0][0]==-1 and plansza[0][1]==-1 and plansza[0][2]==-1) or
        (plansza[0][0]==-1 and plansza[1][0]==-1 and plansza[2][0]==-1) or
        (plansza[1][0]==-1 and plansza[1][1]==-1 and plansza[1][2]==-1) or
        (plansza[2][0]==-1 and plansza[2][1]==-1 and plansza[2][2]==-1) or
        (plansza[0][1]==-1 and plansza[1][1]==-1 and plansza[2][1]==-1) or
        (plansza[0][2]==-1 and plansza[1][2]==-1 and plansza[2][2]==-1)):
            wygral=-1
    else:
        wygral=0
    if(wygral!=0):
        koniec=True
    else:
        koniec=False
    if(koniec==True):
        return(True, wygral)
    elif(plansza[0][0]!=0 and plansza[0][1]!=0 and plansza[0][2]!=0 and
       plansza[1][0]!=0 and plansza[1][1]!=0 and plansza[1][2]!=0 and 
       plansza[2][0]!=0 and plansza[2][1]!=0 and plansza[2][2]!=0):
        return(True, 0)
    else:
        return(False, 0)
        
        
         #zwraca:
#odpowiedź na pytanie, czy gra w podanym stanie jest skończona (prawda lub fałsz),
#0 jeśli gra nie jest skończona, a 1/-1/0 (wygrana odpowiedniej strony lub remis), gdy jest skończona.

#PS. Umowa: na planszy 0 oznacza puste pole, -1 oznacza krzyżyk, 1 oznacza kółko.
