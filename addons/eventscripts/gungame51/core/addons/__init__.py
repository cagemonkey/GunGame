# ../core/addons/__init__.py

'''
$Rev: 572 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-24 12:25:43 -0400 (Mon, 24 Oct 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame Imports
#   Addons
from priority import PriorityAddon
from manager import AddonManager


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def load(*a, **kw):
    AddonManager()._load_addon(*a, **kw)
load.__doc__ = AddonManager._load_addon.__doc__


def unload(*a, **kw):
    AddonManager()._unload_addon(*a, **kw)
unload.__doc__ = AddonManager._unload_addon.__doc__
