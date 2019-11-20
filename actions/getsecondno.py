import sys
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, inp2):
        return(inp2)