SELECT * FROM
(SELECT ca.agentid, ca.duration, max(customerid) AS customerid
   FROM
   (
       SELECT agentid, min(duration) as fastestcall
       FROM calls
       WHERE productsold = 1
       GROUP BY agentid
   ) min
   JOIN calls ca ON ca.agentid = min.agentid AND ca.duration = min.fastestcall
   JOIN agents a ON ca.agentid = a.agentid
   WHERE productsold = 1
   GROUP BY ca.agentid, ca.duration) as x
   LEFT JOIN customers cu on x.customerid= cu.customerid
   
   
   
--Solucion de Manuel en CHATgpt  
   
   
   SELECT 
    ca.agentid,
    ca.duration,
    cu.customerid
FROM 
    (
        SELECT 
            agentid,
            duration,
            customerid,
            ROW_NUMBER() OVER (PARTITION BY agentid ORDER BY duration) AS row_num
        FROM 
            calls
        WHERE 
            productsold = 1
    ) ca
LEFT JOIN 
    customers cu ON ca.customerid = cu.customerid
WHERE 
    ca.row_num = 1
   
   
   