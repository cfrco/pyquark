# -*- coding: utf-8 -*-

from optparse import OptionParser

def act_create_all(option,arg,setting):
    for mod in setting.data_models:
        create_model(mod)

def act_drop_all(option,arg,setting):
    for mod in setting.data_models:
        drop_model(mod)

def act_reset_all(option,arg,setting):
    for mod in setting.data_models:
        reset_model(mod)

def act_create(option,arg,setting):
    for model_name in arg:
        mod = find_model(setting.data_models,model_name)
        create_model(mod)

def act_drop(option,arg,setting):
    for model_name in arg:
        mod = find_model(setting.data_models,model_name)
        drop_model(mod)

def act_reset(option,arg,setting):
    for model_name in arg:
        mod = find_model(setting.data_models,model_name)
        reset_model(mod)

def create_model(mod):
    mod.database.create_engine()
    mod.module.Base.metadata.\
            create_all(mod.database.engine,
                       checkfirst=mod.database.check)
    mod.database.dispose_engine()

def drop_model(mod):
    mod.database.create_engine()
    mod.module.Base.metadata.\
            drop_all(mod.database.engine,
                       checkfirst=mod.database.check)
    mod.database.dispose_engine()

def reset_model(mod):
    mod.database.create_engine()
    mod.module.Base.metadata.\
            drop_all(mod.database.engine,
                       checkfirst=mod.database.check)
    mod.module.Base.metadata.\
            create_all(mod.database.engine,
                       checkfirst=mod.database.check)
    mod.database.dispose_engine()

def find_model(models,name):
    for model in models:
        if model.module.ModelName == name :
            return model
    return None

option_list = {
    "create" : act_create,
    "drop" : act_drop,
    "reset" : act_reset,
    "create-all" : act_create_all,
    "drop-all" : act_drop_all,
    "reset-all" : act_reset_all
}

if __name__ == "__main__":
    pass
