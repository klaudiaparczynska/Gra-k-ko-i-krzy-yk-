from kik_plansza import *
from kik_kom import *

def wyswietl(plansza):
    print(" "+pionek(plansza[0][0])+
          " | "+pionek(plansza[0][1])+
          " | "+pionek(plansza[0][2]))
    print("---+---+---")
    print(" "+pionek(plansza[1][0])+
          " | "+pionek(plansza[1][1])+
          " | "+pionek(plansza[1][2]))
    print("---+---+---")
    print(" "+pionek(plansza[2][0])+
          " | "+pionek(plansza[2][1])+
          " | "+pionek(plansza[2][2]))

plansza=nowa_pusta_plansza()
koniec=False
kto=1
while(koniec==False):
    wyswietl(plansza)
    print(kom_ruch(kto))
    wiersz=int(input("Podaj wiersz:"))
    kolumna=int(input("Podaj kolumnę:"))
    wykonalny, plansza, kto=wykonaj_ruch(plansza, kto, wiersz, kolumna)
    while(wykonalny==False):
        print(kom_zly_ruch())
        wiersz=int(input("Podaj wiersz:"))
        kolumna=int(input("Podaj kolumnę:"))
        wykonalny, plansza, kto=wykonaj_ruch(plansza, kto, wiersz, kolumna)
    print()
    print(kom_ruch_przeciw(-kto, wiersz, kolumna))
    koniec, wygral=koniec_gry(plansza)
print()
wyswietl(plansza)
print(kom_koniec(wygral))
