# -*- coding:utf-8 -*-

from zipfile import ZipFile
from urllib import urlopen

def act_bootstrap_install(option,arg,setting):
    if len(arg) < 1:
        print "No filepath"

    else :
        with ZipFile(arg[0],"r") as zp:
            if "bootstrap_path" in dir(setting):
                path = setting.bootstrap_path
            else :
                path = "static/"

            namelist = zp.namelist()

            for name in namelist:
                if name.startswith(".") or name.startswith("/") :
                    namelist.remove(name)

            for name in namelist:
                print path+name

            zp.extractall(path,namelist)

def act_bootstrap_uninstall(option,arg,setting):
    import os
    if "bootstrap_path" in dir(setting):
        path = setting.bootstrap_path
    else :
        path = "static/"
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
