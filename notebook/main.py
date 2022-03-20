import notebook as nb


class Menu:

    def __init__(self):
        self.notebook = nb.Notebook()
        self.options = {"1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit}

    def show_menu(self):
        print("Wybierz opcje notatnika ktora chcesz uzyc:")
        for option_id, option in self.options:
            print(f"{option_id}: {option}")

    def run(self):
        for number, option in self.options.items():
            print(f" {number}. {option.__name__}")
        user_id = input("Wybierz polecenie ktore chcesz wykonac: ")
        if user_id not in self.options.keys():
            print("Podales bledna opcje, sprobuj jeszcze raz.")
        else:
            to_quit = self.options[user_id]()
        return to_quit

    def show_notes(self, searched=""):
        if not searched:
            print("Wszystkie notatki w notatniku:")
            for anote in self.notebook.notes:
                print(anote)
        else:
            print(f"Notatki w ktorych zawarte jest '{searched}':")
            search_result = self.notebook.search(searched)
            for anote in search_result:
                print(anote)
        print()

    def search_notes(self):
        user_input = input("Podaj wyszukiwany tag lub tekst.\n")
        self.show_notes(user_input)

    def add_note(self):
        note_text = input("Podaj tekst notatki.\n")
        note_tag = input("Podaj tag notatki.\n")
        self.notebook.new_note(note_text, note_tag)

    def modify_note(self):
        for anote in self.notebook.notes:
            print(anote)
        note_choice = int(input("Podaj numer notatki ktora chcesz zmodyfikowac.\n"))
        if not -1 < note_choice <= len(self.notebook.notes)-1:
            print("Nie ma takiej notatki.\n")
        else:
            option_choice = int(input("Chcesz zmodyfikowac:\n1. Tresc\n2. Tag\n"))
            if option_choice == 1:
                modified_text = input("Podaj nowa tresc notatki.\n")
                self.notebook.modify_text(note_choice, modified_text)
            elif option_choice == 2:
                modified_tag = input("Podaj nowy tag/tagi notatki.\n")
                self.notebook.modify_tag(note_choice, modified_tag)
            else:
                print("Wybrales niepoprawna opcje.")

    def quit(self):
        print("Zakonczono dzialanie notatnika.")
        return True


if __name__ == '__main__':
    is_on = True
    menu = Menu()
    while is_on:
        is_on = not menu.run()
