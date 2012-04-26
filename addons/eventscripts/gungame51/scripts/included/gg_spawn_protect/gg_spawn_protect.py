# ../scripts/included/gg_spawn_protect/gg_spawn_protect.py

'''
$Rev: 625 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-21 23:37:28 -0400 (Wed, 21 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Eventscripts Imports
import es
import gamethread
from playerlib import getPlayer

# GunGame Imports
from gungame51.core.addons.shortcuts import AddonInfo
from gungame51.core.players.shortcuts import Player


# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_spawn_protect'
info.title = 'GG Spawn Protection'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 625 $".split('$Rev: ')[1].split()[0]

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Get the es.ServerVar() instance of "gg_spawn_protect"
gg_spawn_protect = es.ServerVar('gg_spawn_protect')

# Get the es.ServerVar() instance of "gg_spawn_protect_cancelonfire"
gg_spawn_protect_cancelonfire = es.ServerVar('gg_spawn_protect_cancelonfire')

# Get the es.ServerVar() instance of "gg_spawn_protect_can_level_up"
gg_spawn_protect_can_level_up = es.ServerVar('gg_spawn_protect_can_level_up')

# Get the es.ServerVar() instance of "gg_spawn_protect_red"
gg_spawn_protect_red = es.ServerVar('gg_spawn_protect_red')

# Get the es.ServerVar() instance of "gg_spawn_protect_green"
gg_spawn_protect_green = es.ServerVar('gg_spawn_protect_green')

# Get the es.ServerVar() instance of "gg_spawn_protect_blue"
gg_spawn_protect_blue = es.ServerVar('gg_spawn_protect_blue')

# Get the es.ServerVar() instance of "gg_spawn_protect_alpha"
gg_spawn_protect_alpha = es.ServerVar('gg_spawn_protect_alpha')

# Get the es.ServerVar() instance of "eventscripts_noisy"
eventscripts_noisy = es.ServerVar('eventscripts_noisy')

noisySave = 0
protectedList = []


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
def load():
    if gg_spawn_protect_cancelonfire:
        es.doblock('corelib/noisy_on')


def unload():
    if gg_spawn_protect_cancelonfire:
        es.doblock('corelib/noisy_off')


# =============================================================================
# >> GAME EVENTS
# =============================================================================
def server_cvar(event_var):
    # Change "eventscripts_noisy" due to "gg_spawn_protect_cancelonfire"?
    if event_var['cvarname'] == 'gg_spawn_protect_cancelonfire':

        if int(event_var['cvarvalue']) >= 1:
            # Set noisy vars
            es.doblock('corelib/noisy_on')
        else:
            # Set noisy back
            es.doblock('corelib/noisy_off')


def weapon_fire(event_var):
    if not int(gg_spawn_protect_cancelonfire):
        return

    userid = int(event_var['userid'])

    if userid in protectedList:
        # Cancel the delay if protected
        gamethread.cancelDelayed('ggSpawnProtect%s' % userid)

        # End the protection
        endProtect(userid)


def player_spawn(event_var):
    # Is spectator?
    if int(event_var['es_userteam']) < 2:
        return

    # Set player's id
    userid = int(event_var['userid'])

    # Is player dead?
    if getPlayer(userid).isdead:
        return

    if userid in protectedList:
        return

    # Start protecting the player
    startProtect(userid)


def player_death(event_var):
    userid = int(event_var['userid'])

    if userid in protectedList:
        gamethread.cancelDelayed('ggSpawnProtect%s' % userid)
        protectedList.remove(userid)


def player_disconnect(event_var):
    userid = int(event_var['userid'])

    # Remove from protected list
    if userid in protectedList:
        gamethread.cancelDelayed('ggSpawnProtect%s' % userid)
        protectedList.remove(userid)


# =============================================================================
# >> CUSTOM/HELPER FUNCTIONS
# =============================================================================
def startProtect(userid):
    # Retrieve player objects
    pPlayer = getPlayer(userid)

    # Add them to the list of protected players
    protectedList.append(userid)

    # Set color
    pPlayer.color = (gg_spawn_protect_red,
                     gg_spawn_protect_green,
                     gg_spawn_protect_blue,
                     gg_spawn_protect_alpha)

    # Start Invincible
    pPlayer.godmode = 1

    # Set PreventLevel if needed
    if not int(gg_spawn_protect_can_level_up):
        ggPlayer = Player(userid)

        if not 'gg_spawn_protect' in ggPlayer.preventlevel():
            ggPlayer.preventlevel.append('gg_spawn_protect')

    # Start the delay to cancel spawn protection
    gamethread.delayedname(int(gg_spawn_protect),
        'ggSpawnProtect%s' % userid, endProtect, (userid))


def endProtect(userid):
    # Are they even protected?
    if not userid in protectedList:
        return

    # Check the client hasn't left during the protection period
    if not es.exists('userid', userid) and userid != 0:
        # Fix potential memory leak:
        protectedList.remove(userid)
        return

    # Retrieve player objects
    pPlayer = getPlayer(userid)

    # Remove the player from the list of protected players
    protectedList.remove(userid)

    # Color
    pPlayer.color = (255, 255, 255, 255)

    # End Invincible
    pPlayer.godmode = 0

    # Remove PreventLevel if it was enabled
    if not int(gg_spawn_protect_can_level_up):
        ggPlayer = Player(userid)

        if 'gg_spawn_protect' in ggPlayer.preventlevel():
            ggPlayer.preventlevel.remove('gg_spawn_protect')
