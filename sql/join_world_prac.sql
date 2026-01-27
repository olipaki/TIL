-- Active: 1769144862377@@127.0.0.1@5432@dvdrental
-- - world database
    -- - 어느 나라에 속한 도시인지
        SELECT co.name AS country_name, 
            ci.name AS capital_city
        FROM city ci
        JOIN country co ON ci.countrycode = co.code
    
    -- - 국가와 그 국가의 공식 수도를 매칭
        
    --     ```sql
    --     SELECT 
    --         co.name AS country_name, 
    --         ci.name AS capital_city
    --     FROM country co
    --     JOIN city ci ON co.capital = ci.id;
    --     ```
        
    
    -- - 특정 대륙에 속한 도시들 목록
        
    --     ```sql
    --     SELECT 
    --         co.continent, 
    --         co.name AS country_name, 
    --         ci.name AS city_name
    --     FROM country co
    --     JOIN city ci ON co.code = ci.countrycode
    --     WHERE co.continent = 'Asia'
    --     ORDER BY co.name, ci.name;
    --     ```
        
    
    -- - 특정 대륙에서 인구가 500만 명 이상인 도시만 조회
        
    --     ```sql
    --     SELECT 
    --         co.continent, 
    --         co.name AS country, 
    --         ci.name AS city, 
    --         ci.population
    --     FROM country co
    --     JOIN city ci ON co.code = ci.countrycode
    --     WHERE co.continent = 'Asia'       
    --       AND ci.population >= 5000000    
    --     ORDER BY ci.population DESC;
    --     ```
        
    
    -- - 국가와 수도, 공식언어 가져오기
        -- co.name AS country_name, ci.name AS capital_city,cl."Language"
    --     FROM country co
    --     JOIN city ci ON co.capital = ci.id
    --     JOIN countrylanguage cl ON co.code = cl.countrycode
    --     WHERE cl.isofficial = 'T'
    #################################################################
#1. 배우가 출연한 영화의 제목을 조회
SELECT a.first_name,a.last_name,f.title
FROM actor a
Join film_actor fa ON a.actor_id = fa.actor_id
JOIN film f ON fa.film_id = f.film_id;

-- . first_name이 PENELOPE 인 배우가 출연한 영화 제목
-- 논리: 1번 쿼리에 WHERE 조건만 딱 걸어주면 끝!
-- 코드: ... WHERE a.first_name = 'PENELOPE';

SELECT 
    f.title   -- 우리가 최종적으로 보고 싶은 건 '영화 제목'이지!
FROM actor a  -- 1번 주머니: 배우
JOIN film_actor fa ON a.actor_id = fa.actor_id  -- 2번 주머니: 출연 명단 (연결고리)
JOIN film f ON fa.film_id = f.film_id           -- 3번 주머니: 영화 정보
WHERE a.first_name = 'PENELOPE';  -- 주인공 이름이 'PENELOPE'인 경우만!

-- 3. 영화 별 출연 배우의 수를 조회
-- 논리: 영화별로 묶고(GROUP BY), 배우 ID를 세면(COUNT) 되겠죠?
-- 코드:

SELECT f.title, COUNT(fa.actor_id)
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
GROUP BY f.title;

-- 4. 출연 배우 수가 5명 초과인 데이터를 배우 수 큰 순으로 조회
-- 논리: 묶은 결과에 조건을 걸 때는 뭐다? HAVING! 정렬은 ORDER BY DESC!
-- 코드: ... 

-- GROUP BY f.title 
-- HAVING COUNT(fa.actor_id) > 5 
-- ORDER BY COUNT(fa.actor_id) DESC;

-- 5. 고객의 대여 정보 조회
-- 논리: 고객(customer)과 대여(rental) 테이블을 잇습니다.
-- 코드: 
SELECT c.first_name, r.rental_date 
FROM customer c JOIN rental r ON c.customer_id = r.customer_id;

-- 6. 고객이 대여한 영화 정보 조회
-- 논리: 이게 중요해요! 고객 → 대여 → 재고 → 영화 순으로 징검다리를 3개 건너야 합니다.
-- 코드:

SELECT c.first_name, f.title
FROM customer c
JOIN rental r ON c.customer_id = r.customer_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film f ON i.film_id = f.film_id;