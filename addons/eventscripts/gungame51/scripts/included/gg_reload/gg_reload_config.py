# ../scripts/included/gg_reload/gg_reload_config.py

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

        # Create the gg_reload instance
        with config.cfg_cvar('gg_reload') as cvar:

            cvar.name = 'RELOAD'
            cvar.description.append('When a player gains a ' +
                'level, the ammo in their clip is replenished.')
            cvar.options.append('0 = (Disabled) Do not load gg_reload.')
            cvar.options.append('1 = (Enabled) Load gg_reload.')
            cvar.default = 0
            cvar.text = 'Enables/Disables gg_reload.'
