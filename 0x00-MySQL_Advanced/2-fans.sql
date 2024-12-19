-- Ranking Origin bands, ordered by the number of fans

SELECT orgin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC
