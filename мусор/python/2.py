class Subject:
    def __init__(self):
        self.hours = 0
        self.labor_intensity = 0

    def init(self, hours, labor_intensity):
        self.hours = hours
        self.labor_intensity = labor_intensity

    def display(self):
        print(f"Часов в неделю: {self.hours}, трудоемкость: {self.labor_intensity}")

    def weight(self):
        return self.hours / 8 * self.labor_intensity / 10

class Student:
    def __init__(self):
        self.subject1 = Subject()
        self.subject2 = Subject()
        self.subject3 = Subject()
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0

    def init_subjects(self, subject1_hours, subject1_labor, subject2_hours, subject2_labor, subject3_hours, subject3_labor):
        self.subject1.init(subject1_hours, subject1_labor)
        self.subject2.init(subject2_hours, subject2_labor)
        self.subject3.init(subject3_hours, subject3_labor)

    def init_scores(self, score1, score2, score3):
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3

    def average_rating(self):
        return (self.score1 * self.subject1.weight() + self.score2 * self.subject2.weight() + self.score3 * self.subject3.weight()) / 3

    def max_weight_subject(self):
        subjects = [self.subject1, self.subject2, self.subject3]
        max_weight_subject = subjects[0]
        for subject in subjects:
            if subject.weight() > max_weight_subject.weight():
                max_weight_subject = subject
        return max_weight_subject

# Создание объекта ученика
student = Student()

# Инициализация предметов
student.init_subjects(4, 8, 3, 6, 2, 10)

# Инициализация баллов
student.init_scores(85, 90, 95)

# Вывод информации о предметах
print("Информация о предметах:")
student.subject1.display()
student.subject2.display()
student.subject3.display()

# Вывод среднего рейтинга ученика
print(f"\nСредний рейтинг ученика: {student.average_rating()}")

# Вывод предмета с максимальным весом в рейтинге
print("\nПредмет с максимальным весом в рейтинге:")
student.max_weight_subject().display()
