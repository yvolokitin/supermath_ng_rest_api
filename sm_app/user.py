from sm_app import sm_db

'''
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
'''
class User(sm_db.Model):
    __tablename__ = 'users'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True)
    NAME = sm_db.Column('NAME', sm_db.String(20), nullable=False, unique=None, default=None)
    LANG = sm_db.Column('LANG', sm_db.String(20), nullable=False, unique=None, default=None)
    AGE = sm_db.Column('AGE', sm_db.DateTime(timezone=False), nullable=False, unique=None, default=None)
    SURNAME = sm_db.Column('SURNAME', sm_db.String(64), nullable=False, unique=None, default='')
    EMAIL = sm_db.Column('EMAIL', sm_db.String(255), nullable=False, unique=True, default=None)
    PSWD = sm_db.Column('PSWD', sm_db.String(35), nullable=False, unique=None, default=None)
    PSWDHASH = sm_db.Column('PSWDHASH', sm_db.String(32), nullable=False, unique=None, default='')
    USERGROUP = sm_db.Column("USERGROUP", sm_db.Enum('GUEST','USER','PAID','ADMIN','FAKE'), nullable=False, unique=None, default='GUEST')
    CREATION_DATE = sm_db.Column('CREATION_DATE', sm_db.DateTime(timezone=False), nullable=False, unique=None, default=None)
    PROGRAM = sm_db.Column('PROGRAM', sm_db.String(20), nullable=False, unique=None, default='')
    BELT = sm_db.Column('BELT', sm_db.String(20), nullable=False, unique=None, default='')
    PASS = sm_db.Column('PASS', sm_db.BigInteger(), nullable=False, unique=None, default=0)
    FAIL = sm_db.Column('FAIL', sm_db.BigInteger(), nullable=False, unique=None, default=0)
    AVATAR = sm_db.Column('AVATAR', sm_db.String(64), nullable=False, unique=None, default='martin-berube')

    def __repr__(self):
        return '<User {}>'.format(self.NAME)
