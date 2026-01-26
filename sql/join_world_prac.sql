-- Active: 1769144862377@@127.0.0.1@5432@world@public
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
        co.name AS country_name, ci.name AS capital_city,cl."Language"
    --     FROM country co
    --     JOIN city ci ON co.capital = ci.id
    --     JOIN countrylanguage cl ON co.code = cl.countrycode
    --     WHERE cl.isofficial = 'T'
    #################################################################

    