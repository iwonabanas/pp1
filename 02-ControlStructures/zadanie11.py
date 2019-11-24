# zad.11. System komputerowy zawiera konto użytkownika o identyfikatorze (login) „marek” i haśle „m-123”.
# Napisz program, który sprawdzi, czy wprowadzony login i hasło są zgodne z danymi konta użytkownika.

login = "marek"
password = "m-123"

user_login = input("Podaj login: ")
user_pass = input("Podaj hasło: ")

if user_login == login and user_pass == password:
    print ("Zalogowano pomyślnie.")
else:
    print("Niepoprawne dane.")