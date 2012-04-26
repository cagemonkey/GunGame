# ../scripts/included/gg_deathmatch/modules/countdown.py

'''
$Rev: 627 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-27 18:28:57 -0400 (Tue, 27 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# EventScripts Imports
#   ES
from es import ServerVar
from es import exists
#   Gamethread
from gamethread import delayed
#   Playerlib
from playerlib import getPlayer

# GunGame Imports
#   Modules
from gungame51.modules.active import ActiveInfo
#   Repeat
from gungame51.core.repeat import Repeat


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
gg_dm_respawn_delay = ServerVar('gg_dm_respawn_delay')


# =============================================================================
# >> CLASSES
# =============================================================================
class PlayerCountdown(object):
    '''Object used to house the countdown methods for BasePlayer objects'''

    def start_repeat(self):
        '''Starts the player's repeat'''

        # Is there a delay?
        if not int(gg_dm_respawn_delay):

            # If not, simply spawn the player
            delayed(0.1, self.check_respawn)

            # No need to go further
            return

        # Start the player's repeat
        self.repeat.start(1, int(gg_dm_respawn_delay))

    def count_down(self):
        '''Sends hudhint messages with remaining time and respawns the player
        '''

        # Is the player still on the server?
        if not exists('userid', self.userid):

            # If not, remove them from the players dictionary
            self.remove_player(self.userid)

            # No need to go further
            return

        # Is the player alive?
        if not getPlayer(self.userid).isdead:

            # Stop the repeat
            self.stop_repeat()

            # No need to continue the count-down
            return

        # Is the round inactive?
        if not ActiveInfo.round:

            # Send the player a hudhint that the round has ended
            self.send_hudhint('RespawnCountdown_RoundEnded')

            # Stop the repeat
            self.stop_repeat()

            # No need to continue
            return

        # Is there more than 1 loop remaining?
        if self.repeat.remaining > 1:

            # Send the player a hudhint with the time remaining
            self.send_hudhint(
                'RespawnCountdown_Plural', {'time': self.repeat.remaining})

        # Is there exactly 1 loop remaining?
        elif self.repeat.remaining == 1:

            # Send the player a hudhint with the time remaining
            self.send_hudhint('RespawnCountdown_Singular')

        # Are there no more loops remaining?
        else:

            # Send the player a hudhint that they are being respawned
            self.send_hudhint('RespawnCountdown_Ended')

            # Get the remaining time (less than a second) to respawn
            remaining = float(gg_dm_respawn_delay) % 1

            # Is there still time remaining?
            if remaining:

                # Respawn the player after the remaining time
                delayed(remaining, self.check_respawn)

            # Is there no time remaining?
            else:

                # Respawn the player immediately
                self.gg_player.respawn()

    def stop_repeat(self, delete=False):
        '''Stops the repeat and deletes it if needed'''

        # Stop the player's repeat
        self.repeat.stop()

        # Does the repeat need deleted?
        if delete:

            # Delete the repeat
            self.repeat.delete()

    def check_respawn(self):
        '''Checks to see if the round is still
            active before spawning the player'''

        # Is the round still active?
        if ActiveInfo.round:

            # Spawn the player
            self.gg_player.respawn()

    @property
    def repeat(self):
        '''Property used to return the player's Repeat instance'''

        # Does the player have a Repeat instance?
        if not hasattr(self, '_repeat'):

            # Create the player's Repeat instance
            self._repeat = Repeat(
                'gg_deathmatch_%s' % self.userid, self.count_down)

        # Return the player's Repeat instance
        return self._repeat
