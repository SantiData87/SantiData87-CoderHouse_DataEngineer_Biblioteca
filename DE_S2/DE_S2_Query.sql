select * from agents
select * from calls
select * from customers

--a. Calcular las ventas totales y las llamadas totales realizadas a los clientes de la profesión de ingeniería
SELECT SUM(ProductSold) AS TotalSales, COUNT(*) AS NCalls
FROM customers Cu
join calls Ca ON Ca.CustomerID = Cu.CustomerID
WHERE Occupation LIKE '%Engineer%'
-- Result= 502 y 2483. El 20.21%  de los ingenieros a los que llamaron compraron el curso




--a. Calcular las ventas totales y las llamadas ATENDIDAS realizadas a los clientes de la profesión de ingeniería
SELECT SUM(ProductSold) AS TotalSales, COUNT(*) AS NCalls
FROM customers Cu
join calls Ca ON Ca.CustomerID = Cu.CustomerID
WHERE Occupation LIKE '%Engineer%' and pickedup=1
-- Result = 502 y 1751: El 28.67% de los ingenieros que atendieron compraron el curso

--b. Generar otra consulta que calcule las mismas métricas para toda la base de clientes.
SELECT SUM(ProductSold) AS TotalSales, COUNT(*) AS NCalls
FROM customers Cu
join calls Ca ON Ca.CustomerID = Cu.CustomerID
-- Result=  = 2084 y 9925. El 20.99%  de TODOS los profesionales a los que llamaron compraron el curso


--c.¿Qué puedes concluir con respecto a la tasa de conversión entre los clientes de ingeniería frente a la base de clientes en general?
--  La tasa de conversión para ambos grupos es ~20.9%, lo que indica que los ingenieros no tienen más probabilidades de comprar nuestros productos que la población en general.

--d.¿Valdría la pena invertir en publicidad en el segmento de clientes que son ingenieros y mayores de 30 años? 
