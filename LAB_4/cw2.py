def czy_pierwsza(*liczby):
    pierwsze = []
    for n in liczby:
        if n in (0, 1):
            pierwsze.append(False)
        elif n == 2:
            pierwsze.append(True)
        elif n % 2 == 0:
            pierwsze.append(False)
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    pierwsze.append(False)
                    break
            else:
                pierwsze.append(True)
    return pierwsze

print(czy_pierwsza(2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 30))