# ../scripts/included/gg_suicide_punish/gg_suicide_punish.py

'''
$Rev: 627 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-27 18:28:57 -0400 (Tue, 27 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Eventscripts Imports
import es
import gamethread

# GunGame Imports
#   Modules
from gungame51.modules.active import ActiveInfo
#   Addons
from gungame51.core.addons.shortcuts import AddonInfo
#   Players
from gungame51.core.players.shortcuts import Player


# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_suicide_punish'
info.title = 'GG Suicide Punish'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 627 $".split('$Rev: ')[1].split()[0]
info.translations = ['gg_suicide_punish']


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the es.ServerVar() instance of "gg_suicide_punish"
gg_suicide_punish = es.ServerVar('gg_suicide_punish')

# Store a list of those who recently changed teams, to not punish them if they
# committed suicide to do so
recentTeamChange = []


# =============================================================================
# >> GAME EVENTS
# =============================================================================
def player_team(event_var):
    userid = int(event_var["userid"])

    # Store them here so we don't punish them if this team change caused a
    # suicide
    if not userid in recentTeamChange:
        recentTeamChange.append(userid)
        gamethread.delayed(0.2, recentTeamChange.remove, userid)


def player_death(event_var):
    '''
    Note to devs:
        Strangely enough, player_death no longer fires anymore when a player
        is killed by the bomb exploding. Therefore, we no longer need to keep
        track of counting bomb deaths as suicide.
    '''
    # Has the round ended?
    if not ActiveInfo.round:
        return

    # Set player ids
    userid = int(event_var['userid'])
    attacker = int(event_var['attacker'])

    # Is the victim on the server?
    if not es.exists('userid', userid) and userid != 0:
        return

    # If the attacker is not "world or the userid of the victim, it is not a
    # suicide
    if not attacker in (0, userid):
        return

    # If the suicide was caused by a team change, stop here
    if userid in recentTeamChange:
        return

    # Get victim object
    ggVictim = Player(userid)

    # Trigger level down
    ggVictim.leveldown(int(gg_suicide_punish), userid, 'suicide')

    # Message
    ggVictim.msg('Suicide_LevelDown', {'newlevel': ggVictim.level},
                    prefix='gg_suicide_punish')

    # Play the leveldown sound
    ggVictim.playsound('leveldown')
