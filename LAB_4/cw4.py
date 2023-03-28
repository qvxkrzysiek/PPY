def szyfr_cezara(wiadomosc, klucz, alfabet='abcdefghijklmnopqrstuvwxyz'):
    zaszyfrowana_wiadomosc = ''
    dlugosc_alfabetu = len(alfabet)
    for litera in wiadomosc:
        if litera.isalpha():
            litera = litera.lower()
            indeks_litera = alfabet.index(litera)
            # przesuwamy indeks litery o wartość klucza w alfabecie
            przesuniety_indeks = (indeks_litera + klucz) % dlugosc_alfabetu
            # pobieramy przesuniętą literę z alfabetu
            przesunieta_litera = alfabet[przesuniety_indeks]
            if litera.isupper():
                przesunieta_litera = przesunieta_litera.upper()
            zaszyfrowana_wiadomosc += przesunieta_litera
        else:
            # pozostawiamy znak niezmieniony
            zaszyfrowana_wiadomosc += litera
    return zaszyfrowana_wiadomosc

print(szyfr_cezara("takz", 1, alfabet='abcdefghijklmnopqrstuvwxyzo'))