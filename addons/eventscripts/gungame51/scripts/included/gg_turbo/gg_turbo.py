# ../scripts/included/gg_turbo/gg_turbo.py

'''
$Rev: 571 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-24 01:05:16 -0400 (Mon, 24 Oct 2011) $
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
from gungame51.core.players.shortcuts import add_attribute_callback
from gungame51.core.players.shortcuts import remove_callbacks_for_addon
from gungame51.core.weapons.shortcuts import get_level_weapon
from gungame51.core.weapons.shortcuts import get_total_levels
from ..gg_nade_bonus.gg_nade_bonus import get_weapon

# =============================================================================
# >> GLOBALS
# =============================================================================
gg_nade_bonus = es.ServerVar("gg_nade_bonus")

# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_turbo'
info.title = 'GG Turbo'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 571 $".split('$Rev: ')[1].split()[0]


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
def load():
    add_attribute_callback('level', level_call_back, info.name)


def unload():
    remove_callbacks_for_addon(info.name)


# =============================================================================
# >> CUSTOM/HELPER FUNCTIONS
# =============================================================================
def level_call_back(name, value, ggPlayer):
    # If the player has been assigned a level already
    if hasattr(ggPlayer, 'level'):
        # Get their previous level, before it was changed
        previousLevel = ggPlayer.level
    # Otherwise
    else:
        # Assume they are on level 1
        previousLevel = 1

    # Delay to give them a new weapon (callbacks are too fast)
    gamethread.delayed(0.005, give_weapon, (ggPlayer.userid, previousLevel))


def give_weapon(userid, previousLevel):
    if not es.exists('userid', userid) and userid != 0:
        return

    # Is spectator?
    if es.getplayerteam(userid) < 2:
        return

    # Get playerlib object
    pPlayer = getPlayer(userid)

    # Is player dead?
    if pPlayer.isdead:
        return

    # Give them their next weapon
    ggPlayer = Player(userid)
    ggPlayer.give_weapon()

    # If previousLevel is not in the order due to weapon orders changing,
    # stop here
    if previousLevel > get_total_levels():
        return

    weapsToStrip = [get_level_weapon(previousLevel)]

    # If the player is was on hegrenade level, and gg_nade_bonus is enabled,
    # and the current level is not hegrenade as well, get the list of their
    # bonus weapons
    if (weapsToStrip[0] == "hegrenade" and
      str(gg_nade_bonus) != "0" and ggPlayer.weapon != "hegrenade"):
        weapsToStrip.extend(get_weapon(userid))

    # If any weapons to be removed were just given, do not strip them
    if ggPlayer.weapon in weapsToStrip:
        weapsToStrip.remove(ggPlayer.weapon)

    # Strip the previous weapons
    ggPlayer.strip_weapons(weapsToStrip)
