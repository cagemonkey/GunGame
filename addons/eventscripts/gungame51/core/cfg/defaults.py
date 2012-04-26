# ../core/cfg/defaults.py

'''
$Rev: 592 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-11-22 16:20:03 -0500 (Tue, 22 Nov 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# EventScripts Imports
import es


# =============================================================================
# >> CLASSES
# =============================================================================
class _CvarDefaults(dict):
    '''Class that stores cvars with their default value'''

    def clear(self):
        '''Resets all cvars in the dictionary and then clears itself'''

        # Loop through all cvars in the dictionary
        for cvar in self:

            # Set the cvar to its default value
            es.ServerVar(cvar).set(self[cvar])

            # Remove the notify flag from the cvar
            es.ServerVar(cvar).removeFlag('notify')

        # Clear the dictionary
        super(_CvarDefaults, self).clear()

# Get the CvarDefaults instance
CvarDefaults = _CvarDefaults()
