# ../scripts/included/gg_friendlyfire/gg_friendlyfire_config.py

'''
$Rev: 571 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-24 01:05:16 -0400 (Mon, 24 Oct 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from __future__ import with_statement
from path import path

# GunGame Imports
from gungame51.core.cfg.configs import ConfigContextManager


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
def load():

    # Create the cfg file
    with ConfigContextManager(
      path(__file__).parent.split('scripts')[~0][1:]) as config:

        # Create the gg_friendlyfire instance
        with config.cfg_cvar('gg_friendlyfire') as cvar:

            cvar.name = 'FRIENDLY FIRE'
            cvar.description.append('Automatically turn on friendly fire ' +
                'when a player reaches "x" levels below the last level (+1).')
            cvar.examples.append('gg_friendlyfire 1\n- The above will ' +
                'turn on friendly fire when a player reaches the last level')
            cvar.examples.append(
                'gg_friendlyfire 2\n- The above will turn on friendly ' +
                'fire when a player reaches one level before the last.')
            cvar.options.append('0 = (Disabled) Do not load gg_friendlyfire.')
            cvar.options.append('# = (Enabled) Turn on friendly fire ' +
                'when a player reaches "#" (+1) levels below the last level.')
            cvar.default = 0
            cvar.text = ('The number (+1) of levels below ' +
                'the last level to enable friendly fire.')
