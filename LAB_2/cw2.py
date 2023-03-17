num1 = float(input("Podaj pierwszą liczbę: "))
num2 = float(input("Podaj drugą liczbę: "))

operator = input("Wybierz operator (+, -, *, /): ")

if operator == '+':
    wynik = num1 + num2
elif operator == '-':
    wynik = num1 - num2
elif operator == '*':
    wynik = num1 * num2
elif operator == '/':
    wynik = num1 / num2
else:
    print("Nieprawidłowy operator. Wybierz +, -, *, lub /")
    exit()

print(f"Wynik: {num1} {operator} {num2} = {wynik}")