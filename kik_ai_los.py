from random import *

##następującą funkcję obsługującą losową sztuczną „inteligencję”:

def wybierz_ruch(plansza, czyj_ruch):
    wiersz=randint(0, 2)
    kolumna=randint(0,2)
    while plansza[wiersz][kolumna]!=0:
        wiersz=randint(0, 2)
        kolumna=randint(0,2)
    return (wiersz, kolumna)
    
    
    
    
    
##która zwraca losowy, ale poprawny ruch
##(czyli współrzędne wiersza i kolumny) dla podanego gracza na podanej planszy.
##wykonaj_ruch(plansza, czyj_ruch, wiersz, kolumna)==
