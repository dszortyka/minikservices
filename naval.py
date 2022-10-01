"""Naval Fate.

Usage:
  kservice start (<services>)...
  kservice stop (<services>)...
  kservice (--left | --right) (<services>)...
  naval_fate.py mine (set|remove) <x> <y> [--moored | --drifting]
  kservice (-h | --help)


Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)