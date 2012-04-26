# ../modules/eventmanager.py

'''
$Rev: 623 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-12 21:00:11 -0400 (Mon, 12 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame Imports
#   Modules
import gameevents
#   Addons
from gungame51.core.addons.events import EventRegistry


# =============================================================================
# >> FUNCTIONS
# =============================================================================
def load_events():
    '''Registers all events'''

    # Loop through all event functions of gameevents
    for event in _game_events():

        # Register the function for the event
        EventRegistry.register_for_event(event, gameevents.__dict__[event])


def unload_events():
    '''Unregisters all events'''

    # Loop through all event functions of gameevents
    for event in _game_events():

        # Unregister the function for the event
        EventRegistry.unregister_for_event(event, gameevents.__dict__[event])


def _game_events():
    '''Property that returns all events within the class'''

    # Loop through all functions of gameevents
    for event in gameevents.__dict__:

        # Get the object's instance
        instance = gameevents.__dict__[event]

        # Is the object a function?
        if type(instance).__name__ != 'function':

            # Do not register the object
            continue

        # Is the object native to gameevents?
        if instance.__module__ != gameevents.__name__:

            # Do not register the object
            continue

        # Yield the event
        yield event
