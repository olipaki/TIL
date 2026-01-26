-- Active: 1769144862377@@127.0.0.1@5432@dvdrental
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

SELECT continent, COUNT(*) as country_count
FROM country
GROUP BY continent;

-- 대륙 별 국가 수가 20개가 넘는 대륙, 국가 수 조회
SELECT continent, COUNT(*) as country_count
FROM country
FROM country
GROUP BY countinent
HAVING COUNT

SELECT continent, COUNT(*) as country_count
FROM country
GROUP BY continent
HAVING COUNT(*) > 20;

####Dvdrental################
-- - **`title`**: 영화 제목
-- - **`rental_rate`**: 영화 대여료 (금액)
-- - **`rating`**: 영화 관람 등급 (G, PG, R 등)
-- - **`length`**: 영화 상영 시간 (분 단위)
-- - **`rental_duration`**: 대여 가능 기간 (일 단위)
-- - **`replacement_cost`**: 영화 분실 시 변상 비용

-- 1. 모든 영화의 제목과 대여료를 조회하시오.
SELECT title, rental_rate
FROM film;

-- 2. 대여료가 4달러 이상인 영화의 제목과 대여료를 조회하시오.
SELECT title,rental_rate
FROM film
WHERE rental_rate >= 4;

-- 3. 등급별 영화 수를 조회하시오.
SELECT rating, count(*) 
from film
GROUP BY rating;


-- 4. 상영 시간을 중복 제거하여 내림차순으로 정렬하고, 
-- 상위 10개를 조회하시오.
-- DISTINCT로 겹치는 시간 다 빼버리고, 
-- DISTINCT로 큰 놈부터 줄 세운 뒤 딱 10명만 끊음
SELECT DISTINCT length
FROM film 
ORDER BY length DESC 
LIMIT 10;

-- 5. 대여 기간별 영화 수를 대여 기간 내림차순으로 
-- 정렬하여 조회하시오.
SELECT title,rental_duration,rental_rate
FROM film
WHERE rental_duration >=5
AND rental_rate >=4;

-- -- 6. 대여 기간이 5일 이상이고 
-- 대여료가 4달러 이상인 
-- 영화의 제목, 대여 기간, 
-- 대여료를 조회하시오.
SELECT title,rental_duration,rental_rate
FROM film
WHERE rental_duration >=5
AND rental_rate  >=4;


-- 7. 등급이 'R'인 영화 중
--  처음 10개의 제목과 등급을 조회하시오.
SELECT title,rating
FROM film
WHERE rating = 'R'
ORDER BY title
LIMIT 10;

-- 8. 대여료별 영화 수를 영화 수 내림차순으로 정렬하여 조회하시오.
SELECT rental_rate,COUNT(*)
FROM film
GROUP BY rental_rate
ORDER BY COUNT(*) DESC;


-- 9. 교체 비용별 영화 수와 평균 대여료를 교체 비용 오름차순으로 정렬하여 조회하시오.
SELECT Count(*),AVG(rental_rate)
FROM film
GROUP by replacement_cost
ORDER BY replacement_cost;

-- 10. 제목에 'angel'이 포함된 영화의 제목을 조회하시오.
SELECT title
FROM film
WHERE title ILIKE '%ace%'

-- 11. 등급별 평균 대여료가 3달러 미만인 등급과 평균 대여료를 조회하시오.

-- 12. 상영 시간이 10번째에서 15번째로 긴 영화의 제목과 상영 시간을 조회하시오. (상영 시간이 같을 경우 제목 오름차순으로 정렬)

-- 13. 등급이 'PG' 또는 'G'이면서 대여 기간이 4일 이하인 영화의 제목, 등급, 대여 기간을 조회하시오.

-- 14. 등급별 영화 수와 평균 상영 시간을 조회하시오.

-- 15. 상영 시간이 60분 이상 120분 이하인 영화의 제목과 상영 시간을 상영 시간 오름차순으로 조회하시오.
