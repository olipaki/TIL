-- Active: 1769144862377@@127.0.0.1@5432@world@public
select * from country;
SELECT c.name, c.population FROM country;
SELECT country.name, country.population FROM country c;
SELECT continent FROM country;

-- 인구가 800만 이상인 도시의 name, population을 조회하시오
SELECT name, population
FROM city
WHERE population >= 8000000;

- 한국(KOR)에 있는 도시의 name, countrycode를 조회하시오

SELECT name, countrycode
FROM city
WHERE countrycode = 'KOR';

- 유럽 대륙에 속한 나라들의 name과 region을 조회하시오.

- 이름이 'San'으로 시작하는 도시의 name을 조회하시오



-- 독립 연도 (indepyear)가 1900년 이후인 나라의 name, indepyear를 조회하시오.
SELECT name, indepyear FROM country WHERE indepyear > 1900;

-- 인구가 100만에서 200만 사이인 한국 도시의 name을 조회하시오.
SELECT name
FROM city
WHERE population BETWEEN 1000000 AND 2000000
  AND countrycode = 'KOR';

  SELECT name, countrycode, population
FROM city
WHERE population >= 5000000
  AND countrycode IN ('KOR', 'CHN', 'JPN');



