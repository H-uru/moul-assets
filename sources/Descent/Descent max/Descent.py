"""
Module: Descent.py
Age: Descent
Date: January 2004
Event Manager hooks for Descent
"""

from Plasma import *
from PlasmaTypes import *
from PlasmaVaultConstants import *

class Descent(ptResponder):

    def __init__(self):
        ptResponder.__init__(self)
        self.id = 5325
        self.version = 1

    def OnServerInitComplete(self):
        self.ICityBookLink()

    def OnVaultNotify(self,type,tupdata):
        # was an owned age just added?
        if type == PtVaultNotifyTypes.kRegisteredOwnedAge:
            link = tupdata[0]
            name = link.getAgeInfo().getAgeFilename()
            if name == "Descent":
                cityBookSP = ptSpawnPointInfo("dsntShaftFall","LinkInPointShaftFall")
                link.addSpawnPoint(cityBookSP)
                link.save()
                PtDebugPrint("Descent - setting the spawnpoint for the city book - OnVaultNotify",level=kDebugDumpLevel)
            else:
                PtDebugPrint("Descent - registering age '%s' (why is this not Descent?)"%(name))
        else:
            PtDebugPrint("Descent:OnVaultNotify - not what we want - type=%d"%(type),level=kDebugDumpLevel)

    def ICityBookLink(self):
        vault = ptVault()
        folder = vault.getAgesIOwnFolder()
        contents = folder.getChildNodeRefList()
        for content in contents:
            link = content.getChild()
            link = link.upcastToAgeLinkNode()
            name = link.getAgeInfo().getAgeFilename()
            if name == "Descent":
                cityBookSP = ptSpawnPointInfo("dsntShaftFall","LinkInPointShaftFall")
                link.addSpawnPoint(cityBookSP)
                link.save()
                PtDebugPrint("Descent:OnServerInitComplete - setting the spawnpoint for the city book",level=kDebugDumpLevel)
                return
        PtDebugPrint("Descent:OnServerInitComplete - error - Descent is not there... hopefully OnVaultNotify catches it")
        return
