SELECT
        a.name AS agent_name,
        cu.name AS customer_name,
        c.duration AS fastest_sale_duration
    FROM (
        SELECT
            agentid,
            MIN(duration) AS fastest_duration
        FROM calls
        WHERE productsold = 1
        GROUP BY agentid
    ) AS min_duration
    JOIN calls c ON c.agentid = min_duration.agentid AND c.duration = min_duration.fastest_duration
    JOIN agents a ON a.agentid = c.agentid
    JOIN customers cu ON cu.customerid = c.customerid
    WHERE c.productsold = 1
    ORDER BY fastest_sale_duration ASC;