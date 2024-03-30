-- Создание базы данных
CREATE DATABASE BreadFactoryDB;
USE BreadFactoryDB;


-- Создание таблицы для изделий (Products)
CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    Weight DECIMAL(10, 2) NOT NULL,
    EnergyValue INT,
    ProductionVolume INT,
    ProductionDate DATE,
    ExpiryDate DATE,
    Description NVARCHAR(MAX),
    Composition NVARCHAR(MAX),
    UnitPrice DECIMAL(10, 2) NOT NULL
);

INSERT INTO Products VALUES
    (1, 'Хлеб ржаной', 500, 200, 100, '2024-01-01', '2024-02-01', 'Очень вкусный ржаной хлеб', 'Мука, вода, соль', 2.50),
    (2, 'Булка пшеничная', 150, 100, 50, '2024-01-05', '2024-02-05', 'Легкая булка для завтрака', 'Мука, вода, дрожжи', 1.20),
    (3, 'Багет', 300, 150, 80, '2024-02-10', '2024-03-10', 'Тонкий хрустящий багет', 'Мука, вода, соль, дрожжи', 3.00),
    (4, 'Крендель', 200, 120, 60, '2024-02-15', '2024-03-15', 'Кружевной крендель с маком', 'Мука, вода, соль, мак', 2.80),
    (5, 'Сдобный булочка', 180, 120, 70, '2024-02-20', '2024-03-20', 'Нежная сдобная булочка', 'Мука, вода, масло, дрожжи', 2.00),
    (6, 'Пирожное "Эклер"', 100, 250, 30, '2024-03-01', '2024-03-10', 'Классическое французское пирожное', 'Мука, вода, масло, яйца, ваниль', 4.50),
    (7, 'Паунд-кейк', 600, 350, 120, '2024-03-05', '2024-04-05', 'Классический кекс', 'Мука, вода, масло, сахар, яйца', 6.00),
    (8, 'Батон', 250, 130, 90, '2024-03-10', '2024-04-10', 'Длинный и тонкий хлеб', 'Мука, вода, соль, дрожжи', 2.20),
    (9, 'Сдобный пирог', 700, 300, 150, '2024-03-15', '2024-04-15', 'Пирог с начинкой из яблок', 'Мука, вода, масло, сахар, яйца, яблоки', 5.50),
    (10, 'Булочка с корицей', 120, 180, 40, '2024-03-20', '2024-04-20', 'Ароматная булочка с корицей', 'Мука, вода, масло, сахар, корица', 2.80);


-- Создание таблицы для ингредиентов (Ingredients)
CREATE TABLE Ingredients (
    IngredientID INT PRIMARY KEY,
    Name NVARCHAR(255) NOT NULL,
    Quantity INT,
    SupplyDate DATE,
    ExpiryDate DATE,
    EnergyValue INT,
    UnitPrice DECIMAL(10, 2) NOT NULL
);

-- Добавление записей в таблицу Ingredients
INSERT INTO Ingredients VALUES
    (1, 'Мука пшеничная', 500, '2024-01-01', '2025-01-01', 100, 1.00),
    (2, 'Вода', 300, '2024-01-02', '2025-01-02', 0, 0.50),
    (3, 'Соль', 50, '2024-01-03', '2025-01-03', 0, 0.30),
    (4, 'Дрожжи', 30, '2024-01-04', '2025-01-04', 20, 0.80),
    (5, 'Масло', 100, '2024-01-05', '2025-01-05', 120, 1.50),
    (6, 'Мак', 10, '2024-01-06', '2025-01-06', 60, 2.00),
    (7, 'Яйца', 50, '2024-01-07', '2025-01-07', 80, 0.70),
    (8, 'Ваниль', 5, '2024-01-08', '2025-01-08', 30, 2.50),
    (9, 'Сахар', 80, '2024-01-09', '2025-01-09', 0, 0.40),
    (10, 'Корица', 15, '2024-01-10', '2025-01-10', 0, 1.00);


