from sm_app import sm_db

'''
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
'''
class User(sm_db.Model):
    __tablename__ = 'users'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True)
    NAME = sm_db.Column('NAME', sm_db.String(20), nullable=False, unique=None, default=None)
    BIRTHDAY = sm_db.Column('BIRTHDAY', sm_db.DateTime(timezone=False), nullable=False, unique=None, default=None)
    SURNAME = sm_db.Column('SURNAME', sm_db.String(64), nullable=False, unique=None, default='')
    EMAIL = sm_db.Column('EMAIL', sm_db.String(255), nullable=False, unique=True, default=None)
    PSWDHASH = sm_db.Column('PSWDHASH', sm_db.String(32), nullable=False, unique=None, default='')
    USERGROUP = sm_db.Column("USERGROUP", sm_db.Enum('GUEST','USER','PAID','ADMIN','FAKE'), nullable=False, unique=None, default='GUEST')
    CREATION_DATE = sm_db.Column('CREATION_DATE', sm_db.DateTime(timezone=False), nullable=False, unique=None, default=None)
    LANG = sm_db.Column('LANG', sm_db.String(20), nullable=False, unique=None, default=None)
    BELT = sm_db.Column('BELT', sm_db.String(20), nullable=False, unique=None, default='')
    PASSED = sm_db.Column('PASSED', sm_db.BigInteger(), nullable=False, unique=None, default=0)
    FAILED = sm_db.Column('FAILED', sm_db.BigInteger(), nullable=False, unique=None, default=0)
    AVATAR = sm_db.Column('AVATAR', sm_db.String(64), nullable=False, unique=None, default='martin-berube')
    SOLVED = sm_db.Column('SOLVED', sm_db.String(1024), nullable=False, unique=None, default='')
    SUBSCR = sm_db.Column('SUBSCR', sm_db.Boolean(), nullable=False, unique=None, default=False)

    def __repr__(self):
        return '<User {}>'.format(self.NAME)

    def get_userinfo(self):
        return {'id': self.ID, 'name': self.NAME, 'surname': self.SURNAME, 'passed': self.PASSED, 'failed': self.FAILED}
