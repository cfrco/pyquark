# -*- coding:utf-8 -*-

"""
starter:
    lang
    charset
    title
    bootstrap_css
    bootstrap_js
    navbar_class
    container_class
"""

template = {
"starter":
"""
<!DOCTYPE html>
<html lang="{0.lang}">
    <head>
        <meta charset="{0.charset}">
        <title>{0.title}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="description" content="">
        <meta name="author" content="">

        <!-- Le styles -->
        <link href="{0.bootstrap_css}" rel="stylesheet">
        <style>
            body {{
                padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
            }}
        </style>

        <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
        <!--[if lt IE 9]>
        <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
        <![endif]-->
    </head>

    <body>

        <div class="navbar {0.navbar_class}">
        </div>
        <div class="container {0.container_class}">
        </div>

        <!-- Placed at the end of the document so the pages load faster -->
        <script src="{0.bootstrap_js}"></script>

    </body>
</html>

<style>
</style>
"""
}
