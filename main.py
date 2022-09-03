from docopt import docopt

doc: str = """Secure Messaging.

Usage:
  messaging write new <name>...
  messaging ship <name> move <x> <y> [--speed=<kn>]
  messaging ship shoot <x> <y>
  messaging mine (set|remove) <x> <y> [--moored | --drifting]
  messaging (-h | --help)
  messaging --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  --speed=<kn>  Speed in knots [default: 10].
  --moored      Moored (anchored) mine.
  --drifting    Drifting mine.

"""

def main():
    arguments: dict[str, any] = docopt(doc, version='Naval Fate 2.0')
    print(arguments)

if __name__ == '__main__':
    main()
