# ../scripts/included/gg_winner_messages/gg_winner_messages.py

'''
$Rev: 563 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-08-23 19:32:15 -0400 (Tue, 23 Aug 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Eventscripts Imports
from gamethread import delayed

# GunGame Imports
#   Addons
from gungame51.core.addons.shortcuts import AddonInfo
#   Messaging
from gungame51.core.messaging.shortcuts import centermsg
from gungame51.core.messaging.shortcuts import saytext2
from gungame51.core.messaging.shortcuts import toptext


# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_winner_messages'
info.title = 'GG Winner Messages'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 563 $".split('$Rev: ')[1].split()[0]
info.translations = ['gg_winner_messages']


# =============================================================================
# >> GAME EVENTS
# =============================================================================
def gg_win(event_var):
    # Store the winner's name
    name = event_var['es_attackername']

    # Store the winner's index
    index = int(event_var['es_attackerindex'])

    # Send chat message for player winning the match
    saytext2('#human', index, 'PlayerWon', {'player': name})

    # We want to loop, so we send a message every second for 3 seconds
    for x in xrange(4):

        # Send centermsgs to players about the winner
        delayed(x, centermsg, ('#human', 'PlayerWon_Center', {'player': name}))

    # Was the winner a Terrorist?
    if int(event_var['es_attackerteam']) == 2:

        # Store color for Terrorists
        color = '#red'

    # Was the winner a CT?
    else:

        # Store color for CTs
        color = '#blue'

    # Send toptext message to players about the winner
    toptext('#human', 10, color, 'PlayerWon_Center', {'player': name})
