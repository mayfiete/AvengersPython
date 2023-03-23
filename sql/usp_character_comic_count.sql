create table hero_count ( 
	hero varchar, 
	count integer 
); 


-- drop procedure usp_character_comic_count; 
CREATE PROCEDURE usp_character_comic_count()
  LANGUAGE plpgsql
AS $$
begin
	insert into hero_count (hero, count)
   SELECT name as hero,
               count(*) as cnt
               FROM character_comic
               GROUP BY name 
         ; 
              
END;
$$;

call usp_character_comic_count() ; 

select * 
from hero_count 
; 
