# ../scripts/included/gg_welcome_msg/gg_welcome_msg.py

'''
$Rev: 571 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-24 01:05:16 -0400 (Mon, 24 Oct 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from __future__ import with_statement
import time

# Eventscripts Imports
import es
from cmdlib import registerSayCommand
from cmdlib import unregisterSayCommand
import popuplib

# GunGame Imports
from gungame51.core.addons.shortcuts import AddonInfo
from gungame51.core import get_game_dir
from gungame51.core import gungame_info
from gungame51.core.addons.shortcuts import get_loaded_addon_list


# =============================================================================
# >> ADDON REGISTRATION/INFORMATION
# =============================================================================
info = AddonInfo()
info.name = 'gg_welcome_msg'
info.title = 'GG Welcome Message'
info.author = 'GG Dev Team'
info.version = "5.1.%s" % "$Rev: 571 $".split('$Rev: ')[1].split()[0]


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
# Store the title of the menu
title = 'GunGame%s -- Welcome Message' % gungame_info('version')
gg_welcome_msg_timeout = es.ServerVar('gg_welcome_msg_timeout')

# Create an empty list for detecting if a player just joined the server
messageQueue = []


# =============================================================================
# >> LOAD & UNLOAD
# =============================================================================
def load():
    # Register !welcome
    registerSayCommand('!welcome', welcome, 'Displays a !welcome menu.')

    # Build the main gg_welcome popup
    buildPopups()


def unload():
    # Unregister !welcome
    unregisterSayCommand('!welcome')

    # Clean up existing popups
    if popuplib.exists('gg_welcome'):
        popuplib.delete('gg_welcome')
    if popuplib.exists('gg_welcome_include'):
        popuplib.delete('gg_welcome_include')
    if popuplib.exists('gg_welcome_custom'):
        popuplib.delete('gg_welcome_custom')


# =============================================================================
# >> GAME EVENTS
# =============================================================================
def player_activate(event_var):
    userid = event_var['userid']

    # If the user is already in the que to receive the welcome message, stop
    # here
    if userid in messageQueue:
        return

    # Add the user to the welcome message queue
    messageQueue.append(userid)


def player_team(event_var):
    userid = event_var['userid']

    # If the user is in the queue
    if userid in messageQueue:
        # Send them the welcome message
        welcome(userid, '')
        # Remove them from the queue
        messageQueue.remove(userid)


# =============================================================================
# >> CUSTOM/HELPER FUNCTIONS
# =============================================================================
def buildPopups():
    # Get the custom text for the popup
    with get_game_dir('cfg/gungame51/' +
      'included_addon_configs/gg_welcome_msg.txt').open() as customFile:
        customText = customFile.readlines()

    # Remove unnecessary characters
    customText = [x.strip() for x in customText]
    # Ignore commented lines
    customText = filter(lambda x: x[:2] != '//', customText)

    # Create a new popuplib instance
    menu = popuplib.create('gg_welcome')
    menu.addline(title)
    menu.addline('-' * 30)

    # For each line of custom text
    for line in customText:
        # If there is nothing on the line, make it a single space to show up
        # on the menu
        if not line:
            line = ' '

        # Replace variables in the line
        line = line.replace('$server', str(es.ServerVar('hostname')))
        line = line.replace('$date', time.strftime('%d/%m/%Y'))
        line = line.replace('$time', time.strftime('%H:%M:%S'))

        # Add the line to the menu
        menu.addline(line)

    # Create the rest of the menu
    menu.addline('-' * 30)
    menu.addline('->1. Included Addons')
    menu.select(1, welcome_handler)
    menu.addline('->2. Custom Addons')
    menu.select(2, welcome_handler)
    menu.addline('-' * 30)
    menu.addline('0. Cancel')

    # Set the timeout for the menu
    menu.timeout('send', int(gg_welcome_msg_timeout))
    menu.timeout('view', int(gg_welcome_msg_timeout))


def welcome(userid, args):
    # Do not send to bots or non-existent players
    if es.getplayersteamid(userid) == 'BOT' or not es.exists('userid', userid):
        return

    # If the user has the popup open, remove it
    popuplib.unsendname('gg_welcome', userid)
    # Send the popup
    popuplib.send('gg_welcome', userid)


def welcome_handler(userid, choice, popupname):
    # If they selected to see the included addons list
    if choice == 1:
        # If the menu exists, delete it
        if popuplib.exists('gg_welcome_include'):
            popuplib.delete('gg_welcome_include')
        # Create an easylist instance
        menu = popuplib.easylist('gg_welcome_include',
                                        get_loaded_addon_list('included'))
    elif choice == 2:
        # If the menu exists, delete it
        if popuplib.exists('gg_welcome_custom'):
            popuplib.delete('gg_welcome_custom')
        # Create an easylist instance
        menu = popuplib.easylist('gg_welcome_custom',
                                            get_loaded_addon_list('custom'))

    # Set the menu's title
    menu.settitle(title)
    # When the menu is closed, go back to the welcome message
    menu.submenu(0, 'gg_welcome')
    # Set the timeout for the menu
    menu.timeout('send', int(gg_welcome_msg_timeout))
    menu.timeout('view', int(gg_welcome_msg_timeout))
    # Send the popup
    menu.send(userid)
