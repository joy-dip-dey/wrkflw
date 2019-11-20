import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, nam):
        return(nam)