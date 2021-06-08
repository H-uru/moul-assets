"""
Module: jfshPlasmaGun
Age: Jellyfish
Date: May 2006
Original Authors: Mark DeForest, Bill Slease, Doug McBride
h4x0r3d by: Derek Odell
Plasma gun used to shoot jellyfishes
"""

from Plasma import *
from PlasmaTypes import *
from PlasmaKITypes import *
import PlasmaControlKeys
import string

# define the attributes that will be entered in max #
#---------------------------------------------------#
clkActivateGun          = ptAttribActivator(1, "click: Use Plasmagun")
camGunHUD               = ptAttribSceneobject(2, "cam: Plasmagun HUD cam")
Behavior                = ptAttribBehavior(3, "Plasmagun behavior (multistage)")
dlgGunHUD               = ptAttribString(4, "string: Plasmagun HUD dlg")
animGunRotate           = ptAttribAnimation(5, "anim: Gun Rotate")
animGunPitch            = ptAttribAnimation(6, "anim: Gun Pitch")
respShootGun            = ptAttribResponder(7, "resp: ShootVapor")
objBullet01             = ptAttribSceneobject(8, "obj: Bullet01")
objBullet02             = ptAttribSceneobject(9, "obj: Bullet02")
objBullet03             = ptAttribSceneobject(10, "obj: Bullet03")
objBullet04             = ptAttribSceneobject(11, "obj: Bullet04")
objBullet05             = ptAttribSceneobject(12, "obj: Bullet05")
objBulletSpawn          = ptAttribSceneobject(13, "obj: Bullet Spawn")

# constants #
#-----------#
kLeftScopeBtn           = 36
kRightScopeBtn          = 37
kUpScopeBtn             = 38
kDownScopeBtn           = 39
kFireScopeBtn           = 40
kExitButton             = 199

kTimerDisengage         = 1
kTimerDisengageTime     = 3
kTimerThrottleFiring    = 2
kTimerThrottleTime      = 0.25

# globals #
#---------#
gThrottleShooting       = 0
LocalAvatar             = None
boolScopeOperator       = 0
boolOperated            = 0
gBulletNum              = 1

#=============================================================================================

