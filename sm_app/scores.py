from sm_app import sm_db

'''
CREATE TABLE `scores` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `SCORE` bigint(20) NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;
'''
class Scores(sm_db.Model):
    __tablename__ = 'scores'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    USERID = sm_db.Column('USERID', sm_db.BigInteger(), nullable=False, unique=None, default=None)
    SCORE = sm_db.Column('SCORE', sm_db.BigInteger(), nullable=False, unique=None, default=None)

    def __repr__(self):
        return '<Solved {}>'.format(self.USERID)
