# ../scripts/included/gg_random_spawn/gg_random_spawn.py

'''
$Rev: 571 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-24 01:05:16 -0400 (Mon, 24 Oct 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
#Python Imports
from __future__ import with_statement
import random

# SPE Imports
import spe

# Eventscripts Imports
import es

# GunGame Imports
from gungame51.core import get_game_dir
from gungame51.core.addons.shortcuts import AddonInfo

# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_random_spawn'
info.title = 'GG Random Spawn'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 571 $".split('$Rev: ')[1].split()[0]

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================

spawnPoints = []
pointsLoaded = False


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
def load():
    loadSpawnFile(str(es.ServerVar("eventscripts_currentmap")))

    userid = es.getuserid()

    # If there are no players on the server, stop here
    if not userid:
        return

    pointsLoaded = True

    if not spawnPoints:
        return

    loadRandomPoints(userid)


# =============================================================================
# >> GUNGAME EVENTS
# =============================================================================
def es_map_start(event_var):
    global pointsLoaded

    pointsLoaded = False
    loadSpawnFile(event_var['mapname'])


def player_activate(event_var):
    global pointsLoaded

    if pointsLoaded:
        return

    pointsLoaded = True

    if not spawnPoints:
        return

    loadRandomPoints(event_var['userid'])


# =============================================================================
# >> CUSTOM/HELPER FUNCTIONS
# =============================================================================
def loadSpawnFile(mapName):
    global spawnPoints
    global pointsLoaded

    spawnPoints = []
    pointsLoaded = False

    # Get spawnpoint file
    spawnFile = get_game_dir('cfg/gungame51/spawnpoints/%s.txt' % mapName)

    # Does the file exist?
    if not spawnFile.isfile():
        return

    # Get spawnpoint lines
    with spawnFile.open() as spawnPointFile:
        fileLines = [x.strip() for x in spawnPointFile.readlines()]

    # Set up spawnpoints
    spawnPoints = [x.split(' ', 6) for x in fileLines]

    # Randomize spawnpoints
    random.shuffle(spawnPoints)


def loadRandomPoints(userid):
    # Remove existing spawnpoints
    for tSpawn in es.getEntityIndexes('info_player_terrorist'):
        es.server.cmd('es_xremove %s' % tSpawn)
    for ctSpawn in es.getEntityIndexes('info_player_counterterrorist'):
        es.server.cmd('es_xremove %s' % ctSpawn)

    # Loop through the spawnpoints
    for spawn in spawnPoints:
        for team in ('info_player_terrorist', 'info_player_counterterrorist'):
            # Create the spawnpoint and get the index
            index = spe.getIndexOfEntity(spe.giveNamedItem(userid, team))

            # Set the spawnpoint position and rotation
            es.setindexprop(index, 'CBaseEntity.m_vecOrigin',
                '%s,%s,%s' % (spawn[0], spawn[1], spawn[2]))
            es.setindexprop(index, 'CBaseEntity.m_angRotation',
                '0,%s,0' % spawn[4])
