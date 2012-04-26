# ../core/cfg/files/__init__.py

'''
$Rev: 592 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-11-22 16:20:03 -0500 (Tue, 22 Nov 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame Imports
from gungame51.core.cfg.dictionary import ConfigTypeDictionary

# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Declare all config *.py files located in the "core.cfg.files" directory
__all__ = ConfigTypeDictionary._get_config_list('main')
