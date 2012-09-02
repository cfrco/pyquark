from pyquark.database import Model,DataBase
db = DataBase("sqlite:///db.sqlite")

import model
m = Model(model,db)
m.database.echo = True

data_models = [m]
