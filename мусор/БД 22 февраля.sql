-- Создание базы данных
CREATE DATABASE MySampleDatabase;
GO

-- Использование созданной базы данных
USE MySampleDatabase;
GO

-- Создание таблицы Users
CREATE TABLE Users (
    UserID INT PRIMARY KEY,
    UserName NVARCHAR(50),
    Age INT,
    Email VARCHAR(100),
    RegistrationDate DATE
);

-- Вставка записей в таблицу Users
INSERT INTO Users (UserID, UserName, Age, Email, RegistrationDate)
VALUES
    (1, 'JohnDoe', 25, 'johndoe@example.com', '2023-01-15'),
    (2, 'JaneSmith', 30, 'janesmith@example.com', '2022-11-20'),
    (3, 'MikeJohnson', 22, 'mikejohnson@example.com', '2024-02-10');

-- Создание таблицы Products
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName NVARCHAR(100),
    Price DECIMAL(10, 2),
    Description TEXT
);

-- Вставка записей в таблицу Products
INSERT INTO Products (ProductID, ProductName, Price, Description)
VALUES
    (1, 'Laptop', 1200.00, '15-inch laptop with SSD'),
    (2, 'Smartphone', 800.50, '6.5-inch smartphone with dual camera'),
    (3, 'Headphones', 99.99, 'Wireless noise-cancelling headphones');

-- Создание таблицы Orders
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    UserID INT,
    OrderDate DATETIME,
    TotalAmount MONEY,
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Вставка записей в таблицу Orders
INSERT INTO Orders (OrderID, UserID, OrderDate, TotalAmount)
VALUES
    (1, 1, '2023-02-01 10:30:00', 1200.00),
    (2, 2, '2022-12-20 15:45:00', 899.49),
    (3, 3, '2024-01-05 09:00:00', 287.98);

-- Создание таблицы OrderDetails
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    UnitPrice DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Вставка записей в таблицу OrderDetails
INSERT INTO OrderDetails (OrderDetailID, OrderID, ProductID, Quantity, UnitPrice)
VALUES
    (1, 1, 1, 1, 1200.00),
    (2, 2, 2, 1, 800.50),
    (3, 2, 3, 2, 199.98);

-- Создание таблицы Addresses
CREATE TABLE Addresses (
    AddressID INT PRIMARY KEY,
    UserID INT,
    StreetAddress NVARCHAR(100),
    City NVARCHAR(50),
    State NVARCHAR(50),
    ZipCode VARCHAR(10),
    FOREIGN KEY (UserID) REFERENCES Users(UserID)
);

-- Вставка записей в таблицу Addresses
INSERT INTO Addresses (AddressID, UserID, StreetAddress, City, State, ZipCode)
VALUES
    (1, 1, '123 Main St', 'Anytown', 'NY', '10001'),
    (2, 2, '456 Oak Ave', 'Smallville', 'CA', '90210'),
    (3, 3, '789 Pine Rd', 'Metro City', 'TX', '77002');

-- Создание таблицы Reviews
CREATE TABLE Reviews (
    ReviewID INT PRIMARY KEY,
    UserID INT,
    ProductID INT,
    Rating TINYINT,
    ReviewText NVARCHAR(MAX),
    ReviewDate DATETIME,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Вставка записей в таблицу Reviews
INSERT INTO Reviews (ReviewID, UserID, ProductID, Rating, ReviewText, ReviewDate)
VALUES
    (1, 1, 1, 5, 'Great laptop, fast delivery!', '2023-02-05 14:20:00'),
    (2, 2, 3, 4, 'Good sound quality but a bit uncomfortable after long use.', '2022-12-25 09:30:00'),
    (3, 3, 2, 5, 'Best smartphone I ever had!', '2024-01-15 20:10:00');

-- Создание таблицы UserOrders (один к одному)
CREATE TABLE UserOrders (
    UserID INT PRIMARY KEY,
    LastOrderID INT,
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (LastOrderID) REFERENCES Orders(OrderID)
);

-- Вставка записей в таблицу UserOrders
INSERT INTO UserOrders (UserID, LastOrderID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);

-- Создание таблицы ProductReviews (многие ко многим)
CREATE TABLE ProductReviews (
    ReviewID INT,
    ProductID INT,
    PRIMARY KEY (ReviewID, ProductID),
    FOREIGN KEY (ReviewID) REFERENCES Reviews(ReviewID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

-- Вставка записей в таблицу ProductReviews
INSERT INTO ProductReviews (ReviewID, ProductID)
VALUES
    (1, 1),
    (2, 3),
    (3, 2);

-- Создание таблицы UserAddresses (многие ко многим)
CREATE TABLE UserAddresses (
    UserID INT,
    AddressID INT,
    PRIMARY KEY (UserID, AddressID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (AddressID) REFERENCES Addresses(AddressID)
);

-- Вставка записей в таблицу UserAddresses
INSERT INTO UserAddresses (UserID, AddressID)
VALUES
    (1, 1),
    (2, 2),
    (3, 3);
