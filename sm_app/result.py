from sm_app import sm_db

'''
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
'''
class Result(sm_db.Model):
    __tablename__ = 'results'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    USERID = sm_db.Column('USERID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True)
    EXECUTION_DATE = sm_db.Column('EXECUTION_DATE', sm_db.DateTime(timezone=False), nullable=False, unique=None, default=None)
    PASSED = sm_db.Column('PASSED', sm_db.Integer, nullable=False, unique=None, default=0)
    FAILED = sm_db.Column('FAILED', sm_db.Integer, nullable=False, unique=None, default=0)
    DURATION = sm_db.Column('DURATION', sm_db.String(64), nullable=False, unique=None, default='')
    PERCENT = sm_db.Column('PERCENT', sm_db.Integer, nullable=False, unique=None, default=0)
    RATE = sm_db.Column('RATE', sm_db.String(27), nullable=False, unique=None, default='')
    BELT = sm_db.Column('BELT', sm_db.String(20), nullable=False, unique=None, default='')
    TASK = sm_db.Column('TASK', sm_db.String(20), nullable=False, unique=None, default='')

    def __repr__(self):
        return '<Result {}>'.format(self.USERID)

    def get_result(self):
        return {'id': self.USERID,
            'date': self.EXECUTION_DATE,
            'passed': self.PASSED,
            'failed': self.FAILED,
            'duration': self.DURATION,
            'percent': self.PERCENT,
            'rate': self.RATE,
            'belt': self.BELT,
            'task': self.TASK,
        }
