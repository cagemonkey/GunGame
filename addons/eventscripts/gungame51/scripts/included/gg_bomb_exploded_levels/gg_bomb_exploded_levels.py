# ../scripts/included/gg_bomb_exploded_levels/gg_bomb_exploded_levels.py

'''
$Rev: 560 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-08-22 20:46:56 -0400 (Mon, 22 Aug 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Eventscripts Imports
import es

# GunGame Imports
#   Addons
from gungame51.core.addons.shortcuts import AddonInfo
#   Players
from gungame51.core.players.shortcuts import Player
#   Weapons
from gungame51.core.weapons.shortcuts import get_level_weapon
from gungame51.core.weapons.shortcuts import get_total_levels

# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_bomb_exploded_levels'
info.title = 'GG Welcome Message'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 560 $".split('$Rev: ')[1].split()[0]
info.translations = ['gg_bomb_exploded_levels']

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
gg_bomb_exploded_levels = es.ServerVar('gg_bomb_exploded_levels')
gg_bomb_exploded_skip_knife = es.ServerVar('gg_bomb_exploded_skip_knife')
gg_bomb_exploded_skip_nade = es.ServerVar('gg_bomb_exploded_skip_nade')


# =============================================================================
# >> GAME EVENTS
# =============================================================================
def bomb_exploded(event_var):
    # Get the player instance
    ggPlayer = Player(event_var['userid'])

    # The number of levels we will level up the player
    levels = 1

    # If they shouldn't be skipping their current level, stop here
    if ((not int(gg_bomb_exploded_skip_knife) and ggPlayer.weapon == 'knife')
      or (not int(gg_bomb_exploded_skip_nade) and
      ggPlayer.weapon == 'hegrenade')):
        ggPlayer.msg('CannotSkipLevel_ByPlanting', {'level': ggPlayer.weapon})
        return

    # Loop through weapons of the levels we plan to level the player up past
    for weapon in getLevelupList(ggPlayer.level,
      ggPlayer.level + int(gg_bomb_exploded_levels)):
        # If gg_bomb_exploded_skip_knife or gg_bomb_exploded_skip_nade are
        # disabled, make sure the player will not skip that level
        if ((not int(gg_bomb_exploded_skip_knife) and weapon == 'knife') or
          (not int(gg_bomb_exploded_skip_nade) and weapon == 'hegrenade')):
            ggPlayer.msg('CannotSkipLevel_ByPlanting', {'level': weapon})
            break

        # Add to the number of levels they will gain
        levels += 1

    # Level up the player
    ggPlayer.levelup(levels, 0, 'bomb_exploded')


# =============================================================================
# >> CUSTOM/HELPER FUNCTIONS
# =============================================================================
def getLevelupList(currentLevel, levelupLevel):
    levelupList = []

    # Get the total number of levels
    totalLevels = get_total_levels()

    # If the player would exceed the total number of levels, stop at the total
    if levelupLevel > totalLevels:
        levelupLevel = totalLevels

    # Create a list of the weapon names for levels we plan to level the player
    # up past
    for level in xrange(currentLevel + 1, levelupLevel):
        levelupList.append(get_level_weapon(level))

    # Return the list
    return levelupList
