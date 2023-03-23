

create table character_comic (
	id serial, 
	name varchar(250), 
	comic varchar(750), 
	character_id bigint
); 

select * 
from character_comic; 

alter table character_comic 
	add character_id bigint; 

-- truncate table character_comic; 



select * 
from pg_user 
; 


create table hero_count ( 
	hero varchar, 
	count integer 
); 

select * 
from hero_count 
; 



call usp_character_comic_count() ; 
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