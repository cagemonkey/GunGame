# ../scripts/included/gg_noblock/gg_noblock_config.py

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

        # Create the gg_noblock instance
        with config.cfg_cvar('gg_noblock') as cvar:

            cvar.name = 'NO BLOCK'
            cvar.description.append(
                'Makes it possible to pass through all players.')
            cvar.options.append('0 = (Disabled) Do not load gg_noblock.')
            cvar.options.append('1 = (Enabled) Load gg_noblock.')
            cvar.default = 0
            cvar.text = 'Enables/Disables gg_noblock.'
