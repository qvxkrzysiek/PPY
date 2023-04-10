students_data = {}

def grade_students():
    for student in students_data.values():
        if student['status'] not in ('GRADED', 'MAILED'):
            points = student['points']
            if points >= 91:
               grade = 5
            elif points >= 81:
                grade = 4.5
            elif points >= 71:
                grade = 4
            elif points >= 61:
                grade = 3.5
            elif points >= 51:
                grade = 3
            else:
                grade = 2

            student['grade'] = grade
            student['status'] = 'GRADED'

            students_data[email] = student

def save_file():
    with open('students.txt', 'w') as f:
        for email, student in students_data.items():
            data = ','.join([
                student['email'],
                student['name'],
                student['surname'],
                str(student['points']),
                str(student['grade']),
                student['status']
            ])
            f.write(data + '\n')

with open('students.txt', 'r') as f:
    for line in f:
        data = line.strip().split(',')
        print(data)
        email, name, surname, points = data[:4]
        grade, status = data[4:] if len(data) > 4 else ('', '')

        student = {
            'email': email,
            'name': name,
            'surname': surname,
            'points': int(points),
            'grade': grade,
            'status': status
        }

        students_data[email] = student

grade_students()

while True:
    print("Co chcesz zrobić?")
    print("1. Dodaj studenta")
    print("2. Usuń studenta")
    print("3. Wyświetl studentów")
    print("4. Wyjdź z programu")
    
    choice = input("Wybierz opcję (1/2/3/4): ")
    
    if choice == '1':
        email = input("Podaj adres e-mail studenta: ")
        if email in students_data:
            print("Podany adres e-mail jest już zajęty.")
        else:
            name = input("Podaj imię studenta: ")
            surname = input("Podaj nazwisko studenta: ")
            points = input("Podaj liczbę punktów studenta: ")
            grade = ''
            status = ''
            
            student = {
                'email': email,
                'name': name,
                'surname': surname,
                'points': int(points),
                'grade': grade,
                'status': status
            }
            
            students_data[email] = student
            grade_students()
            save_file()
            print("Dodano studenta.")
    
    elif choice == '2':
        email = input("Podaj adres e-mail studenta do usunięcia: ")
        if email not in students_data:
            print("Nie znaleziono studenta o podanym adresie e-mail.")
        else:
            del students_data[email]
            save_file()
            print("Usunięto studenta.")
    
    elif choice == '3':
        for email, student in students_data.items():
            print(email, student['name'], student['surname'], student['points'], student['grade'], student['status'])
    
    elif choice == '4':
        break
    
    else:
        print("Nieprawidłowa opcja. Spróbuj ponownie.")