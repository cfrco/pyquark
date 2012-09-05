# -*- coding:utf-8 -*-

import re
UserID_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*$")
NetMail_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*@((?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.)*[a-zA-Z][a-zA-Z]+$)")

class User:
    @staticmethod
    def checkID(str_id,minlen=1,maxlen=50):
        str_id = str_id.strip()     #remove space
        strlen = len(str_id)

        if strlen < minlen or strlen > maxlen :
            return False
        
        return UserID_regex.match(str_id)!=None

    @staticmethod
    def checkMail(str_mail):
        str_mail = str_mail.strip()

        res = NetMail_regex.match(str_mail)
        
        # May should add more limition
        if res :
            return True
        return False
