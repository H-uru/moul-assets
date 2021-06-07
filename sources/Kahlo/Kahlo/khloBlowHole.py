# Author:  Bill Slease
# Date:    10/8/01

#  This module applies the Kahlo blowhole effect to a player.

from Plasma import *
print "Module 'khloBlowHole' imported."


#  ----
#  INIT
#  ----



bhVectors = {}
bhVectors[0] = (0,0,20000)		# default
bhVectors[2] = (0,0,40000)		# blowhole type 1
bhVectors[1] = (0,1000,30000)		# angle south
bhVectors[4] = (-2000,0,20000)

bhVectors[3] = (0,0,40000)		# blowhole type 1
bhVectors[5] = (0,0,30000)
bhVectors[11] = (0,0,40000)
bhVectors[14] = (0,0,40000)
bhVectors[15] = (-1000,0,5000)
bhVectors[20] = (1000,-1000,10000)
bhVectors[21] = (-1000,1000,10000)

# spine puffers
bhVectors[25] = (0,0,40000)
bhVectors[26] = (0,0,25000)
bhVectors[27] = (0,0,55000)


#  ---------
#  FUNCTIONS
#  ---------


#  Function 'Whoosh' applies a physical force to the player.
#  This force, based upon a vector, creates the blowhole effect.
#  It is applied to whichever player (avatar) happens to trigger it.

def Whoosh(events,bhID=0):
	for event in events:
		if event[0] == 1:
			vec = Vector3(bhVectors[bhID][0],bhVectors[bhID][1],bhVectors[bhID][2])
			event[2].physics.force(vec)
			
			print "Puffer activated: %s" % bhID
			break
