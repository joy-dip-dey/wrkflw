import sys
import datetime
from st2common.runners.base_action import Action
from u_procs import part_of_a_day

class MyAction(Action):

    def run(self, person):
        timenow = datetime.datetime.now()
        hrofdy = timenow.hour
        return('Hi ' + person + ' Good ' + part_of_a_day(hrofdy))