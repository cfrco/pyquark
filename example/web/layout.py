from pyquark.web.layout import Layout
from pyquark.web.form import *

form = Form()
form.append(StringField("user","Type User Name ..."))
form.append(PasswordField("password","Type Password ..."))
form.append(PasswordField("password_check","Type Password againg ..."))
form.append(TextField("bio","Type your biography ...",attrs={"class":"span12"}))

layouts = {
    "index":Layout("templates/index.html","main","starter",
        {
            "lang":"en",
            "charset":"utf-8",
            "title":"Test",
            "bootstrap_css":"../static/bootstrap/css/bootstrap.min.css",
            "bootstrap_js":"../static/bootstrap/js/bootstrap.min.js"
        }
    ),

    "form-new-user": form
}
