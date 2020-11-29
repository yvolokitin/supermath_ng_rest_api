mysql -h localhost -u root -pasdas12 supermath_db;
mysql -u root -pasdas12 supermath_db;

select ID, NAME, FAIL from users;

select ID, NAME, SURNAME, AVATAR, FAIL from users ORDER BY FAIL DESC LIMIT 10;

select ID, NAME, SURNAME, AVATAR, PASS from users ORDER BY PASS DESC LIMIT 10;

select * from results where USERID=1 AND monthname(EXECUTION_DATE)='June';

UPDATE users SET LEVEL='NONE' WHERE ID=9;
UPDATE users SET SOLVED='white1,white2,white3,white4,white5,white6,orange1,green1,' WHERE ID=9;
select ID, NAME, LANG, SOLVED, LEVEL from users where ID=9;

select ID, NAME, LANG, SOLVED, LEVEL from users;

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
    `ID` bigint(20) NOT NULL auto_increment,
    `LEVEL` varchar(8) DEFAULT 'task_1',
    `RU` varchar(512) DEFAULT '',
    `EN` varchar(512) DEFAULT '',
    `NL` varchar(512) DEFAULT '',
    `DE` varchar(512) DEFAULT '',
    `FR` varchar(512) DEFAULT '',
    `ES` varchar(512) DEFAULT '',
    `IT` varchar(512) DEFAULT '',
    `RESULT` varchar(32) NOT NULL,
    `IMAGE` varchar(64) DEFAULT '',
    PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=1;

INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Периметр квадрата равен 24 см. Чему равна сторона квадрата?', 'The perimeter of the square is 24 cm. What is the side of the square?', 'De omtrek van het vierkant is 24 cm Wat is de zijde van het vierkant?', '6', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Миша купил в магазине яблоки и груши. Яблоки стоили 50 рублей, а груши в 2 раза дороже. Сколько рублей потратил Миша?', 'Mike bought apples and pears in the store. Apples cost 50 euro, and pears cost in two time expensive. How much money Mike spent?', 'Mike kocht appels en peren in de winkel. Appels kosten 50 euro en peren kosten in twee keer duur. Hoeveel geld heeft Mike uitgegeven?', '150', 'apples_pears.jpg');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Чему равен периметр квадрата, если длина одной его стороны 7см?', 'What is the perimeter of a square if the length of one side is 7cm?', 'Wat is de omtrek van een vierkant als een zijde 7 cm lang is?', '28', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько углов у прямоугольника?', 'How many corners does a rectangle have?', 'Hoeveel hoeken heeft een rechthoek?', '4', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько останется, если из восьми десятков вычесть разность чисел 28 и 15?', 'How much will you have if you subtract the difference of 28 and 15 from eight tens?', 'Hoeveel heb je als je het verschil van 28 en 15 aftrekt van acht tienen?', '67', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько углов у круга?', 'How many corners does a circle have?', 'Hoeveel hoeken heeft een cirkel?', '0', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Чему равно уменьшаемое если разность 13 и вычитаемое 7?', 'What is the minuend if the difference is 13 and the subtrahend is 7?', 'Wat is de minuend als het verschil 13 is en de aftrekker 7?', '20', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Реши цепочку: 57 - 14 + 17 - 20 + 15 = ?', 'Solve the math chain: 57 - 14 + 17 - 20 + 15 = ?', 'Los de wiskundeketen op: 57 - 14 + 17 - 20 + 15 = ?', '55', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Периметр квадрата равен 20 см. Чему равна сторона квадрата?', 'The perimeter of the square is 20 cm. What is the length of one side of the square?', 'De omtrek van het vierkant is 20 cm. Wat is de lengte van één zijde van het vierkant?', '5', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько сторон у параллелограмма?', 'How many sides does a parallelogram have?', 'Hoeveel zijden heeft een parallellogram?', '4', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько всего рук и ног у 6 мальчиков?', 'How many arms and legs do 6 boys have all together?', 'Hoeveel armen en benen hebben 6 jongens allemaal bij elkaar?', '24', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Реши цепочку: 33 + 12 - 19 + 5x4 + 89 - 76 = ?', 'Solve the math chain: 33 + 12 - 19 + 5x4 + 89 - 76 = ?', 'Los de wiskundeketen op: 33 + 12 - 19 + 5x4 + 89 - 76 = ?', '59', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько углов у овала?', 'How many corners does the oval have?', 'Hoeveel hoeken heeft het ovaal?', '0', '');

INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_2', 'На часах 3 часа 15 минут, сколько градусов между стрелками?', '','', '', '');

INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Сколько сторон у ромба?', '','', '4', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Реши цепочку: 57 - 14 + 17 - 20 + 15 = ?', 'Solve the math chain: 57 - 14 + 17 - 20 + 15 = ?', 'Los de wiskundeketen op: 57 - 14 + 17 - 20 + 15 = ?', '55', '');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Вычисли разность 52 и 19', '33', '');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Чему равно уменьшаемое если разность 13 и вычитаемое 7', '20', 'difference.png');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Чему равно вычитаемое если разность 53 и уменьшаемое 78', '25', 'difference.png');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у прямоугольника?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сколько сторон у трапеции?', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '4', 'chetirehugolnik.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '0', 'krugs.jpg');

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Уменьшаемое 80, разность 54. Чему равно вычитаемое?', '26', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Сумму чисел 9 и 24 увеличить на 13. Ответ?', '46', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Из 8 десятков вычесть разность чисел 28 и 15. Ответ?', '67', 'solving.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '24', 'butterfly.png');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', 'Вычисли периметр прямоугольника, если ширина 3 см, что на 5см меньше длины?', '22', 'perimeter.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '5', 'perimeter.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `IMAGE`) VALUES ('task_1', 'ru', '', '55', 'chain.jpg');


INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', '', '90', 'градусов', 'clock.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', 'На часах 6 часа 00 минут, сколько градусов между стрелками?', '180', 'градусов', 'clock.jpg');
INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`, `UNITS`, `IMAGE`) VALUES ('task_2', 'ru', 'На часах 4 часа 50 минут, сколько градусов между стрелками?', '180', 'градусов', 'clock.jpg');
