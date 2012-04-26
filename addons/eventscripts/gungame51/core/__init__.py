# ../core/__init__.py

'''
$Rev: 627 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2012-03-27 18:28:57 -0400 (Tue, 27 Mar 2012) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from __future__ import with_statement
from os import name as os_name
from path import path

# Eventscripts Imports
import es


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
game_path = path(path(
    __file__).parent.rsplit('addons', 1)[0][:~0].replace('\\', '/'))


# =============================================================================
# >> CLASSES
# =============================================================================
class GunGameError(Exception):
    '''Base Error to use for GunGame errors'''
    pass


class InfoList(list):
    '''Class used to store the keylist and verify that attributes
        that start with "_" do not get added to the keylist'''

    def append(self, item):
        '''Verify that the item does not start with
            "_" when adding the item to the keylist'''

        # Does the item start with "_"?
        if not item.startswith('_'):

            # If not, add it to the list
            super(InfoList, self).append(item)


class _GunGameInfo(es.AddonInfo):
    '''Class used to store the AddonInfo for GunGame51'''

    def __init__(self):
        '''Called on initialization of the class'''

        # Store the keylist as an InfoList instance
        self.keylist = InfoList()

        # Store the version
        self._version = get_version()

    @property
    def version(self):
        '''Property that returns the version of GunGame51'''

        # Return the version
        return self._version


# =============================================================================
# >> FILES, DIRECTORIES, & OS FUNCTIONS
# =============================================================================
def get_game_dir(folder=None):
    '''!Gets an absolute path to a game directory.

    @remark Implicitly replaces \\ with / (linux support)

    @param dir Directory to append to the game directory.

    @return An absolute path to the game directory plus \p dir.'''
    if folder:
        folder = str(folder).replace('\\', '/')
        return game_path.joinpath(folder)
    return game_path


def get_os():
    return os_name


def in_map():
    '''!Checks to see if the server is currently in a map.

    @retval True The server is in a map.
    @retval False The server is not in a map.'''
    return (str(es.ServerVar('eventscripts_currentmap')) != '')


def remove_return_chars(text):
    text = text.replace('\\r', '')
    return text.replace('\\n', '')


def get_file_list(top=get_game_dir('addons/eventscripts')):
    '''
    Generator that returns a list of files from within the gungame51 directory
    recursively.

    returns something like this:
    ['c:/srcds/cstrike/addons/eventscripts/gungame51',
        ['core', 'gungame51.py', 'scripts', '__init__.py']]

    (Excluding svn folders and files.)
    '''
    for name in path(top).walkdirs():
        if not "gungame51" in name:
            continue

        yield [str(name).replace('\\', '/'),
            [str(x.name) for x in name.files('*.py')]]

# =============================================================================
# >> OLD FILE REMOVAL
# =============================================================================
# List of old files no longer in use.
old_files = [
    'addons/eventscripts/gungame51/core/events/data/es_gungame_events.res',
    'addons/eventscripts/gungame51/scripts/included/gg_error_logging',
    'addons/eventscripts/gungame51/scripts/included/gg_thanks',
    'cfg/gungame51/included_addon_configs/gg_error_logging.cfg',
    'cfg/gungame51/included_addon_configs/gg_thanks.cfg',
    'cfg/gungame51/gg_default_addons.cfg',
]

# Delete any out of date files
for old_file in old_files:

    # Get the full path to the file
    old_file = get_game_dir(old_file)

    if old_file.isfile():
        old_file.remove()

    # Delete entire directory?
    elif old_file.isdir():
        old_file.rmtree()
    else:
        continue

    # Send console message
    es.server.queuecmd('echo [GunGame] Deleted %s' % str(old_file))


def gungame_info(info):
    '''
    Fetches the head revision number from all of gungame's files
    '''

    # Looking for GunGame's version?
    if info == 'version':

        # Return the version number
        return GunGameInfo.version

    # Updating GunGame's information?
    if info == 'update':

        # Update Included Addons
        GunGameInfo.__setattr__('Included Addons', gungame_info('included'))

        # Update Custom Addons
        GunGameInfo.__setattr__('Custom Addons', gungame_info('custom'))

    # Getting Included or Custom Addon information?
    if info in ('included', 'custom'):

        # Retrieve the Loaded Addons
        from addons.loaded import LoadedAddons

        # Format our output
        addonlist = ['\t' * 4 + '%s (v%s)\n' % (
            LoadedAddons[addon].info.name,
            LoadedAddons[addon].info.version) for addon in
            LoadedAddons if LoadedAddons[addon].addon_type == info]

        # If no addons, output is None
        if not addonlist:

            # Return a string showing no addons are loaded
            return '\n' + '\t' * 4 + 'None\n'

        # Add a line return to the beginning of our output
        addonlist.insert(0, '\n')

        # Return the list as one string
        return ' '.join(addonlist)


def get_version(addon=None):
    '''Function used to get the current version of GunGame'''

    # Start with 0 as the revision number
    revision = 0

    # Getting GunGame's version?
    if addon is None:

        # Get all files in the gungame51 directory
        basepath = get_game_dir('addons/eventscripts/gungame51')

    # Getting an included addon's version?
    else:

        # Get all files in the addon's directory
        basepath = get_game_dir(
            'addons/eventscripts/gungame51/scripts/included/%s' % addon)

    # Loop through all .py files in the GunGame structure
    for file_path in basepath.walkfiles('*.py'):

        # Is the file part of a custom addon?
        if 'custom' in file_path.splitall():

            # If so, we don't want to include this file
            continue

        # Try to open the file and get its revision number
        try:
            with file_path.open() as pyfile:
                version = int(pyfile.read().split('$Rev: ')[1].split()[0])

            # Is the current file's version newer than the current newest file?
            if version > revision:

                # Set the newest file version to the current file's version
                revision = version

        # If an error is encountered, just continue to the next file
        except:
            continue

    # Return the newest revision number
    return '5.1.%s' % revision

# Get the _GunGameInfo instance
GunGameInfo = _GunGameInfo()
