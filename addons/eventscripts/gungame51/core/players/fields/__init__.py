# ../core/players/fields/__init__.py

'''
$Rev: 548 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-08-01 22:42:23 -0400 (Mon, 01 Aug 2011) $
'''

# =============================================================================
# >> Imports
# =============================================================================
from fields import *


def make_fields(**kwargs):
    for k, v in kwargs.items():
        if not isinstance(v, PlayerField):
            raise ValueError('Fields must be a PlayerField instance.')
    return kwargs
