# ../scripts/included/gg_earn_nade/gg_earn_nade_config.py

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

        # Create the gg_earn_nade instance
        with config.cfg_cvar('gg_earn_nade') as cvar:

            cvar.name = 'EARN GRENADES'
            cvar.description.append(
                'When a player reaches grenade level, they can earn ' +
                'extra grenades by killing enemies with another weapon.')
            cvar.notes.append(
                'Players can only carry one hegrenade at a time.')
            cvar.options.append('0 = (Disabled) Do not load gg_earn_nade.')
            cvar.options.append('1 = (Enabled) Load gg_earn_nade.')
            cvar.default = 0
            cvar.text = 'Enables/Disables gg_earn_nade.'
