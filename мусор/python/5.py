import json


class Person:
    def __init__(self, last_name, first_name, patronymic, gender, passport, address):
        self.last_name = last_name
        self.first_name = first_name
        self.patronymic = patronymic
        self.gender = gender
        self.passport = passport
        self.address = address


class Student(Person):
    def __init__(self, last_name, first_name, patronymic, gender, passport, address, parents, group):
        super().__init__(last_name, first_name, patronymic, gender, passport, address)
        self.parents = parents
        self.group = group


class Teacher(Person):
    def __init__(self, last_name, first_name, patronymic, gender, passport, address, department, position):
        super().__init__(last_name, first_name, patronymic, gender, passport, address)
        self.department = department
        self.position = position

    def to_dict(self):
        return {
            "last_name": self.last_name,
            "first_name": self.first_name,
            "patronymic": self.patronymic,
            "gender": self.gender,
            "passport": self.passport,
            "address": self.address,
            "department": self.department,
            "position": self.position
        }


class Department:
    def __init__(self, name, head_teacher):
        self.name = name
        self.head_teacher = head_teacher


class Faculty:
    def __init__(self, name, departments):
        self.name = name
        self.departments = departments


class Group:
    def __init__(self, number, speciality, head_student, department):
        self.number = number
        self.speciality = speciality
        self.head_student = head_student
        self.department = department


class University:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.departments = []
        self.faculties = []
        self.groups = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_department(self, department):
        self.departments.append(department)

    def add_faculty(self, faculty):
        self.faculties.append(faculty)

    def add_group(self, group):
        self.groups.append(group)

    def save_to_file(self, filename):
        data = {
            "students": [s.__dict__ for s in self.students],
            "teachers": [t.to_dict() for t in self.teachers],
            "departments": [d.__dict__ for d in self.departments],
            "faculties": [f.__dict__ for f in self.faculties],
            "groups": [g.__dict__ for g in self.groups]
        }
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_file(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            self.students = [Student(**s) for s in data["students"]]
            self.teachers = [Teacher(**t) for t in data["teachers"]]
            self.departments = [Department(**d) for d in data["departments"]]
            self.faculties = [Faculty(**f) for f in data["faculties"]]
            self.groups = [Group(**g) for g in data["groups"]]

    def get_all_students(self):
        return sorted(self.students, key=lambda s: s.last_name)

    def get_students_without_parents(self):
        return [s for s in self.students if not s.parents]

    def get_all_teachers(self):
        return sorted(self.teachers, key=lambda t: t.last_name)

    def get_department_heads(self):
        return [d.head_teacher for d in self.departments]

    def get_groups_without_head(self):
        return [g for g in self.groups if not g.head_student]

    def find_children_of_parent(self, parent_last_name):
        return [s for s in self.students if parent_last_name in [p.last_name for p in s.parents]]

    def get_teachers_with_children(self):
        return [t for t in self.teachers if any([parent.last_name == t.last_name for parent in t.parents])]


def main():
    university = University()

    # Добавляем студентов
    student1 = Student("Ivanov", "Ivan", "Ivanovich", "Male", "1234 567890", "Moscow", [], None)
    student2 = Student("Petrova", "Maria", "Sergeevna", "Female", "5678 123456", "Saint Petersburg", [], None)
    university.add_student(student1)
    university.add_student(student2)

    # Добавляем преподавателей
    teacher1 = Teacher("Sidorov", "Petr", "Vasilievich", "Male", "9876 543210", "Kazan", "Mathematics", "Professor")
    teacher2 = Teacher("Smirnova", "Olga", "Ivanovna", "Female", "5432 109876", "Novosibirsk", "Physics", "Associate Professor")
    university.add_teacher(teacher1)
    university.add_teacher(teacher2)

    # Добавляем кафедры
    department1 = Department("Mathematics", teacher1)
    department2 = Department("Physics", teacher2)
    university.add_department(department1)
    university.add_department(department2)

    # Добавляем факультеты
    faculty1 = Faculty("Engineering", [department1])
    faculty2 = Faculty("Science", [department2])
    university.add_faculty(faculty1)
    university.add_faculty(faculty2)

    # Добавляем группы
    group1 = Group("A-101", "Engineering", student1, department1)
    group2 = Group("B-202", "Science", student2, department2)
    university.add_group(group1)
    university.add_group(group2)

    # Сохраняем данные в файл
    university.save_to_file("university_data.json")

    # Загружаем данные из файла
    university.load_from_file("university_data.json")

    # Получаем список всех студентов и сортируем их по фамилии
    all_students = university.get_all_students()
    print("All Students:")
    for student in all_students:
        print(f"{student.last_name} {student.first_name} {student.patronymic}")

    print()

    # Получаем список студентов без родителей
    students_without_parents = university.get_students_without_parents()
    print("Students Without Parents:")
    for student in students_without_parents:
        print(f"{student.last_name} {student.first_name} {student.patronymic}")

    print()

    # Получаем список всех преподавателей и сортируем их по фамилии
    all_teachers = university.get_all_teachers()
    print("All Teachers:")
    for teacher in all_teachers:
        print(f"{teacher.last_name} {teacher.first_name} {teacher.patronymic}")

    print()

    # Получаем список заведующих кафедрами
    department_heads = university.get_department_heads()
    print("Department Heads:")
    for head in department_heads:
        print(f"{head.last_name} {head.first_name} {head.patronymic}")

    print()

    # Получаем список групп без старост и кафедр без заведующих
    groups_without_heads = university.get_groups_without_head()
    print("Groups Without Heads:")
    for group in groups_without_heads:
        print(f"Group: {group.number}, Department: {group.department.name}")

    print()

    # Поиск детей-студентов у заданного родителя
    parent_last_name = "Ivanov"
    children_of_parent = university.find_children_of_parent(parent_last_name)
    print(f"Children of Parent '{parent_last_name}':")
    for child in children_of_parent:
        print(f"{child.last_name} {child.first_name} {child.patronymic}")

    print()

    # Получаем список преподавателей, у которых есть дети-студенты
    teachers_with_children = university.get_teachers_with_children()
    print("Teachers with Children Students:")
    for teacher in teachers_with_children:
        print(f"{teacher.last_name} {teacher.first_name} {teacher.patronymic}")


if __name__ == "__main__":
    main()
