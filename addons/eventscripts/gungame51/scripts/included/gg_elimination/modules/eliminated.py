# ../scripts/included/gg_elimination/modules/eliminated.py

'''
$Rev: 623 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-12 21:00:11 -0400 (Mon, 12 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Script Imports
from respawn import respawn_players


# =============================================================================
# >> CLASSES
# =============================================================================
class EliminatedPlayers(set):
    '''Class used to store players that were eliminated by an individual player
        and set the list of players to respawn when the player has died'''

    def clear(self):
        '''Clears the player's set of eliminated players
            and sets the eliminated players to respawn'''

        # Add the eliminated players to the respawn list
        respawn_players.append(list(self))

        # Clear the set
        super(EliminatedPlayers, self).clear()
