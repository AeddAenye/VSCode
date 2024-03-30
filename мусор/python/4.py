class Address:
    def __init__(self):
        self._index = None
        self._country = None
        self._city = None
        self._street = None
        self._house = None
        self._apartment = None

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, value):
        self._index = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def street(self):
        return self._street

    @street.setter
    def street(self, value):
        self._street = value

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, value):
        self._house = value

    @property
    def apartment(self):
        return self._apartment

    @apartment.setter
    def apartment(self, value):
        self._apartment = value


class Rectangle:
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area_calculator(self):
        return self.side1 * self.side2

    def perimeter_calculator(self):
        return 2 * (self.side1 + self.side2)

    @property
    def area(self):
        return self.area_calculator()

    @property
    def perimeter(self):
        return self.perimeter_calculator()


class Title:
    def __init__(self, title):
        self.title = title

    def show(self):
        return "Title: " + self.title


class Author:
    def __init__(self, author):
        self.author = author

    def show(self):
        return "Author: " + self.author


class Content:
    def __init__(self, content):
        self.content = content

    def show(self):
        return "Content: " + self.content


class Book:
    def __init__(self, title, author, content):
        self.title = Title(title)
        self.author = Author(author)
        self.content = Content(content)

    def show(self):
        return f"{self.title.show()}\n{self.author.show()}\n{self.content.show()}"


def main():
    # Task 1: Address
    print("Task 1: Address")
    address = Address()
    address.index = "123456"
    address.country = "Russia"
    address.city = "Moscow"
    address.street = "Lenin Street"
    address.house = "10"
    address.apartment = "25"
    print("Address Information:")
    print("Index:", address.index)
    print("Country:", address.country)
    print("City:", address.city)
    print("Street:", address.street)
    print("House:", address.house)
    print("Apartment:", address.apartment)
    print()

    # Task 2: Rectangle
    print("Task 2: Rectangle")
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    rectangle = Rectangle(side1, side2)
    print("Area of the rectangle:", rectangle.area)
    print("Perimeter of the rectangle:", rectangle.perimeter)
    print()

    # Task 3: Book
    print("Task 3: Book")
    book = Book("The Great Gatsby", "F. Scott Fitzgerald", "The story primarily concerns the young and mysterious millionaire Jay Gatsby and his quixotic passion and obsession with the beautiful former debutante Daisy Buchanan.")
    print("Book Information:")
    print(book.show())


if __name__ == "__main__":
    main()
