# ../core/players/fields/exceptions.py

'''
$Rev: 551 $
$LastChangedBy: micbarr $
$LastChangedDate: 2011-08-02 02:35:16 -0400 (Tue, 02 Aug 2011) $
'''


# =============================================================================
# >> Exception Classes
# =============================================================================
class ValidationError(Exception):
    def __init__(self, msg):
        if isinstance(msg, list):
            self.messages = msg
        else:
            self.messages = [msg]

    def __str__(self):
        return repr(self.messages)

    def __repr__(self):
        return 'ValidationError(%s)' % repr(self.messages)
