# -*- coding:utf-8 -*-

from zipfile import ZipFile
from urllib import urlopen
from ..web.layout import replace_layout

"""
    setting file have to gived `bootstrap_path`,if user wants to use this feature.
"""
def act_bootstrap_install(option,arg,setting):
    if len(arg) == 0: filename = "bootstrap.zip"
    else : filename = arg[0]

    with ZipFile(filename,"r") as zp:
        path = setting.bootstrap_path
        namelist = zp.namelist()

        for name in namelist:
            if name.startswith(".") or name.startswith("/") :
                namelist.remove(name)

        for name in namelist:
            print path+name

        zp.extractall(path,namelist)

def act_bootstrap_uninstall(option,arg,setting):
    import os
    path = setting.bootstrap_path
    os.system("rm -rv "+path+"bootstrap")

def act_bootstrap_get(option,arg,setting):
    url = "http://twitter.github.com/bootstrap/assets/bootstrap.zip"
    print "get "+url
    req = urlopen(url)
    fp = open("bootstrap.zip","w")

    fp.write(req.read())
    fp.close()

def act_layout_file(option,arg,setting):
    for name in arg:
        if name in setting.layouts:
            setting.layouts[name].tofile()
            print "%s -> %s" %(name,setting.layouts[name].target)
        else :
            print "No layout name `%s`" % (name)

def act_layout(option,arg,setting):
    for name in arg:
        if name in setting.layouts:
            setting.layouts[name].print_text()

def act_layout_replace(option,arg,setting):
    if len(arg) != 2:
        print "Error!!"
        return 

    with open(arg[0],"r") as srcfp:
        with open(arg[1],"w") as destfp:

            for line in srcfp:
                destfp.write(replace_layout(line,setting.layouts))

    print "%s -> %s" %(arg[0],arg[1])

option_list = {
    "bootstrap-install": act_bootstrap_install,
    "bootstrap-uninstall": act_bootstrap_uninstall,
    "bootstrap-get": act_bootstrap_get,
    "layout-file" : act_layout_file,
    "layout" : act_layout,
    "layout-replace": act_layout_replace
}
