-- Select all columns from cities
Select * from cities


SELECT *
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;


-- Select name fields (with alias) and region 
SELECT cities.name AS city, countries.name AS country, countries.region
FROM cities
INNER JOIN countries
ON cities.country_code = countries.code;

------------------------


-- Select fields with aliases
SELECT c.code AS country_code, c.name, e.year, e.inflation_rate
FROM countries AS c
-- Join to economies (alias e)
INNER JOIN economies AS e
-- Match on code field using table aliases
ON c.code = e.code;



SELECT c.name AS country, l.name AS language, official
FROM countries AS c
INNER JOIN languages AS l
-- Match using the code column
USING (code);


----------------------------------------------

-- This is a one-to-many relationship.


--This is a many-to-many relationship

--Inspecting a Relationship
-- Select country and language names, aliased
SELECT c.name AS country, l.name AS language
-- From countries (aliased)
FROM countries AS c
-- Join to languages (aliased)
INNER JOIN languages AS l
-- Use code as the joining field with the USING keyword
USING (code);



-- Rearrange SELECT statement, keeping aliases
SELECT c.name AS country, l.name AS language
FROM countries AS c
INNER JOIN languages AS l
USING(code)
-- Order the results by language
ORDER BY language;

--Alsatian is spoken in more than one country.


--Joining multiple tables

-- Select relevant fields
SELECT name, year, fertility_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
-- Inner join countries and populations, aliased, on code




-- Select fields
SELECT name, p.year, fertility_rate, e.year, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
-- Join to economies (as e)
INNER JOIN economies AS e
ON c.code = e.code;
-- Match on country code


--Checking multi-table joins
SELECT name, e.year, fertility_rate, unemployment_rate
FROM countries AS c
INNER JOIN populations AS p
ON c.code = p.country_code
INNER JOIN economies AS e
ON c.code = e.code
-- Add an additional joining condition such that you are also joining on year
AND e.year = p.year;




