# -*- coding: utf-8 -*-

from sqlalchemy import engine
from sqlalchemy import create_engine

class DataBase:
    """
        a database class for admin
    """
    def __init__(self,url):
        self.url = url
        self.auto_flush = False
        self.auto_commit = False
        self.check = True
        self.echo = False
        self.encoding = "utf-8"

        self.engine = None

    def create_engine(self):
        if self.engine == None:
            self.engine = create_engine(self.url,echo=self.echo,
                                        encoding=self.encoding)
        return self.engine

    def dispose_engine(self): 
        if self.engine:
            self.engine.dispose()
            self.engine = None

    @staticmethod
    def MySQL_URI(host,user,password,database,port=None,charset="utf-8"):
        url = "mysql://"+user+":"+password+"@"
        url += host
        if port :
            url += ":"+str(port)
        url += "/"+database
        url += "?"+"charset="+charset

        return url

class Model:
    """
        a pair of model and database
    """
    def __init__(self,module,database):
        self.module = module
        self.database = database

