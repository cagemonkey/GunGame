# ../core/players/messaging.py

'''
$Rev: 540 $
$LastChangedBy: micbarr $
$LastChangedDate: 2011-07-27 04:35:17 -0400 (Wed, 27 Jul 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame Imports
from gungame51.core.messaging import MessageManager as _MessageManager


# =============================================================================
# >> GLOBALS
# =============================================================================
_MESSAGEMANAGER = _MessageManager()


# =============================================================================
# >> CLASSES
# =============================================================================
class PlayerMessaging(object):
    """Adds messaging methods to the BasePlayer class."""
    def msg(self, string, tokens={}, prefix=False):
        _MESSAGEMANAGER.msg(self.userid, string, tokens, prefix)

    def saytext2(self, index, string, tokens={}, prefix=False):
        _MESSAGEMANAGER.saytext2(self.userid, index, string, tokens, prefix)

    def centermsg(self, string, tokens={}):
        _MESSAGEMANAGER.centermsg(self.userid, string, tokens)

    def hudhint(self, string, tokens={}):
        _MESSAGEMANAGER.hudhint(self.userid, string, tokens)

    def toptext(self, duration, color, string, tokens={}):
        _MESSAGEMANAGER.toptext(self.userid, duration, color, string, tokens)

    def echo(self, level, string, tokens={}, prefix=False):
        _MESSAGEMANAGER.echo(self.userid, level, string, tokens, prefix)

    def langstring(self, string, tokens={}, prefix=False):
        return _MESSAGEMANAGER.langstring(string, tokens, self.userid, prefix)
