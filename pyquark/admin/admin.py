#!/usr/bin/env python2.7
# -*- coding:utf-8 -*-

from optparse import OptionParser
import imp

import database

option_list = {
    "database":database        
}
def opt_get():
    parser = OptionParser()
    parser.add_option("-f","--file",action="store",default="setting.py",
                      type="string",dest="filename")

    return parser.parse_args()

def main(): 
    option,arg = opt_get()
    setting = imp.load_source('quark_setting_file',option.filename)
    
    if arg[0] in option_list:
        name = arg.pop(0)
        if arg[0] in option_list[name].option_list:
            action = arg.pop(0)
            option_list[name].option_list[action](option,arg,setting)
        else :
            print 'No this action `'+arg[0]+'`.'
    else :
        print 'No `'+arg[0]+'`.'
        
if __name__ == '__main__':
    main()
