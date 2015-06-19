#!/usr/bin/env python
'''Gus' commands'''

from pymavlink import mavutil
from MAVProxy.modules.lib import mp_module
from MAVProxy.modules.lib.mp_settings import MPSetting

class GusModule(mp_module.MPModule):
    def __init__(self, mpstate):
        super(GusModule, self).__init__(mpstate, "gus", "gus' commands")
        self.battery_period = mavutil.periodic_event(5)

    def mavlink_packet(self, m):
        '''handle a mavlink packet'''
        if m.get_type() == "MAV_CMD":
            print 'Command:', m.name

def init(mpstate):
    '''initialise module'''
    return GusModule(mpstate)