class jfshPlasmaGun(ptModifier):
    ###########################
    def __init__(self):
        ptModifier.__init__(self)
        self.id = 5342
        self.version = 1
        print "jfshPlasmaGun: init version = %d" % self.version

    ###########################
    def OnFirstUpdate(self):
        "Nothing Here"

    ###########################
    def OnServerInitComplete(self):
        "Nothing Here"

    ###########################
    def AvatarPage(self, avObj, pageIn, lastOut):
        "Nothing Here"
            
    ###########################
    def __del__(self):
        if type(dlgGunHUD.value) != type(None) and dlgGunHUD.value != "":
            PtUnloadDialog(dlgGunHUD.value)

    ###########################
    def OnNotify(self,state,id,events):
        global LocalAvatar
        global boolScopeOperator

        if state and id == clkActivateGun.id and PtWasLocallyNotified(self.key):
            LocalAvatar = PtFindAvatar(events)
            self.IStartTelescope()

        # Dunno what this is for
        for event in events:
            if event[0] == kMultiStageEvent and event[1] == 0 and event[2] == kAdvanceNextStage:
                if boolScopeOperator:
                    self.IEngageTelescope()
                    boolScopeOperator = 0
                break

    ###########################
    def OnGUINotify(self,id,control,event):
        global gThrottleShooting

        if event == kDialogLoaded:
            control.show()
        elif event == kAction:
            if type(control) != type(None):
                btnID = control.getTagID()
                if btnID == kLeftScopeBtn:
                    if isinstance(control,ptGUIControlButton) and control.isButtonDown():
                        print "jfshPlasmaGun: GUINotify Left button down"
                        animGunRotate.value.backwards(0)
                        animGunRotate.value.resume()
                    else:
                        print "jfshPlasmaGun: GUINotify Left button up"
                        animGunRotate.value.stop()
                elif btnID == kRightScopeBtn:
                    if isinstance(control,ptGUIControlButton) and control.isButtonDown():
                        print "jfshPlasmaGun: GUINotify Right button down"
                        animGunRotate.value.backwards(1)
                        animGunRotate.value.resume()
                    else:
                        print "jfshPlasmaGun: GUINotify Right button up"
                        animGunRotate.value.stop()
                elif btnID == kUpScopeBtn:
                    if isinstance(control,ptGUIControlButton) and control.isButtonDown():
                        print "jfshPlasmaGun: GUINotify Up button down"
                        animGunPitch.value.backwards(0)
                        animGunPitch.value.resume()
                    else:
                        print "jfshPlasmaGun: GUINotify Up button up"
                        animGunPitch.value.stop()
                elif btnID == kDownScopeBtn:
                    if isinstance(control,ptGUIControlButton) and control.isButtonDown():
                        print "jfshPlasmaGun: GUINotify Down button down"
                        animGunPitch.value.backwards(1)
                        animGunPitch.value.resume()
                    else:
                        print "jfshPlasmaGun: GUINotify Down button up"
                        animGunPitch.value.stop()
                elif btnID == kFireScopeBtn:
                    if not gThrottleShooting:
                        print "jfshPlasmaGun: GUINotify Shoot vapor"
                        respShootGun.run(self.key)
                        #PtRequestLOSScreen(self.key,42,0.5,0.5,10000,PtLOSObjectType.kShootable,PtLOSReportType.kReportHitOrMiss)
                        self.IFireBullet()
                        gThrottleShooting = 1
                        try:
                            if type(dlgGunHUD.value) != type(None) and dlgGunHUD.value != "":
                                scopeDlg = PtGetDialogFromString(dlgGunHUD.value)
                                if scopeDlg:
                                    try:
                                        fireBtn = ptGUIControlButton(scopeDlg.getControlFromTag(kFireScopeBtn))
                                        fireBtn.disable()
                                    except KeyError:
                                        print "jfshPlasmaGun: GUINotify can't find the fire button"
                        except KeyError:
                            print "jfshPlasmaGun: GUINotify can't find VaporScope dialog"
                        PtAtTimeCallback(self.key,kTimerThrottleTime,kTimerThrottleFiring)
                    else:
                        print "jfshPlasmaGun: GUINotify Throttling"
                elif btnID == kExitButton:
                    self.IQuitTelescope()


    ###########################
    def OnControlKeyEvent(self,controlKey,activeFlag):
        if controlKey == PlasmaControlKeys.kKeyExitMode:
            self.IQuitTelescope()
        elif controlKey == PlasmaControlKeys.kKeyMoveBackward or controlKey == PlasmaControlKeys.kKeyRotateLeft or controlKey == PlasmaControlKeys.kKeyRotateRight:
            self.IQuitTelescope()

    ###########################
    def OnLOSNotify(self,ID,noHitFlag,sceneobject,hitPoint,distance):
        print "jfshPlasmaGun: LOSNotify:  ID=%d  noHitFlag=%d at a distance of %g" % (ID,noHitFlag,distance)
        PtShootBulletFromScreen(self.key,0.5,0.5,1.0,10000)
        if sceneobject:
            print "jfshPlasmaGun: LOSNotify: ===>hit object %s at point(%g,%g,%g)" % (sceneobject.getName(),hitPoint.getX(),hitPoint.getY(),hitPoint.getZ())
            # first look for a python file guy (before responders)
            pmlist = sceneobject.getPythonMods()
            if len(pmlist) > 0:
                print "jfshPlasmaGun: LOSNotify:  ...python mod list:"
                for pm in pmlist:
                    print "       %s" % (pm.getName())
                    if string.lower(pm.getName()).startswith("vaporminerhitme"):
                        print "jfshPlasmaGun: LOS: VaporMiner HIT!"
                        notify = ptNotify(self.key)
                        notify.clearReceivers()
                        notify.addReceiver(pm)
                        notify.setclkActivateGun(1.0)
                        notify.send()
            else:
                print "jfshPlasmaGun: LOSNotify: ...no python mods found"
            # next look for responders attached
            resplist = sceneobject.getResponders()
            if len(resplist) > 0:
                print "jfshPlasmaGun: LOSNotify:  ...responder list:"
                for resp in resplist:
                    print "       %s" % (resp.getName())
                    if string.lower(resp.getName()).startswith("vaporminerhitme"):
                        print "jfshPlasmaGun: LOS: VaporMiner HIT!"
                        atResp = ptAttribResponder(42)
                        atResp.__setvalue__(resp)
                        atResp.run(self.key)
            else:
                print "jfshPlasmaGun: LOSNotify: ...no responders found"
        else:
            print "jfshPlasmaGun: LOSNotify: No sceneobject found..."

    ###########################
    def IStartTelescope(self):
        global LocalAvatar
        global boolScopeOperator

        clkActivateGun.disable()
        PtSendKIMessage(kDisableKIandBB,0)
        boolScopeOperator = 1
        Behavior.run(LocalAvatar)
        
    ###########################
    def IEngageTelescope(self):
        cam = ptCamera()
        cam.undoFirstPerson()
        cam.disableFirstPersonOverride()

        virtCam = ptCamera()
        virtCam.save(camGunHUD.sceneobject.getKey())

        if type(dlgGunHUD.value) != type(None) and dlgGunHUD.value != "":
            PtLoadDialog(dlgGunHUD.value,self.key, "Jellyfish")
            if ( PtIsDialogLoaded(dlgGunHUD.value) ):
                PtShowDialog(dlgGunHUD.value)

        PtEnableControlKeyEvents(self.key)

    ###########################
    def IQuitTelescope(self):
        global LocalAvatar
        global boolScopeOperator

        if type(dlgGunHUD.value) != type(None) and dlgGunHUD.value != "":
            PtHideDialog(dlgGunHUD.value)

        virtCam = ptCamera()
        virtCam.restore(camGunHUD.sceneobject.getKey())

        Behavior.gotoStage(LocalAvatar,2)
        #Behavior.nextStage(LocalAvatar)

        PtDisableControlKeyEvents(self.key)
        boolScopeOperator = 0

        cam = ptCamera()
        cam.enableFirstPersonOverride()
        PtAtTimeCallback(self.key,kTimerDisengageTime,kTimerDisengage)

    ###########################
    def OnTimer(self,id):
        global gThrottleShooting

        if id == kTimerDisengage:
            clkActivateGun.enable()
            PtSendKIMessage(kEnableKIandBB,0)
        elif id == kTimerThrottleFiring:
            gThrottleShooting = 0
            try:
                if type(dlgGunHUD.value) != type(None) and dlgGunHUD.value != "":
                    scopeDlg = PtGetDialogFromString(dlgGunHUD.value)
                    if scopeDlg:
                        try:
                            fireBtn = ptGUIControlButton(scopeDlg.getControlFromTag(kFireScopeBtn))
                            fireBtn.enable()
                        except KeyError:
                            print "jfshPlasmaGun: Timer can't find the fire button"
            except KeyError:
                print "jfshPlasmaGun: Timer can't find VaporScope dialog"

    ###########################
    def IFireBullet(self):
        global gBulletNum

        code = "Bullet = objBullet0" + str(gBulletNum) + ".sceneobject"
        exec code

        Bullet.physics.damp(0)
        Bullet.physics.disable()
        Bullet.physics.warpObj(objBulletSpawn.value.getKey())
        Bullet.physics.enable()
        Bullet.physics.impulse(ptVector3(100,100,0))


        if gBulletNum == 5:
            gBulletNum = 1
        else:
            gBulletNum += 1

        return Bullet

    ###########################
    def OnBackdoorMsg(self, target, param):
        if target == "shoot":
            self.IFireBullet()