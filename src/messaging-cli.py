import sys

from docopt import docopt
from typing import List
from messaging import MessagingService, SignatureType

USAGE: str = """Secure Messaging.

Usage:
  messaging write alice <message>...
  messaging read alice
  messaging write bob <message>...
  messaging read bob
  messaging genkey [<algorithm>]
  messaging (-h | --help)
  messaging --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""

VERSION: str = '1.0.0'


def main(arguments: List[str]) -> None:
    args = docopt(USAGE, argv=arguments, version=VERSION)

    if args['genkey']:
      algorithm = args['<algorithm>']

      gen_key(algorithm)

def gen_key(algorithm: str) -> None:
  svc = MessagingService()

  svc.gen_key(SignatureType[algorithm])
  

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
