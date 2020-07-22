from sm_app import sm_db

'''
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
'''
class Tasks(sm_db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    LANG = sm_db.Column('LANG', sm_db.String(3), nullable=False, unique=None, default=None)
    LEVEL = sm_db.Column('LEVEL', sm_db.String(32), nullable=False, unique=None, default='')
    DESCRIPTION = sm_db.Column('DESCRIPTION', sm_db.String(1024), nullable=False, unique=None, default=None)
    RESULT = sm_db.Column('RESULT', sm_db.String(128), nullable=False, unique=None, default=None)
    UNITS = sm_db.Column('UNITS', sm_db.String(128), nullable=False, unique=None, default='')
    IMAGE = sm_db.Column('IMAGE', sm_db.String(128), nullable=False, unique=None, default='')
