"""The Messaging command-line interface"""

import sys
from typing import List

from docopt import docopt
from lib.crypto.types import KeyAlgorithm
from lib.messaging import MessagingService

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
    """The program entry point"""
    options = docopt(USAGE, argv=arguments, version=VERSION)

    if options['genkey']:
        algorithm = options['<algorithm>']

        gen_key(algorithm)
    elif options['write']:
        raise NotImplementedError("write command not yet implemented")
    elif options['read']:
        raise NotImplementedError("read command not yet implemented")
    else:
        raise ValueError("unexpected arguments")


def gen_key(algorithm_name: str) -> None:
    """Generate a key using the specified algorithm"""
    algorithm = __parse_algorithm(algorithm_name)

    svc = MessagingService()
    key = svc.gen_key(algorithm)
    print(key.to_bytes())

def __parse_algorithm(input_value: str) -> KeyAlgorithm:
    valid_values = [algorithm.name for algorithm in KeyAlgorithm]
    if input_value not in valid_values:
        raise ValueError(
            f"Unexpected algorithm '{input_value}', expected one of: {valid_values}")

    return KeyAlgorithm[input_value]

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
