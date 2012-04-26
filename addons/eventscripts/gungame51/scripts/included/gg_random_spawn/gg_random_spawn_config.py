# ../scripts/included/gg_random_spawn/gg_random_spawn_config.py

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

        # Create the gg_random_spawn instance
        with config.cfg_cvar('gg_random_spawn') as cvar:

            cvar.name = 'RANDOM SPAWNPOINTS'
            cvar.description.append('Loads random spawnpoints if a ' +
                'spawnpoint file for the current map has been created.')
            cvar.notes.append('Create spawnpoint files ' +
                'with the gg_spawnpoints included addon.')
            cvar.options.append('0 = (Disabled) Do not load gg_random_spawn.')
            cvar.options.append('1 = (Enabled) Load gg_random_spawn.')
            cvar.default = 0
            cvar.text = 'Enables/Disables random spawn points.'
