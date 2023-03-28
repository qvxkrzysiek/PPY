import math

def ilosc_opakowan(dlugosc_podlogi, szerokosc_podlogi, dlugosc_panela, szerokosc_panela, ilosc_paneli_w_opakowaniu):
    # obliczamy powierzchnię pomieszczenia
    powierzchnia = (dlugosc_podlogi * szerokosc_podlogi) * 1.1
    
    # obliczamy powierzchnię panela
    powierzchnia_panela = dlugosc_panela * szerokosc_panela
    
    # obliczamy ilość potrzebnych paneli
    ilosc_paneli = math.ceil(powierzchnia / powierzchnia_panela)
    
    # obliczamy ilość potrzebnych opakowań
    ilosc_opakowan = math.ceil(ilosc_paneli / ilosc_paneli_w_opakowaniu)
    
    return ilosc_opakowan

print(ilosc_opakowan(5, 6, 1, 0.5, 10))
