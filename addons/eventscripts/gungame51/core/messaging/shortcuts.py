# ../core/messaging/shortcuts.py

'''
$Rev: 588 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-11-13 10:23:46 -0500 (Sun, 13 Nov 2011) $
'''

from gungame51.core.messaging import MessageManager


def msg(filter, string, tokens={}, prefix=False):
    MessageManager().msg(filter, string, tokens, prefix)


def saytext2(filter, index, string, tokens={}, prefix=False):
    MessageManager().saytext2(filter, index, string, tokens, prefix)


def centermsg(filter, string, tokens={}):
    MessageManager().centermsg(filter, string, tokens)


def hudhint(filter, string, tokens={}):
    MessageManager().hudhint(filter, string, tokens)


def toptext(filter, duration, color, string, tokens={}):
    MessageManager().toptext(filter, duration, color, string, tokens)


def echo(filter, level, string, tokens={}, prefix=False):
    MessageManager().echo(filter, level, string, tokens, prefix)


def langstring(string, tokens={}, userid=0, prefix=False):
    return MessageManager().langstring(string, tokens, userid, prefix)


def load_translation(name, addon):
    MessageManager().load(name, addon)


def unload_translation(name, addon):
    MessageManager().unload(name, addon)
