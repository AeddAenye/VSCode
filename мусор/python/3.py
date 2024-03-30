import random

# Абстрактный класс Sorting
class Sorting:
    def __init__(self, sequence_id):
        self.sequence_id = sequence_id

    def sort(self):
        pass

    def get_sum(self):
        pass

    def display(self):
        pass

    def sort_by_criteria(self, criteria):
        pass

    def write_to_file(self, filename):
        pass

    @classmethod
    def read_from_file(cls, filename):
        pass

# Класс Choice, наследующий Sorting
class Choice(Sorting):
    def __init__(self, sequence_id, data):
        super().__init__(sequence_id)
        self.data = data

    def sort(self):
        self.data.sort()

    def get_sum(self):
        return sum(self.data)

    def display(self):
        print(f"Choice ID: {self.sequence_id}")
        print("Data:", self.data)
        print("Sum:", self.get_sum())

    def sort_by_criteria(self, criteria):
        if criteria == 'ascending':
            self.data.sort()
        elif criteria == 'descending':
            self.data.sort(reverse=True)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Choice ID: {self.sequence_id}\n")
            f.write("Data: " + ' '.join(map(str, self.data)) + "\n")
            f.write(f"Sum: {self.get_sum()}\n")

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            sequence_id = int(lines[0].split(": ")[1])
            data = list(map(int, lines[1].split(": ")[1].split()))
            return cls(sequence_id, data)

# Класс Quick, наследующий Sorting
class Quick(Sorting):
    def __init__(self, sequence_id, data):
        super().__init__(sequence_id)
        self.data = data

    def sort(self):
        self._quick_sort(self.data, 0, len(self.data) - 1)

    def _quick_sort(self, arr, low, high):
        if low < high:
            pi = self._partition(arr, low, high)
            self._quick_sort(arr, low, pi - 1)
            self._quick_sort(arr, pi + 1, high)

    def _partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def get_sum(self):
        return sum(self.data)

    def display(self):
        print(f"Quick ID: {self.sequence_id}")
        print("Data:", self.data)
        print("Sum:", self.get_sum())

    def sort_by_criteria(self, criteria):
        if criteria == 'ascending':
            self.sort()
        elif criteria == 'descending':
            self.data.sort(reverse=True)

    def write_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Quick ID: {self.sequence_id}\n")
            f.write("Data: " + ' '.join(map(str, self.data)) + "\n")
            f.write(f"Sum: {self.get_sum()}\n")

    @classmethod
    def read_from_file(cls, filename):
        with open(filename, 'r') as f:
            lines = f.readlines()
            sequence_id = int(lines[0].split(": ")[1])
            data = list(map(int, lines[1].split(": ")[1].split()))
            return cls(sequence_id, data)

# Класс Series
# Класс Series
class Series:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def display_all(self):
        for obj in self.objects:
            obj.display()

    def total_sum(self):
        total = 0
        for obj in self.objects:
            total += obj.get_sum()
        return total

    def sort_all_by_criteria(self, criteria):
        for obj in self.objects:
            obj.sort_by_criteria(criteria)

    def write_all_to_file(self, filename):
        with open(filename, 'w') as f:
            for obj in self.objects:
                obj.write_to_file(filename)  # Fix here

    @classmethod
    def read_all_from_file(cls, filename):
        series = cls()
        with open(filename, 'r') as f:
            lines = f.readlines()
            i = 0
            while i < len(lines):
                if "Choice ID" in lines[i]:
                    sequence_id = int(lines[i].split(": ")[1])
                    data = list(map(int, lines[i + 1].split(": ")[1].split()))
                    series.add_object(Choice(sequence_id, data))
                elif "Quick ID" in lines[i]:
                    sequence_id = int(lines[i].split(": ")[1])
                    data = list(map(int, lines[i + 1].split(": ")[1].split()))
                    series.add_object(Quick(sequence_id, data))
                i += 3
        return series


# Демонстрационная программа
def main():
    series = Series()

    # Создаем объекты Choice и Quick
    choice_data = random.sample(range(1, 100), 5)
    choice = Choice(1, choice_data)
    quick_data = random.sample(range(1, 100), 5)
    quick = Quick(2, quick_data)

    # Добавляем объекты в Series
    series.add_object(choice)
    series.add_object(quick)

    print("Initial Series:")
    series.display_all()
    print("Total Sum of All Objects:", series.total_sum())

    # Сортируем все объекты по убыванию
    series.sort_all_by_criteria('descending')

    print("\nSeries After Sorting:")
    series.display_all()
    print("Total Sum of All Objects:", series.total_sum())

    # Записываем все объекты в файл
    series.write_all_to_file("sorted_objects.txt")

    # Читаем объекты из файла
    new_series = Series.read_all_from_file("sorted_objects.txt")

    print("\nObjects Read From File:")
    new_series.display_all()
    print("Total Sum of All Objects:", new_series.total_sum())

if __name__ == "__main__":
    main()
