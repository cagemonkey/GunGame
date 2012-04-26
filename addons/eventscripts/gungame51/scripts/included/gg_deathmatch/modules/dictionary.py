# ../scripts/included/gg_deathmatch/modules/dictionary.py

'''
$Rev: 617 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-01-23 13:23:59 -0500 (Mon, 23 Jan 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Script Imports
from player import BasePlayer


# =============================================================================
# >> CLASSES
# =============================================================================
class DictionaryOfPlayers(dict):
    '''Stores BasePlayer instances for each userid on the server'''

    def __getitem__(self, userid):
        ''' Overrides __getitem__ to make sure the
            proper BasePlayer instance is returned
        '''

        # Typecast the userid
        userid = int(userid)

        # Is the userid already in the dictionary?
        if userid in self:

            # Return the player's instance
            return super(DictionaryOfPlayers, self).__getitem__(userid)

        # Create the player's instance
        player = self[userid] = BasePlayer(userid)

        # Assign the remove_player method
        # to delete the userid from the dictionary
        player.remove_player = self.__delitem__

        # Return the player's new instance
        return player

    def __delitem__(self, userid):
        '''Overrides __delitem__ to stop the player's repeat prior to deletion
        '''

        # Typecast the userid
        userid = int(userid)

        # Is the userid in the dictionary?
        if userid in self:

            # Stop the player's repeat
            self[userid].stop_repeat(True)

            # Remove the player from the dictionary
            super(DictionaryOfPlayers, self).__delitem__(userid)

    def clear(self):
        '''Overrides the clear method to call __delitem__ for each userid'''

        # Loop through all userids in the dictionary
        for userid in list(self):

            # Delete the item from the dictionary
            self.__delitem__(userid)

# Get the DictionaryOfPlayer instance
players = DictionaryOfPlayers()
