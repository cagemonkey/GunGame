# ../core/players/fields/validators.py

'''
$Rev: 548 $
$LastChangedBy: satoon101 $
$LastChangedDate: 2011-08-01 22:42:23 -0400 (Mon, 01 Aug 2011) $
'''

# =============================================================================
# >> IMPORTS
# =============================================================================
# GunGame Imports
from exceptions import ValidationError


# =============================================================================
# >> GLOBALS
# =============================================================================
__all__ = ['MinValueValidator', 'MaxValueValidator', 'MinLengthValidator',
           'MaxLengthValidator']


# =============================================================================
# >> CLASSES
# =============================================================================
class MinValueValidator(object):
    def __init__(self, value):
        self.value = value

    def __call__(self, check_value):
        if not check_value < self.value:
            return

        raise ValidationError('The given value (%s) must be ' % check_value +
                              'greater than or equal to %s.' % self.value)


class MaxValueValidator(object):
    def __init__(self, value):
        self.value = value

    def __call__(self, check_value):
        if not check_value > self.value:
            return

        raise ValidationError('The given value (%s) must be ' % check_value +
                              'less than or equal to %s.' % self.value)


class MinLengthValidator(object):
    """Validates that the length of a value is greater than or equal to the
    minimum.

    """
    def __init__(self, value):
        self.value = value

    def __call__(self, check_value):
        if len(check_value) < self.value:
            raise ValidationError('Ensure this value has at least ' +
                                  '%d characters (it has %d).' % (self.value,
                                  len(check_value)))


class MaxLengthValidator(object):
    """Validates that the length of a value is less than or equal to the
    minimum.

    """
    def __init__(self, value):
        self.value = value

    def __call__(self, check_value):
        if len(check_value) > self.value:
            raise ValidationError('Ensure this value has at most ' +
                                  '%d characters (it has %d).' % (self.value,
                                  len(check_value)))
