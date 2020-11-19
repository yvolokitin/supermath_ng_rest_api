from sm_app import sm_db

'''
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
'''
class Tasks(sm_db.Model):
    __tablename__ = 'tasks'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    LEVEL = sm_db.Column('LEVEL', sm_db.String(8), nullable=False, unique=None, default='task_1')

    RU = sm_db.Column('RU', sm_db.String(512), nullable=False, unique=None, default='')
    EN = sm_db.Column('EN', sm_db.String(512), nullable=False, unique=None, default='')
    NL = sm_db.Column('NL', sm_db.String(512), nullable=False, unique=None, default='')
    DE = sm_db.Column('DE', sm_db.String(512), nullable=False, unique=None, default='')
    FR = sm_db.Column('FR', sm_db.String(512), nullable=False, unique=None, default='')
    ES = sm_db.Column('ES', sm_db.String(512), nullable=False, unique=None, default='')
    IT = sm_db.Column('IT', sm_db.String(512), nullable=False, unique=None, default='')

    RESULT = sm_db.Column('RESULT', sm_db.String(32), nullable=False, unique=None, default=None)
    IMAGE = sm_db.Column('IMAGE', sm_db.String(64), nullable=False, unique=None, default='')