-- Создание таблицы для продаж (Sales)
CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    ProductID INT FOREIGN KEY REFERENCES Products(ProductID),
    SaleDate DATE,
    QuantitySold INT,
    TotalAmount DECIMAL(10, 2)
);

-- Добавление записей в таблицу Sales
INSERT INTO Sales VALUES
    (1, 1, '2024-02-01', 10, 25.00),
    (2, 2, '2024-02-02', 5, 6.00),
    (3, 3, '2024-02-03', 8, 24.00),
    (4, 4, '2024-02-04', 6, 16.80),
    (5, 5, '2024-02-05', 7, 14.00),
    (6, 6, '2024-02-06', 4, 18.00),
    (7, 7, '2024-02-07', 12, 72.00),
    (8, 8, '2024-02-08', 9, 19.80),
    (9, 9, '2024-02-09', 15, 82.50),
    (10, 10, '2024-02-10', 3, 8.40);


-- Запросы

--1
SELECT 
    P.Name AS ProductName,
    P.Weight - COALESCE(SUM(S.QuantitySold), 0) AS RemainingStock
FROM Products P
LEFT JOIN Sales S ON P.ProductID = S.ProductID
GROUP BY P.ProductID, P.Name, P.Weight;

--2
SELECT 
    P.Name AS ProductName,
    SUM(I.UnitPrice * P.CompositionQuantity) AS TotalCost
FROM Products P
JOIN (
    SELECT 
        P.ProductID,
        I.UnitPrice,
        I.Quantity AS CompositionQuantity
    FROM Ingredients I
    JOIN Products P ON I.Name = P.Composition
) AS I ON P.ProductID = I.ProductID
GROUP BY P.ProductID, P.Name;


--3
SELECT 
    P.Name AS ProductName,
    SUM(I.EnergyValue * P.CompositionQuantity) AS TotalEnergyValue
FROM Products P
JOIN (
    SELECT 
        P.ProductID,
        I.EnergyValue,
        I.Quantity AS CompositionQuantity
    FROM Ingredients I
    JOIN Products P ON I.Name = P.Composition
) AS I ON P.ProductID = I.ProductID
GROUP BY P.ProductID, P.Name;

--4
SELECT 
    P.Name AS ProductName,
    SUM(S.TotalAmount) AS TotalProfit
FROM Products P
JOIN Sales S ON P.ProductID = S.ProductID
GROUP BY P.ProductID, P.Name;

--5
SELECT 
    AVG(P.UnitPrice) AS AverageUnitPrice
FROM Products P;

--6
SELECT 
    P.Name AS BestSellingProduct,
    SUM(S.QuantitySold) AS TotalQuantitySold
FROM Products P
JOIN Sales S ON P.ProductID = S.ProductID
GROUP BY P.ProductID, P.Name
ORDER BY TotalQuantitySold DESC
LIMIT 1;

--7
SELECT 
    P.Name AS ProductName,
    P.ExpiryDate
FROM Products P
WHERE DATEDIFF(MONTH, GETDATE(), P.ExpiryDate) <= 1;

--8
SELECT 
    P.Name AS ProductName,
    COALESCE(SUM(S.QuantitySold), 0) AS TotalQuantitySold
FROM Products P
LEFT JOIN Sales S ON P.ProductID = S.ProductID
GROUP BY P.ProductID, P.Name
ORDER BY TotalQuantitySold DESC;

--9
SELECT 
    AVG(EnergyValue) AS AverageEnergyValue
FROM (
    SELECT 
        I.EnergyValue,
        P.CompositionQuantity
    FROM Ingredients I
    JOIN Products P ON I.Name = P.Composition
) AS ProductComposition;

--10
SELECT 
    Name AS ProductName,
    UnitPrice
FROM Products
ORDER BY UnitPrice DESC
LIMIT 5;
