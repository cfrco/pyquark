# -*- coding:utf-8 -*-

import re
UserID_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*$")
NetMail_regex = re.compile("^[a-zA-z][-._a-zA-Z0-9]*@((?:(?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9])\\.)+[a-zA-Z][a-zA-Z]+$)")
NetHostname_regex = re.compile("^((?:(?:[a-zA-Z]|[a-zA-Z][-a-zA-Z0-9]*[a-zA-Z0-9]\\.))+[a-zA-Z][a-zA-Z]+$)")

HttpUrl_regex = re.compile("(https?://(?:[a-z]|[a-z0-9][-a-z0-9]*[a-z0-9]\\.)+[a-z][a-z]+(?::\\d+)?"
"(?:/[^.!,?;\"'<>()\\[\\]{}\\s\\x7F-\\xFF]*(?:[.!,?]+[^.!,?;\"'<>()\[\]{}\\s\\x7F-\\xFF]+)*)?)",re.I)
# from Mastering Regular Expressions, 3rd ed.


class Html:
    @staticmethod
    def UrlActive(text):
        return HttpUrl_regex.sub("<a href=\"\\1\">\\1</a>",text)
