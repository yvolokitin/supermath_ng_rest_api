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
    `BIRTHDAY` datetime NOT NULL,
    `SURNAME` varchar(64) COLLATE `utf8_general_ci` DEFAULT '',
    `EMAIL` varchar(255) COLLATE `utf8_general_ci` NOT NULL,
    `PSWDHASH` varchar(32) DEFAULT '',
    `USERGROUP` enum('GUEST', 'USER', 'PAID', 'ADMIN', 'FAKE') NOT NULL DEFAULT 'USER',
    `CREATION_DATE` datetime NOT NULL,
    `LANG` varchar(20) COLLATE `utf8_general_ci` DEFAULT 'en',
    `BELT` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    `PASSED` bigint(20) DEFAULT 0,
    `FAILED` bigint(20) DEFAULT 0,
    `AVATAR` varchar(64) COLLATE `utf8_general_ci` DEFAULT 'martin-berube',
    `SOLVED` varchar(1024) COLLATE `utf8_general_ci` DEFAULT '',
    `SUBSCR` BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (`ID`),
    UNIQUE KEY `EMAIL_IX` (`EMAIL`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;

INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`) VALUES ('Sergei', '2014-01-28 06:13:13', 'Volokitin', 'volokitin@bk.ru', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '254', '13');
INSERT INTO users (`NAME`, `BIRTHDAY`, `SURNAME`, `EMAIL`, `PSWDHASH`, `CREATION_DATE`, `PASSED`, `FAILED`) VALUES ('Roman', '2009-07-07 18:13:13', 'Volokitin', 'yuri.volokitin@bk.ru', '932dead244625bcf80d74bd69ba4f23b', '2020-01-31 13:13:13', '3', '0');

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
