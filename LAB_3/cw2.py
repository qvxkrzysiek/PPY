import random

miasta = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Katowice"]
odwiedzone_miasta = []  # pusta lista na odwiedzone miasta

while len(odwiedzone_miasta) < 10:  # dopóki nie odwiedzono 10 miast
    miasto = random.choice(miasta)  # wybierz losowe miasto
    if miasto not in odwiedzone_miasta:  # jeśli nie było jeszcze odwiedzone
        odwiedzone_miasta.append(miasto)  # dodaj do listy odwiedzonych miast

print("Plan wycieczki:")
for i, miasto in enumerate(odwiedzone_miasta):
    print(f"{i+1}. {miasto}")
