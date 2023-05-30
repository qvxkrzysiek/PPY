import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Funkcja tworząca tabelę w bazie danych
def create_table():
    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS students
                     (email TEXT, first_name TEXT, last_name TEXT, points INTEGER)''')
        conn.commit()
        conn.close()
    except sqlite3.Error as error:
        messagebox.showerror("Błąd bazy danych", str(error))

# Funkcja dodająca studenta do bazy danych
def add_student():
    email = email_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    points = points_entry.get()

    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                  (email, first_name, last_name, points))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Student został dodany do bazy danych.")
        clear_entries()
    except sqlite3.Error as error:
        messagebox.showerror("Błąd bazy danych", str(error))

# Funkcja wyświetlająca dane studentów
def show_students():
    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("SELECT * FROM students")
        rows = c.fetchall()
        conn.close()

        # Wyświetlanie danych w messagebox
        if rows:
            students_info = "Dane studentów:\n"
            for row in rows:
                students_info += f"Email: {row[0]}, Imię: {row[1]}, Nazwisko: {row[2]}, Punkty: {row[3]}\n"
            messagebox.showinfo("Dane studentów", students_info)
        else:
            messagebox.showinfo("Brak danych", "Brak zapisanych danych studentów.")
    except sqlite3.Error as error:
        messagebox.showerror("Błąd bazy danych", str(error))

# Funkcja usuwająca dane studenta na podstawie podanego emaila
def delete_student():
    email = email_entry.get()

    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("DELETE FROM students WHERE email=?", (email,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Dane studenta zostały usunięte z bazy danych.")
        clear_entries()
    except sqlite3.Error as error:
        messagebox.showerror("Błąd bazy danych", str(error))

# Funkcja edytująca dane studenta na podstawie podanego emaila
def edit_student():
    email = email_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    points = points_entry.get()

    try:
        conn = sqlite3.connect('students.db')
        c = conn.cursor()
        c.execute("UPDATE students SET first_name=?, last_name=?, points=? WHERE email=?",
                  (first_name, last_name, points, email))
        conn.commit()
        conn.close()
        messagebox.showinfo("Sukces", "Dane studenta zostały zaktualizowane.")
        clear_entries()
    except sqlite3.Error as error:
        messagebox.showerror("Błąd bazy danych", str(error))

# Funkcja czyszcząca pola tekstowe
def clear_entries():
    email_entry.delete(0, END)
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    points_entry.delete(0, END)

# Tworzenie tabeli przy starcie aplikacji
create_table()

# Tworzenie głównego okna
window = Tk()
window.title("Aplikacja studenci")
window.geometry("400x300")


# Tworzenie etykiet i pól tekstowych
email_label = ttk.Label(window, text="Email:")
email_label.pack()
email_entry = ttk.Entry(window)
email_entry.pack()

first_name_label = ttk.Label(window, text="Imię:")
first_name_label.pack()
first_name_entry = ttk.Entry(window)
first_name_entry.pack()

last_name_label = ttk.Label(window, text="Nazwisko:")
last_name_label.pack()
last_name_entry = ttk.Entry(window)
last_name_entry.pack()

points_label = ttk.Label(window, text="Punkty:")
points_label.pack()
points_entry = ttk.Entry(window)
points_entry.pack()


# Tworzenie przycisków
add_button = Button(window, text="Dodaj", command=add_student)
add_button.pack()

show_button = Button(window, text="Wyświetl", command=show_students)
show_button.pack()

delete_button = Button(window, text="Usuń", command=delete_student)
delete_button.pack()

edit_button = Button(window, text="Edytuj", command=edit_student)
edit_button.pack()

clear_button = Button(window, text="Wyczyść", command=clear_entries)
clear_button.pack()

window.mainloop()
