# ../scripts/included/gg_convert/gg_convert_config.py

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

        # Create the gg_convert instance
        with config.cfg_cvar('gg_convert') as cvar:

            cvar.name = 'CONVERT'
            cvar.description.append('A tool used to convert gungame 3, 4 ' +
                'and 5 (prior to 5.1) winner databases & spawnpoint files.')
            cvar.instructions.append(
                'Place a copy of your winners database or spawnpoint ' +
                'files in this folder:\n ../cfg/gungame51/converter/')
            cvar.instructions.append(
                'Database files include:\nGunGame3: es_gg_winners_db.txt' +
                '\nGunGame4: es_gg_database.sqldb\nGunGame5: winnersdata.db')
            cvar.notes.append(
                'GunGame5.0 SpawnPoint files have not been ' +
                'changed in GunGame5.1. (Simply drag them to ' +
                '../cfg/gungame51/spawnpoints/)')
            cvar.options.append('0 = (Disabled)')
            cvar.options.append('1 = (Enabled) Add together the current ' +
                'and converted wins for each player and combine spawnpoints.')
            cvar.options.append('2 = (Enabled) Replace the current ' +
                'winners and spawnpoints with the converted ones.')
            cvar.default = 0
            cvar.text = 'Enables/Disables gg_convert.'
