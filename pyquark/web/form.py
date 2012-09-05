# -*- coding:utf-8 -*-

class Form:
    def __init__(self,method="POST",action="",clas=""):
        self.method = method
        self.action = action
        self.clas = clas
        self.fields = []

    def append(self,field):
        self.fields.append(field)

    def insert(self,index,field):
        self.fields.insert(index,field)

    def __str__(self):
        out = "<form method=\"%s\" action=\"%s\" class=\"%s\">\n" %\
                (self.method,self.action,self.clas)

        for field in self.fields:
            out += "    "+str(field)

        out += "</form>"
        return out

def InputField(itype,name,placeholder="",br=True,attrs={}):
    out = "<input type=\"%s\" name=\"%s\" placeholder=\"%s\" " %\
            (itype,name,placeholder)
    for k,v in attrs.items():
        out += k+"=\"%s\" " % (v)

    out += ">"
    if br:
        out += "<br/>"
    out += "\n"
    return out

def StringField(name,placeholder="",br=True,attrs={}):
    return InputField("text",name,placeholder,br,attrs)

def PasswordField(name,placeholder="",br=True,attrs={}):
    return InputField("password",name,placeholder,br,attrs)

def TextField(name,placeholder="",rows=5,content="",br=True,attrs={}):
    out = "<textarea name=\"%s\" rows=\"%d\" placholder=\"%s\" " %\
            (name,rows,placeholder)

    for k,v in attrs.items():
        out += k+"=\"%s\" " % (v)

    out += ">"+content+"</textarea>"

    if br:
        out += "<br/>"
    out += "\n"
    return out
