from pyquark.database import Model,DataBase

db = DataBase("sqlite:///db.sqlite")
db.echo = True

import model
import issue
data_models = [Model(model,db),Model(issue,db)]

bootstrap_path = "static/"
