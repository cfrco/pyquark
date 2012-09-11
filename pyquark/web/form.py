# -*- coding:utf-8 -*-

class Form:
    def __init__(self,method="POST",action="",clas="",fields=None):
        self.method = method
        self.action = action
        self.clas = clas
        self.target = ""
        if fields != None:
            self.fields = fields

    def append(self,field):
        self.fields.append(field)

    def insert(self,index,field):
        self.fields.insert(index,field)

    def print_text(self):
        print str(self)

    def tofile(self,filename=None):
        if filename == None:
            filename = self.target

        with open(filename,"w") as fp:
            fp.write(str(self))

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

def SelectField(name,options,multiple=False,br=True,attrs={}):
    out = "<select name=\"%s\" " % name
    
    if multiple :
        out += "multiple=\"multiple\" "
    
    for k,v in attrs.items():
        out += k+"=\"%s\" " % (v)

    out += ">\n"

    if isinstance(options,dict):
        for k,v in options.items():
            out += "<option value=\"%s\">%s</option>\n" % (k,v)

    else :
        for v in options:
            out += "<option>%s</option>\n" % v

    out +=  "</select>"
    return out

def PreApp(inputfield,pre=None,app=None):
    """
        this is for bootstrap
    """
    out = "<div class=\""
    
    if pre :
        out += " input-prepend "
    if app :
        out += " input-append "

    out += "\">"
    
    if pre :
        out += "<span class=\"add-on\">%s</span>" % pre
    out += inputfield
    if app :
        out += "<span class=\"add-on\">%s</span>" % app
    out += "</div>"

    return out
   
