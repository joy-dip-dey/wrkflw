import sys
from st2common.runners.base_action import Action
from u_procs import part_of_a_day

class MyAction(Action):

    def run(self, person, ctim):
        #print('Hi ' + person + ' Good ' + part_of_a_day(ctim))
        return('Hi ' + person + ' Good ' + part_of_a_day(ctim))