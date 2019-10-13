#		python code
#		script_name:
#
#		author:
#		description:
#

from earsketch import *

init()
setTempo(120)
mySound = RD_ROCK_POPELECTRICLEAD_2
mySound1 = HOUSE_BREAKBEAT_005
mySound2 = RD_WORLD_PERCUSSION_DRUMSMAIN_8
beatString = '0-00-00-0+++0++0+'
makeBeat(OS_COWBELL02, 1, 1, beatString)
print beatString
fitMedia(mySound, 4, 1, 6)
setEffect(4, FLANGER, FLANGER_LENGTH, 120)
setEffect(4, DELAY, DELAY_TIME, 200)

#fitMedia(mySound1, 2, 5, 9)
#fitMedia(mySound2, 3,1,5)
beatString = reverseString(beatString)
makeBeat(OS_COWBELL02, 1, 2, beatString)
print beatString

beatString = shuffleString(beatString)
makeBeat(OS_COWBELL02, 1, 3, beatString)
print beatString

beatString = replaceString(beatString, '+','-')
makeBeat(OS_COWBELL02, 1, 4, beatString)
print beatString

beatString = reverseString(beatString)
makeBeat(OS_COWBELL02, 1, 4.75, beatString)
print beatString

fitMedia(HOUSE_DEEP_PIANO_001, 3, 1, 6)
#setEffect(3, DISTORTION, DISTO_GAIN, 0, 1, 50, 5)


newBeats = [HIPHOP_MUTED_GUITAR_001, HIPHOP_MUTED_GUITAR_002, HIPHOP_MUTED_GUITAR_003, HIPHOP_MUTED_GUITAR_004, HIPHOP_MUTED_GUITAR_005, HIPHOP_MUTED_GUITAR_006, HIPHOP_MUTED_GUITAR_007]
for measure in range(1,5):
  makeBeat(newBeats, 2, measure, '0+-0+1+2+-3+4++5-6+-4+')
  


finish()
 