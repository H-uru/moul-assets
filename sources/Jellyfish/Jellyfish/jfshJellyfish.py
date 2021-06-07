"""
Module: jfshJellyfish
Age: Jellyfish
Date: May 2006
Author: Derek Odell
Jellyfish Logic
"""

from Plasma import *
from PlasmaTypes import *

# define the attributes that will be entered in max #
#---------------------------------------------------#
collectorGoal01             = ptAttribActivator(1, "Jellyfish Goal 01")

# globals #
#---------#


#=============================================================================================

class jfshJellyfish(ptResponder):
    ###########################
    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5341
        self.version = 1
        print "jfshJellyfish: init version = %d" % self.version

    ###########################
    def OnFirstUpdate(self):
        "Nothing Here"

    ###########################
    def OnServerInitComplete(self):
        "Nothing Here"

    ###########################
    def OnNotify(self,state,id,events):
        if id == collectorGoal01.id:
            print "GOOOOOOOOAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL!"
            