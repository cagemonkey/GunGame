# ../core/menus/shortcuts.py

'''
$Rev: 540 $
$LastChangedBy: micbarr $
$LastChangedDate: 2011-07-27 04:35:17 -0400 (Wed, 27 Jul 2011) $
'''


def get_index_page(index, optionsPerPage=10):
    '''
    Returns the page number that item with the index specified is on.
    '''
    return (index / optionsPerPage) + (1 if index % optionsPerPage > 0 else 0)
