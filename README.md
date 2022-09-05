# Encrypted Messaging

This project explores encrypted messaging and related tools. 

This project contains self-implemented cryptography and while attempting to be correct, was not designed to meet rigorous security standards. Use at your own risk.

## TODO

- Implement PGP
- Implement `libsodium`

## Installation

```
brew install python3 watchman

python3 -m venv ~/.venvs/venv
source ~/.venvs/venv/bin/activate

pip install pyre-check
pip install pep8
pip install pylint
pip install docopt
pip install cryptography
```

## Using the CLI

```
# Generate an RSA key and print to terminal
python src/messaging_cli.py genkey RSA
```

## Running Tests

```
# enter src for proper pathing
cd src
python -m unittest discover tests # run all tests
python -m tests.test_messaging # run a specific test module
```