# -*- coding:utf-8 -*-

import re
UserID_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*$")
NetMail_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*@((?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.)*[a-zA-Z][a-zA-Z]+$)")
NetHostname_regex = re.compile("^((?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.)*[a-zA-Z][a-zA-Z]+$)")

