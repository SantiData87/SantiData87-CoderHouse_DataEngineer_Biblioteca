--Este panel se reúne cada cuatro años y quiere que dejes almacenado un procedimiento llamado pETL_Desastres que permita cuantificar el cambio promedio en Temperatura y Oxígeno así como la suma total de los otros eventos mencionados por cuatrienios (2023-2026 y 2027-2030) llenando una tabla denominada DESASTRES_FINAL en una base de datos llamada DESASTRES_BDE. El código SQL para la creación de tablas y valores respectivos con el fin de crear este procedimiento las encuentras en este enlace
--Tener en cuenta el concepto de JOINS
--Hacer uso de funciones de agregación
--Hacer uso del CASE-END
------------------------------------------------------------------
CREATE OR REPLACE FUNCTION pETL_Desastres()
RETURNS VOID AS $$
BEGIN


-- Eliminar informacion existente en desastres_final
	DELETE FROM desastres_final

	
INSERT INTO desastres_final
SELECT
	CASE WHEN t1.año<=2026 THEN '2023-2026' ELSE '2027-2030' END AS Cuatrenio,
	AVG (t2.temperatura) AS avg_temp,
	AVG (t2.oxigeno) as avg_oxygen,
	SUM (t1.tsunamis) AS total_tsunamis,
	SUM (t1.olas_calor) AS total_olas_calor,
	SUM (t1.terremotos) AS total_terremotos , 
	SUM (t1.erupciones) AS total_erupciones , 
	SUM (t1.incendios) AS total_incendios , 
	AVG (t3.r_menor15+t3.r_15_a_30) AS avg_muertes_jovenes,
	AVG (t3.r_30_a_45+t3.r_45_a_60) AS avg_muertes_adultosjovenes,
	AVG (t3.r_m_a_60) AS avg_muertes_ancianos
FROM desastres t1
LEFT JOIN clima t2 ON t1.año = t2.año
LEFT JOIN muertes t3 ON t1.año = t2.año
GROUP BY 1;
---------------------------------------------------
END;
$$ LANGUAGE plpgsql;

-- Resultado
select * from desastres_final











