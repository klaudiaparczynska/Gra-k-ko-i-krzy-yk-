from kik_plansza import*
from kik_kom import*
from kik_ai_int import*

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

print("Cz-człowiek, K-komputer")
kto_kolko=input("Kto gra o (Cz/K): ")
kto_krzyzyk=input("Kto gra x (Cz/K): ")
kto_zaczyna=input("Kto zaczyna pierwszą partie? (o/x): ")
ile_partii=int(input("Ile partii chcesz rozegrać? "))
while ile_partii<=0:
    ile_partii=int(input("Podano błędne dane. Ile partii chcesz rozegrać? "))

if kto_zaczyna=="x":
    kto=1
else:
    kto=-1
    
wyniki=[]
for i in range (ile_partii):
    plansza=nowa_pusta_plansza()
    koniec=False
    while(koniec==False):
        print("Partia "+str(i+1))
        wyswietl(plansza)
        print(kom_ruch(kto))
        if kto_kolko=="K" and kto==-1:
            wiersz, kolumna=wybierz_ruch_int(plansza, -1)
        elif kto_krzyzyk=="K" and kto==1:
            wiersz, kolumna=wybierz_ruch_int(plansza, 1)
        else:
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
    wyniki.append(wygral)
    kto=0-kto
    print()
    wyswietl(plansza)
    print(kom_koniec(wygral))
print("x wygrał następującą ilość tur:  "+str(wyniki.count(1))+ " razy")
print("Gra zakończyła się remisem "+str(wyniki.count(0)) + " razy")
print("o wygrało następującą ilość tur: "+str(wyniki.count(-1)))
            
                
          
                
