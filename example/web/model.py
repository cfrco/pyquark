from pyquark.modelbase import *

Base = get_base()
ModelName = "test"
TableArgs = {}
#TableArgs = {'mysql_engine':'InnoDB','mysql_charset':'utf8'}

class User(Base):
    __tablename__ = table_name(ModelName,"user")
    __table_args__ = TableArgs

    id = Column(Integer,primary_key=True)
    name = Column(String(30))

