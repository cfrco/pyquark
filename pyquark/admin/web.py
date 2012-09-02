# -*- coding:utf-8 -*-

from zipfile import ZipFile
from urllib import urlopen

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

option_list = {
    "bootstrap-install": act_bootstrap_install,
    "bootstrap-uninstall": act_bootstrap_uninstall,
    "bootstrap-get": act_bootstrap_get
}
