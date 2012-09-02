# -*- coding:utf-8 -*-

"""
    It's a base for database's models(tables)

    `from pyquark.modelbase import *`
"""

from sqlalchemy import MetaData
from sqlalchemy import Table,Column,Integer,String,Text
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

#Base = declarative_base()

def get_base():
    return declarative_base()

def table_name(mod,name):
    return mod+"_"+name
