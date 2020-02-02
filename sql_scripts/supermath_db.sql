﻿# mysql -uroot -pasdasd12 supermath_db;

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
    `AGE` datetime NOT NULL,
    `SURNAME` varchar(64) COLLATE `utf8_general_ci` DEFAULT '',
    `EMAIL` varchar(255) COLLATE `utf8_general_ci` NOT NULL,
    `PSWD` varchar(35) COLLATE `utf8_general_ci` NOT NULL,
    `PSWDHASH` varchar(32) DEFAULT '',
    `USERGROUP` enum('GUEST', 'USER', 'PAID', 'ADMIN', 'FAKE') NOT NULL DEFAULT 'GUEST',
    `CREATION_DATE` datetime NOT NULL,
    `PROGRAM` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    `BELT` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    `PASS` bigint(20) DEFAULT 0,
    `FAIL` bigint(20) DEFAULT 0,
    `AVATAR` varchar(64) COLLATE `utf8_general_ci` DEFAULT 'martin-berube',
    PRIMARY KEY (`ID`),
    UNIQUE KEY `EMAIL_IX` (`EMAIL`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;

INSERT INTO users (`NAME`, `AGE`, `SURNAME`, `EMAIL`, `PSWD`, `PSWDHASH`, `CREATION_DATE`) VALUES ('Sergey', '2014-01-28 06:13:13', 'Volokitin', 'volokitin@bk.ru', 'asdas12', '123456', '2020-01-31 13:13:13');
INSERT INTO users (`NAME`, `AGE`, `SURNAME`, `EMAIL`, `PSWD`, `PSWDHASH`, `CREATION_DATE`) VALUES ('Roman', '2009-07-07 18:13:13', 'Volokitin', 'yuri.volokitin@bk.ru', 'asdas12', '123456', '2020-01-31 13:13:13');
