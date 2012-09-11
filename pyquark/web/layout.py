# -*- coding:utf-8 -*-

class Layout:
    def __init__(self,target,sketon,name,content):
        self.target = target
        self.content = content
        self.sketon = sketon
        self.name = name

    def tofile(self,filename=None):
        if filename == None:
            filename = self.target

        with open(filename,"w") as fp:
            fp.write(self.out())

    def print_text(self):
        print self.out()

    def out(self):
        if self.sketon == "main":
            from .layout_main import template
            return template[self.name].format(Content(self.content))

    def __str__(self):
        return self.out()
            


class Content:
    def __init__(self,d):
        self._d = d

    def __getattr__(self,name):
        if name in self._d:
            return self._d[name]
        return ""

def replace_layout(text,layouts):
    import re
    target_re = re.compile("<@\\s*([^\\s\\n@>]+)\\s*@>")

    res = target_re.search(text)

    while res != None:
        name = res.group(1)
        print name
        print res.groups()
        if name in layouts :
            text = text[:res.start(0)]+str(layouts[name])+text[res.end(0):]
        else :
            text = text[:res.start(0)]+" "+text[res.end(0):]

        res = target_re.search(text)
    
    return text
