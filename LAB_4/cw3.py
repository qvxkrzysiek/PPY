def szyfr_cezara(wiadomosc, przesuniecie):
    zaszyfrowana_wiadomosc = ''
    # przekształcamy wiadomość do postaci tylko z liter
    wiadomosc = wiadomosc.lower()
    for litera in wiadomosc:
        if litera.isalpha():
            # przesuwamy literę o wartość klucza w alfabecie
            przesunieta_litera = chr(ord(litera) + przesuniecie)
            zaszyfrowana_wiadomosc += przesunieta_litera.upper()
        else:
            # pozostawiamy znak niezmieniony
            zaszyfrowana_wiadomosc += litera
    return zaszyfrowana_wiadomosc

print(szyfr_cezara("tak",1))