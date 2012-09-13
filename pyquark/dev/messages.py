#-*- coding:utf-8 -*-

from flask import flash

class DoingError(Exception):
    pass

class MessageHub:
    """
        hub = MessageHub()
        hub.check(user.set_name(....),False,set_name_error_message,"error")
        # when user.set_name(...) == False => 
        # (set_name_error_message,"error") will be push into hub

        if hub.has_error():
            #do_things
            hub.flash_message() # for flask flash
            return render_template(....)

        #or

        hub = MessageHub(raise_error=True)
        try:
            hub.check(user.set_name(....),False,set_name_error_message,"error")
            #others...
        except DoingError:
            #do_things
            #db_session.rollback()
            #....
    """
    def __init__(self,raise_error=False):
        self.messages = []
        self.counter = {"error":0,"success":0,"info":0}
        self.raise_error = raise_error

    def push(self,message,state):
        self.messages += [(message,state)]

        if state in self.counter:
            self.counter[state] += 1
        else :
            self.counter[state] = 1
    
    def check(self,do,bol,message,state):
        """
            when `do` == `bol` ,`message` will be added to `self.messages`
        """
        if do == bol:
            self.push(message,state)
            
            if state == "error":
                raise DoingError(message)

    def has_error(self):
        return self.counter["error"] > 0

    def has_state(self,state):
        if state in self.counter:
            return self.counter[state] > 0
        else :
            return False

    def flash_message(self,filter=None):
        """
            flash_message() # push all messages
            flash_message(filter=["success"]) # push `success` messafes
        """
        if filter == None:
            for message in self.messages:
                flash(message[0],message[1])
        else :
            for message in self.messages:
                if message[1] in filter:
                    flash(message[0],message[1])
