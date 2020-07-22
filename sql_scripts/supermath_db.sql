# mysql -uroot -pasdasd12 supermath_db;

# fix troubles with localhost root access
# ALTER USER 'root'@'localhost' IDENTIFIED BY 'asdasd12';
# UPDATE mysql.user SET authentication_string = PASSWORD('asdasd12') WHERE User = 'root';
# GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost';

# SET CHARACTER SET utf8;
# CREATE DATABASE supermath_db;
CREATE DATABASE `supermath_db` CHARACTER SET `utf8` COLLATE `utf8_general_ci`;

# Table structure `users`
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
    `ID` bigint(20) NOT NULL auto_increment,
    `NAME` varchar(64) COLLATE `utf8_general_ci` NOT NULL,
    `BIRTHDAY` varchar(64) COLLATE `utf8_general_ci` NOT NULL,
    `EMAIL` varchar(255) COLLATE `utf8_general_ci` NOT NULL,
    `SURNAME` varchar(64) COLLATE `utf8_general_ci` DEFAULT '',
    `PSWDHASH` varchar(32) DEFAULT '',
    `USERGROUP` enum('GUEST', 'USER', 'PAID', 'ADMIN', 'FAKE') NOT NULL DEFAULT 'USER',
    `CREATION_DATE` datetime NOT NULL,
    `LANG` varchar(20) COLLATE `utf8_general_ci` DEFAULT 'en',
    `BELT` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    `PASSED` bigint(20) DEFAULT 0,
    `FAILED` bigint(20) DEFAULT 0,
    `CARDS` int(20) DEFAULT 0,
    `AVATAR` varchar(64) COLLATE `utf8_general_ci` DEFAULT 'martin',
    `SOLVED` varchar(1024) COLLATE `utf8_general_ci` DEFAULT '',
    `SUBSCR` BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (`ID`),
    UNIQUE KEY `EMAIL_IX` (`EMAIL`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;

INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Sergei', '2014-01-28', 'Volokitin', 'volokitin@bk.ru', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '233', '0', '6', 'white1,white2,white3,white4,white6,white8,white5,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Roman', '2009-07-07', 'Volokitin', 'yuri.volokitin@bk.ru', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '390', '0', '15', 'white1,white2,white3,white4,white5,white6,white7,white8,white9,orange1,navy1,navy2,navy3,orange2,orange3,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Hem', '2010-09-13', 'Subbaiyan', 'Alisha@lb.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '326', '8', '4', 'white1,white2,white3,white4,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Jash', '2010-09-13', 'Solomon', 'Jash@lb.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '518', '2', '4', 'white1,white2,white3,white4,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Kashvi', '2010-09-13', 'Singh', 'Kashvi@lg.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '666', '6', '4', 'white1,white2,white3,white4,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Ananya', '2010-10-18', 'Singh', 'Ananya@lg.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '684', '9', '4', 'white1,white2,white3,white4,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Pavati', '2010-07-02', 'Gnanasundar', 'Pavati@lb.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '315', '2', '4', 'white1,white2,white3,white4,');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`, `CARDS`, `SOLVED`) VALUES ('Taara', '2010-07-02', 'Patel', 'Taara@lb.com', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '615', '11', '4', 'white1,white2,white3,white4,');


DROP TABLE IF EXISTS `results`;
CREATE TABLE `results` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `EXECUTION_DATE` datetime NOT NULL,
    `PASSED` int DEFAULT 0,
    `FAILED` int DEFAULT 0,
    `DURATION` varchar(64) COLLATE `utf8_general_ci` DEFAULT '',
    `PERCENT` int DEFAULT 0,
    `RATE` varchar(27),
    `BELT` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    `TASK` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;

DROP TABLE IF EXISTS `friends`;
CREATE TABLE `friends` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `FRIENDID` bigint(20) NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`),
    FOREIGN KEY (FRIENDID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;


DROP TABLE IF EXISTS `scores`;
CREATE TABLE `scores` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `SCORE` bigint(20) NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;

DROP TABLE IF EXISTS `tasks`;
CREATE TABLE `tasks` (
    `ID` bigint(20) NOT NULL auto_increment,
    `LANG` varchar(3) NOT NULL,
    `LEVEL` varchar(32) DEFAULT '',
    `DESCRIPTION` varchar(1024) NOT NULL,
    `RESULT` varchar(128) NOT NULL,
    `UNITS` varchar(128) DEFAULT '',
    `IMAGE` varchar(128) DEFAULT '',
    PRIMARY KEY (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET utf8 COLLATE=utf8_general_ci AUTO_INCREMENT=1;

INSERT INTO tasks (`LEVEL`, `LANG`, `DESCRIPTION`, `RESULT`) VALUES ('task_1', 'ru', 'Вычисли разность 52 и 19', '33');

SELECT * FROM tasks ORDER BY RAND() LIMIT 1;
