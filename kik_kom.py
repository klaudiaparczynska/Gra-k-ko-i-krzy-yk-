def pionek(wartosc):
    if(wartosc==1):
        return("x")
    elif(wartosc==-1):
        return("o")
    else:
        return(" ")
#która zwraca odpowiedni napis reprezentujący pionek dla użytkownika dla
#danej wartości z tablicy (czyli " " (spacja) dla 0, "x" dla -1 oraz "o" dla 1);


def kom_zly_ruch():
    return("Nieprawidłowy ruch! Musisz poprawić!")
#która zwraca (nie: wyświetla!) komunikat o złym ruchu;
def kom_koniec(kto):
    if(kto!=0):
        return("Wygrał gracz "+str(pionek(kto))+"!")
    else:
        return("Remis!")
#która zwraca (nie: wyświetla!) komunikat o zakończeniu gry remisem lub
##wygranajednej z osób (należy skorzystać z funkcji pionek);


def kom_ruch(kto):
    return("Ruch gracza "+str(pionek(kto)))
#która zwraca (nie: wyświetla!) prośbę o ruch skierowaną do odpowiedniego gracza
#(kto — znowu funkcja pionek);

def kom_ruch_przeciw(kto, wiersz, kolumna):
    return("Przeciwnik ("+str(pionek(kto))+") wykonuje ruch: "+str(wiersz)+", "+str(kolumna)+".")

    
#która zwraca (nie: wyświetla!) komunikat o ruchu przeciwnika;
##użyj funkcji pionek.
