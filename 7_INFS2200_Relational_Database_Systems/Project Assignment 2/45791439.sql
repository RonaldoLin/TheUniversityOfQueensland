--Line Size
SET LINE 300;

--Time
SET TIMING ON;

--Task 1 - Views

--1 Film Search
SELECT F.title 
FROM film F, film_category FC, language L, category C
WHERE F.film_id = FC.film_id 
AND C.category_id = FC.category_id 
AND F.language_id = L.language_id
AND F.length < 50 
AND L.name = 'English'
AND C.name = 'Comedy';

--2 Actor Search
SELECT DISTINCT actor_id, first_name, last_name
FROM actor, film
WHERE title in (SELECT title 
		FROM film, language, category
		WHERE film.length < 50 
		AND language.name = 'English'
		AND category.name = 'Comedy');

--3 Virtual View Create
CREATE VIEW V_HR_MU_2010_ACTORS AS
SELECT DISTINCT actor_id, first_name, last_name
FROM actor, film, category
WHERE film.rental_rate > 4
AND film.release_year = 2010
AND category.name = 'Music';

--4 Materialized View Create
CREATE MATERIALIZED VIEW MV_HR_MU_2010_ACTORS
BUILD IMMEDIATE
AS
SELECT DISTINCT actor_id, first_name, last_name
FROM actor, film, category
WHERE film.rental_rate > 4
AND film.release_year = 2010
AND category.name = 'Music';

--5 View Execution Time & Plan

--Virtual View
SELECT * FROM V_HR_MU_2010_ACTORS;
EXPLAIN PLAN FOR SELECT * FROM V_HR_MU_2010_ACTORS;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--Materialized View
SELECT * FROM MV_HR_MU_2010_ACTORS;
EXPLAIN PLAN FOR SELECT * FROM MV_HR_MU_2010_ACTORS;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--Task 2 - Indexes

--1 Film Search
SELECT title
FROM film
WHERE INSTR (description, 'Boat') > 0
ORDER BY title ASC
FETCH FIRST 10 ROWS ONLY;

--2 Function-based Index Create
CREATE INDEX IDX_BOAT ON film (INSTR(TO_CHAR(description), ‘Boat’));

--3 Function-based Index Execution Time & Plan

--Film Search
SELECT title
FROM film
WHERE INSTR (description, 'Boat') > 0
ORDER BY title ASC
FETCH FIRST 10 ROWS ONLY;

--Function-based Index
EXPLAIN PLAN FOR SELECT title FROM film WHERE INSTR (description, 'Boat') > 0;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--Function-based Index Drop
DROP INDEX IDX_BOAT;

--Film Search
SELECT title
FROM film
WHERE INSTR (description, 'Boat') > 0
ORDER BY title ASC
FETCH FIRST 10 ROWS ONLY;

--No Function-based Index
EXPLAIN PLAN FOR SELECT title FROM film WHERE INSTR (description, 'Boat') > 0;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--4 Film Number Count
SELECT SUM(COUNT(*)) 
FROM film 
WHERE release_year IS NOT NULL AND rating IS NOT NULL AND special_features IS NOT NULL
GROUP BY release_year, rating, special_features 
HAVING COUNT(*) >= 41;

--5 Bitmap Index Create

--BIDX_YEAR 
CREATE BITMAP INDEX BIDX_YEAR ON film (release_year);

--BIDX_RATE
CREATE BITMAP INDEX BIDX_RATE ON film(rating);

--BIDX_FEATURE
CREATE BITMAP INDEX BIDX_FEATURE ON film(special_features);

--6 Bitmap Execution Time & Plan

--Film Number Count
SELECT SUM(COUNT(*)) 
FROM film 
WHERE release_year IS NOT NULL AND rating IS NOT NULL AND special_features IS NOT NULL
GROUP BY release_year, rating, special_features 
HAVING COUNT(*) >= 41;

--Bitmap Index
EXPLAIN PLAN FOR SELECT SUM(COUNT(*)) FROM film WHERE release_year IS NOT NULL AND rating IS NOT NULL AND special_features IS NOT NULL GROUP BY release_year, rating, special_features HAVING COUNT(*) >= 41;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--Bitmap Index Drop

--INDEX BIDX_YEAR
DROP INDEX BIDX_YEAR;

--INDEX BIDX_RATE
DROP INDEX BIDX_RATE;

--INDEX BIDX_FEATURE
DROP INDEX BIDX_FEATURE;

--Film Number Count
SELECT SUM(COUNT(*)) 
FROM film 
WHERE release_year IS NOT NULL AND rating IS NOT NULL AND special_features IS NOT NULL
GROUP BY release_year, rating, special_features 
HAVING COUNT(*) >= 41;

--No Bitmap Index
EXPLAIN PLAN FOR SELECT SUM(COUNT(*)) 
FROM film 
WHERE release_year IS NOT NULL AND rating IS NOT NULL AND special_features IS NOT NULL
GROUP BY release_year, rating, special_features 
HAVING COUNT(*) >= 41;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--Task 3 - Execution Plan

--1 B+ Tree Index 
ANALYZE INDEX PK_FILMID VALIDATE STRUCTURE;
ANALYZE TABLE FILM COMPUTE STATISTICS;

--Height
SELECT HEIGHT FROM INDEX_STATS;

--Leaf Block Number
SELECT LF_BLKS FROM INDEX_STATS;

--Block Access Number
SELECT BLOCKS FROM USER_TABLES WHERE TABLE_NAME = ‘FILM’;

--2 Rule-based > 100
EXPLAIN PLAN FOR SELECT /*+RULE*/ * FROM FILM WHERE FILM_ID > 100;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--3 Cost-based > 100
EXPLAIN PLAN FOR SELECT * FROM FILM WHERE FILM_ID > 100;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--4 Cost-based > 19990
EXPLAIN PLAN FOR SELECT * FROM FILM WHERE FILM_ID > 19990;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);

--5 Cost-based = 100
EXPLAIN PLAN FOR SELECT * FROM FILM WHERE FILM_ID = 100;
SELECT PLAN_TABLE_OUTPUT FROM TABLE (DBMS_XPLAN.DISPLAY);
