from sm_app import sm_db

'''
CREATE TABLE `solved` (
    `ID` bigint(20) NOT NULL auto_increment,
    `USERID` bigint(20) NOT NULL,
    `GAMEID` int DEFAULT 0,
    `BELT` varchar(20) COLLATE `utf8_general_ci` DEFAULT '',
    PRIMARY KEY (`ID`),
    FOREIGN KEY (USERID) REFERENCES `users` (`ID`)
) ENGINE=MyISAM DEFAULT CHARACTER SET `utf8` COLLATE=utf8_general_ci AUTO_INCREMENT=1;
'''
class Solved(sm_db.Model):
    __tablename__ = 'solved'
    __table_args__ = {'useexisting': True}

    ID = sm_db.Column('ID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True, autoincrement=True)
    USERID = sm_db.Column('USERID', sm_db.BigInteger(), nullable=False, unique=None, default=None, primary_key=True)
    GAMEID = sm_db.Column('GAMEID', sm_db.Integer, nullable=False, unique=None, default=0)
    BELT = sm_db.Column('BELT', sm_db.String(20), nullable=False, unique=None, default='')

    def __repr__(self):
        return '<Solved {}>'.format(self.USERID)
