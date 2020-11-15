select ID, NAME, FAIL from users;

select ID, NAME, SURNAME, AVATAR, FAIL from users ORDER BY FAIL DESC LIMIT 10;

select ID, NAME, SURNAME, AVATAR, PASS from users ORDER BY PASS DESC LIMIT 10;

select * from results where USERID=1 AND monthname(EXECUTION_DATE)='June';


INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_1', 'ru', 'Периметр квадрата равен 24 см. Чему равна сторона квадрата?', '6', 'см', 'perimeter.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_1', 'ru', 'Чему равен периметр квадрата, если длина одной его стороны 7см?', '28', 'см', 'perimeter.jpg');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Вычисли разность 52 и 19', '33', 'difference.png');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Чему равно уменьшаемое если разность 13 и вычитаемое 7', '20', 'difference.png');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Чему равно вычитаемое если разность 53 и уменьшаемое 78', '25', 'difference.png');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько углов у прямоугольника?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у прямоугольника?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у трапеции?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у ромба?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у параллелограмма?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько углов у круга?', '0', 'krugs.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько углов у овала?', '0', 'krugs.jpg');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Уменьшаемое 80, разность 54. Чему равно вычитаемое?', '26', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сумму чисел 9 и 24 увеличить на 13. Ответ?', '46', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Из 8 десятков вычесть разность чисел 28 и 15. Ответ?', '67', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько крыльев у 6 бабочек?', '24', 'butterfly.png');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Вычисли периметр прямоугольника, если ширина 3 см, что на 5см меньше длины?', '22', 'perimeter.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Периметр квадрата равен 20 см. Чему равна сторона квадрата?', '5', 'perimeter.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Реши цепочку: 57 - 14 + 17 - 20 + 15 = ?', '55', 'chain.jpg');


INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', 'На часах 3 часа 15 минут, сколько градусов между стрелками?', '90', 'градусов', 'clock.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', 'На часах 6 часа 00 минут, сколько градусов между стрелками?', '180', 'градусов', 'clock.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', 'На часах 4 часа 50 минут, сколько градусов между стрелками?', '180', 'градусов', 'clock.jpg');
