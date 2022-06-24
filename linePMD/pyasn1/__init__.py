import sys

__version__ = '0.4.8'

if sys.version_info[:2] < (2, 4):
    raise RuntimeError('Requires Python 2.4 or later')
