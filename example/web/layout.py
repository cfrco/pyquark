from pyquark.web.form import *

form = Form()
form.append(StringField("user","Type User Name ..."))
form.append(PasswordField("password","Type Password ..."))
form.append(PasswordField("password_check","Type Password againg ..."))
form.append(TextField("bio","Type your biography ...",attrs={"class":"span12"}))

layouts = {
    "form-new-user": form
}
