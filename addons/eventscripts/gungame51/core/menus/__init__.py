# ../core/menus/__init__.py

'''
$Rev: 575 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-10-25 02:24:08 -0400 (Tue, 25 Oct 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# Python Imports
from path import path

# Eventscripts Imports
import es
from popuplib import Popup_popup
from playerlib import getUseridList

# GunGame Imports
#   Messaging
from gungame51.core.messaging.shortcuts import langstring


# =============================================================================
# >> GLOBAL VARIABLES
# =============================================================================
menu_folder = path(__file__).parent


# =============================================================================
# >> CLASSES
# =============================================================================
class MenuManager(object):
    '''
    Class for managing menus
    '''
    def __new__(cls, *p, **k):
        if not '_gg_menus' in cls.__dict__:
            cls._gg_menus = object.__new__(cls)
            cls._gg_menus.__loaded__ = {}

        return cls._gg_menus

    def load_menus(self):
        es.dbgmsg(0, langstring('Load_Commands'))
        for file_path in menu_folder.files('*_menu.py'):
            self._load(file_path)

    def _load(self, file_path):
        name = file_path.namebase
        if name in self.__loaded__:
            raise NameError('GunGame menu "%s" is already loaded' % name)

        if not file_path.isfile():
            raise NameError('"%s" is not a valid menu name.' % name)

        menuInstance = self.get_menu_by_name(name)
        self.__loaded__[name] = menuInstance
        self.call_block(menuInstance, 'load')

    def unload_menus(self):
        for name in self.__loaded__.keys():
            self._unload(name)

    def _unload(self, name):
        menu_instance = self.get_menu_by_name(name)
        self.call_block(menu_instance, 'unload')
        del self.__loaded__[name]

    def send(self, name, filter_type):
        if name not in self.__loaded__:
            raise NameError('"%s" is not a loaded menu name.' % name)

        elif str(filter_type).isdigit():
            menu_instance = self.get_menu_by_name(name)
            self.call_block(menu_instance, 'send_menu', filter_type)

        elif str(filter_type).startswith('#'):
            for userid in getUseridList(filter_type):
                self.send(name, userid)

        else:
            raise ValueError('"%s" is not a value filter/userid' % filter_type)

    def get_menu_by_name(self, name):
        '''
        Returns the module of an addon by name
        '''
        # If the menu is loaded we have stored the module
        if name in self.__loaded__:
            return self.__loaded__[name]

        # If the menu is not loaded we need to import it
        loadedMenu = __import__(('gungame51.core.menus.%s' % name),
                                                     globals(), locals(), [''])

        # We have to reload the module to re-instantiate the globals
        reload(loadedMenu)
        return loadedMenu

    def call_block(self, menu_instance, blockname, *a, **kw):
        """ Calls a block in a loaded sub-addon """
        menu_globals = menu_instance.__dict__
        if blockname in menu_globals and callable(menu_globals[blockname]):
            menu_globals[blockname](*a, **kw)


class OrderedMenu(object):
    '''
    Creates an ordered menu with continuous numbering throughout pages.
    This class only creates single page popups, for the page the player has
      requested. This way, it only makes a popup for requested pages. It stores
      all of the data for the menu in the list "items".

    Note: highlightIndex will highlight the item at it's number in the menu.
            Menu numbering starts at 1.
    '''
    def __init__(self, userid, title, items=[], options=10,
                                                        highlightIndex=None):
        self.userid = userid
        self.title = title
        self.items = items
        self.options = options
        self.highlightIndex = highlightIndex
        self.totalPages = (
            (len(items) / options) + (1 if len(items) % options > 0 else 0))

    def send_page(self, page):
        # If a page less than 1 is requested, send page 1
        if page < 1:
            page = 1
        # If a page more than the total number of pages is requested, send the
        # last page
        elif page > self.totalPages:
            page = self.totalPages

        # Create a popup
        popup = Popup_popup("OrderedMenu_p%s" % page)
        # Get the index of the first item on the current page
        startIndex = (page - 1) * self.options
        # Add the title
        popup.addline("%s%s(%s/%s)" % (self.title, " " * 5, page,
                                                            self.totalPages))
        popup.addline("-----------------------------")

        # Add all of the options
        for index in xrange(startIndex, startIndex + self.options):
            # If it is the last page, and we are out of data, add empty lines
            if index >= len(self.items):
                popup.addline(" ")
                continue

            # If the current index is the highlightIndex, add -> in front
            highlight = "->" if index + 1 == self.highlightIndex else ""
            # Add the line to the popup
            popup.addline("%s%s. %s" % (highlight, index + 1,
                                                            self.items[index]))

        popup.addline("-----------------------------")

        # Add the back and next buttons based on page number
        if page > 1:
            popup.addline("->8. Back")
        else:
            popup.addline(" ")

        if page < self.totalPages:
            popup.addline("->9. Next")
        else:
            popup.addline(" ")

        # Finish setting up the popup
        popup.addline("0. Exit")
        # Have self.menuselect fire when the player makes a selection
        popup.menuselect = self.menuselect

        popup.timeout('view', 30)
        popup.timeout('send', 30)

        # Send the page
        popup.send(self.userid)

    def menuselect(self, userid, choice, popupName):
        # Get the page number from the popup name
        currentPage = int(popupName.replace("OrderedMenu_p", ""))

        # Close the menu
        if choice == 10:
            return
        # Decrement the page number
        elif choice == 8:
            newPage = currentPage - 1
            self.send_page(newPage)
        # Increment the page number
        elif choice == 9:
            newPage = currentPage + 1
            self.send_page(newPage)
        # Resend the page
        else:
            self.send_page(currentPage)
