-- displays the average temperature
-- ordered by temperature
SELECT city, AVG(value) as avg_tempt
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
