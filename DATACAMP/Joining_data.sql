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


--This is a LEFT JOIN, right?
SELECT 
    c1.name AS city,
    c2.code,
    c2.name AS country,
    c2.region,
    c1.city_proper_pop
FROM cities AS c1 INNER JOIN countries as c2 on c1.country_code = c2.code;

SELECT 
	c1.name AS city, 
    c2.code, 
    c2.name AS country,
    c2.region, 
    c1.city_proper_pop
FROM cities AS c1 LEFT JOIN countries AS c2 
ON c1.country_code = c2.code
ORDER BY code DESC;


--Building on your LEFT JOIN
SELECT name,region,gdp_percapita
FROM countries AS c
LEFT JOIN economies AS e ON c.code = e.code  WHERE YEAR = 2010;

--Is this RIGHT?
-- Modify this query to use RIGHT JOIN instead of LEFT JOIN
SELECT countries.name AS country, languages.name AS language, percent
FROM languages
RIGHT JOIN countries
ON countries.code = languages.code
ORDER BY language;


--Comparing joins
SELECT name AS country, code, region, basic_unit
FROM countries
FULL JOIN currencies
USING (code)
WHERE region ='North America' OR name ISNULL
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
LEFT JOIN currencies
USING (code)
WHERE region = 'North America' 
OR name IS NULL
ORDER BY region;

SELECT name AS country, code, region, basic_unit
FROM countries
INNER JOIN currencies
USING (code)
WHERE region = 'North America' 
OR name IS NULL
ORDER BY region;


--Chaining FULL JOINs
SELECT 
	c1.name AS country, 
    region, 
    l.name AS language,
	basic_unit, 
    frac_unit
FROM countries as c1 
FULL JOIN languages as l on c1.code = l.code
-- Full join with languages (alias as l)
-- Full join with currencies (alias as c2)
FULL JOIN currencies as c2 on c1.code = c2.code
WHERE region LIKE 'M%esia';


--Histories and languages
SELECT c.name AS country, l.name AS language
-- Inner join countries as c with languages as l on code
FROM countries AS c INNER JOIN
languages AS l 
ON c.code = l.code
WHERE c.code IN ('PAK','IND')
	AND l.code in ('PAK','IND');


--Choosing your join
SELECT 
	c.name AS country,
    region,
    life_expectancy AS life_exp
FROM countries AS c
-- Join to populations (alias as p) using an appropriate join
INNER JOIN populations as p
ON c.code = p.country_code
-- Filter for only results in the year 2010
WHERE p.YEAR = 2010
-- Sort by life_exp
ORDER BY life_exp
-- Limit to five records
LIMIT 5;


--Comparing a country to itself
-- Select aliased fields from populations as p1
SELECT p1.country_code,p2.country_code,p1.size as size2010,p2.size as size2015
FROM populations as p1 INNER JOIN populations as p2 on p1.country_code = p2.country_code;
-- Join populations as p1 to itself, alias as p2, on country code


--Comparing global economies
-- Select all fields from economies2015
SELECT * FROM economies2015  
UNION
-- Select all fields from economies2019
SELECT * FROM economies2019
ORDER BY code, year;


--Comparing two set operations
-- Query that determines all pairs of code and year from economies and populations, without duplicates
SELECT code, YEAR from economies
UNION
SELECT country_code,YEAR from populations;

SELECT code, year
FROM economies
-- Set theory clause
UNION ALL
SELECT country_code, year
FROM populations
ORDER BY code, year;

--INTERSECT
-- Return all cities with the same name as a country
SELECT NAME FROM cities
INTERSECT
SELECT NAME FROM countries;


--You've got it, EXCEPT...
-- Return all cities that do not have the same name as a country
SELECT NAME FROM cities
EXCEPT
SELECT NAME FROM countries
ORDER BY name;


--Semi join
-- Select country code for countries in the Middle East
SELECT code FROM countries WHERE region ='Middle East'

--Diagnosing problems using anti join
-- Select code and name of countries from Oceania
SELECT code, NAME FROM countries WHERE continent ='Oceania'

--Subquery inside WHERE
-- Select average life_expectancy from the populations table
SELECT AVG(life_expectancy) from populations
-- Filter for the year 2015
WHERE YEAR =2015;

--WHERE do people live?
-- Select relevant fields from cities table
SELECT NAME,country_code,urbanarea_pop FROM cities
-- Filter using a subquery on the countries table
WHERE NAME IN(
  SELECT capital from countries
)
ORDER BY urbanarea_pop DESC;

--Subquery inside SELECT
-- Find top nine countries with the most cities
SELECT countries.NAME as country, count(countries.NAME) as cities_num FROM countries
LEFT JOIN cities
on countries.code = cities.country_code
GROUP BY countries.NAME
-- Order by count of cities as cities_num
ORDER BY cities_num DESC,countries.NAME LIMIT 9;


--Subquery inside FROM
-- Select code, and language count as lang_num
SELECT code,COUNT(NAME) as lang_num FROM languages GROUP BY code;

--Subquery challenge
-- Select relevant fields
SELECT code,inflation_rate,unemployment_rate FROM economies
WHERE YEAR=2015 and code NOT IN
(SELECT code from countries where gov_form LIKE '%Republic%' or gov_form LIKE '%Monarchy%' )
ORDER BY economies.inflation_rate;


--Final challenge
-- Select fields from cities
SELECT NAME,country_code,city_proper_pop,metroarea_pop,city_proper_pop / metroarea_pop * 100 as city_perc FROM cities
-- Use subquery to filter city name
WHERE NAME in (SELECT capital from countries WHERE continent LIKE '%Europe%' or continent LIKE '%America')
-- Add filter condition such that metroarea_pop does not have null values
and NOT(metroarea_pop ISNULL)
-- Sort and limit the result
ORDER BY city_perc DESC
LIMIT 10;







