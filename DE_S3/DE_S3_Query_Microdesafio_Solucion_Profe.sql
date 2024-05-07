--6. Crear un procedimiento almacenado para el ETL
--- es la tecnica mas sencilla (aclarado y rellenado) pero no es la unica tecnica (e.g actualizacion)

CREATE PROCEDURE pETL_Desastres
AS $$
DELETE FROM DESASTRES_BDE.dbo.DESASTRES_FINAL;

INSERT INTO DESASTRES_FINAL
SELECT x.Cuatrenio, AVG(x.Temperatura) AS Temp_AVG, AVG(x.NivelOxigeno) AS Oxi_AVG,
SUM(x.Tsunamis) AS T_Tsunamis,SUM(x.OlasCalor) AS T_OlasCalor,SUM(x.Terremotos) AS T_Terremotos,
SUM(x.Erupciones) AS T_Erupciones,SUM(x.Incendios) AS T_Incendios,
AVG(x.Muertes_Jovenes) as M_Jovenes_AVG,AVG(x.Muertes_Adultos) as M_Adultos_AVG, AVG(x.Muertes_Ancianos) as M_Ancianos_AVG
FROM
(SELECT CASE WHEN c.año < 2026 THEN '2023-2026' ELSE '2027-2030' END AS Cuatrenio,
Temperatura =c.temperatura,
NivelOxigeno =c.oxigeno,
Tsunamis= d.Tsunamis,
OlasCalor= d.Olas_calor,
Terremotos= d.Terremotos,
Erupciones= d.Erupciones,
Incendios=d.Incendios, 
Muertes_Jovenes= m.R_Menor15 + m.R_15_a_30,
Muertes_Adultos= m.R_30_a_45 +m.R_45_a_60,
Muertes_Ancianos= m.R_M_a_60
FROM DESASTRES c
JOIN DESASTRES d ON c.año =d.año
JOIN DESASTRES m ON c.año = m.año) x
GROUP BY x.Cuatrenio
