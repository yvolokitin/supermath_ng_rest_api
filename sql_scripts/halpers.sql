select ID, NAME, FAIL from users;

select ID, NAME, SURNAME, AVATAR, FAIL from users ORDER BY FAIL DESC LIMIT 10;

select ID, NAME, SURNAME, AVATAR, PASS from users ORDER BY PASS DESC LIMIT 10;

select * from results where USERID=1 AND monthname(EXECUTION_DATE)='June';


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

INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Периметр квадрата равен 24 см. Чему равна сторона квадрата?', 'The perimeter of the square is 24 cm. What is the side of the square?', 'De omtrek van het vierkant is 24 cm Wat is de zijde van het vierkant?', '6', '');
INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', 'Чему равен периметр квадрата, если длина одной его стороны 7см?', '','', '28', '');

INSERT INTO tasks (`LEVEL`, `RU`, `EN`, `NL`, `RESULT`, `IMAGE`) VALUES ('task_1', '', '','', '28', '');

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
