select ID, NAME, FAIL from users;

select ID, NAME, SURNAME, AVATAR, FAIL from users ORDER BY FAIL DESC LIMIT 10;

select ID, NAME, SURNAME, AVATAR, PASS from users ORDER BY PASS DESC LIMIT 10;

select * from results where USERID=1 AND monthname(EXECUTION_DATE)='June';
