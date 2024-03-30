class Note:
    def __init__(self):
        self.full_name = ""
        self.phone_number = ""
        self.birthday = [0, 0, 0]

    def read(self):
        self.full_name = input("Введите имя и фамилию (через пробел): ")
        self.phone_number = input("Введите номер телефона: ")
        self.birthday = self.get_valid_birthday()

    def display(self):
        print(f"Имя и фамилия: {self.full_name}")
        print(f"Номер телефона: {self.phone_number}")
        print(f"Дата рождения: {self.birthday}")

    def find_birthday_by_month(self, month):
        return self.birthday[1] == month

    @staticmethod
    def get_valid_birthday():
        while True:
            birthday_input = input("Введите дату рождения (дд мм гггг): ")
            if len(birthday_input.split()) == 3:
                return list(map(int, birthday_input.split()))
            print("Некорректный ввод даты рождения. Пожалуйста, повторите ввод.")

def main():
    notes = [Note() for _ in range(2)]

    for note in notes:
        note.read()

    notes.sort(key=lambda note: note.full_name.split()[-1])  # Сортировка по фамилии

    month = int(input("Введите месяц: "))
    found = False
    print("\nЛюди, чьи дни рождения приходятся на этот месяц:")

    for note in notes:
        if note.find_birthday_by_month(month):
            note.display()
            print()
            found = True

    if not found:
        print("Нет людей, чьи дни рождения приходятся на этот месяц.")

if __name__ == "__main__":
    main()
