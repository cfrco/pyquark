from pyquark.web.layout import Layout

layouts = {
    "index":Layout("templates/index.html","main","starter",
        {
            "lang":"en",
            "charset":"utf-8",
            "title":"Test",
            "bootstrap_css":"../static/bootstrap/css/bootstrap.min.css",
            "bootstrap_js":"../static/bootstrap/js/bootstrap.min.js"
        }
    )
}
