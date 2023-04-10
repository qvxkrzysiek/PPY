liczby = input("Podaj liczby rozdzielone przecinkiem: ")
lista_liczb = liczby.split(",")  # dzieli łańcuch na listę elementów
max_liczba = int(lista_liczb[0])  # przyjmuje pierwszą liczbę jako maksimum
min_liczba = int(lista_liczb[0])  # przyjmuje pierwszą liczbę jako minimum

# porównuje każdą liczbę z maksimum i minimum
for i in range(1, len(lista_liczb)):
    if int(lista_liczb[i]) > max_liczba:
        max_liczba = int(lista_liczb[i])
    if int(lista_liczb[i]) < min_liczba:
        min_liczba = int(lista_liczb[i])

print("Największa liczba to:", max_liczba)
print("Najmniejsza liczba to:", min_liczba)
