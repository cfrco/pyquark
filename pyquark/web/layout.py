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
            


class Content:
    def __init__(self,d):
        self._d = d

    def __getattr__(self,name):
        if name in self._d:
            return self._d[name]
        return ""
