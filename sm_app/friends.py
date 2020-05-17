from sm_app import sm_db

'''
CREATE TABLE `friends` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `FRIENDID` bigint(20) NOT NULL,
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`),
    FOREIGN KEY (FRIENDID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;
'''
class Friends(sm_db.Model):
    __tablename__ = 'solved'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    USERID = sm_db.Column('USERID', sm_db.BigInteger(), nullable=False, unique=None, default=None)
    FRIENDID = sm_db.Column('FRIENDID', sm_db.BigInteger(), nullable=False, unique=None, default=None)

    def __repr__(self):
        return '<Solved {}>'.format(self.USERID)
