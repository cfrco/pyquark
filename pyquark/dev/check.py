# -*- coding:utf-8 -*-

import re
UserID_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*$")
NetMail_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*@((?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.)*[a-zA-Z][a-zA-Z]+$)")
NetHostname_regex = re.compile("^((?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.)*[a-zA-Z][a-zA-Z]+$)")

LowerSet = set("abcdefghijklmnopqrstuvwxyz")
UpperSet = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
DigitSet = set("0123456789")
OtherSet = set("-+=_*~.")

class User:
    @staticmethod
    def checkID(str_id,minlen=1,maxlen=20):
        str_id = str_id.strip()     #remove space
        strlen = len(str_id)

        if strlen < minlen or strlen > maxlen :
            return None
        
        if UserID_regex.match(str_id) != None:
            return str_id

    @staticmethod
    def checkMail(str_mail):
        str_mail = str_mail.strip()

        res = NetMail_regex.match(str_mail)
        
        # May should add more limition
        if res :
            return str_mail
        return None

    @staticmethod
    def checkPassword(str_password,minlen=5,maxlen=20,level=0):
        if str_password != str_password.strip():
            return None
        
        strlen = len(str_password)

        if strlen < minlen or strlen > maxlen :
            return None
        
        lower = 0
        upper = 0
        digit = 0
        other = 0

        for c in str_password:
            if c in LowerSet:
                lower += 1
            elif c in UpperSet:
                upper += 1
            elif c in DigitSet:
                digit += 1
            elif c in OtherSet:
                other += 1
            else :
                return None

        if level == 0:
                return str_password

        #have letter and digit
        elif level == 1:
            if (lower>0 or upper>0) and digit>0:
                return str_password

        #have upper and lower letter and digit
        elif level == 2:
            if lower>0 and upper>0 and digit>0:
                return str_password

        #have upper and lower letter and digit and others
        elif level == 4:
            if lower>0 and upper>0 and digit>0 and other>0:
                return str_password

        return None
