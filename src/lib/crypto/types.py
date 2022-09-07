"""A module which specifies cryptographic types"""

from abc import ABC, abstractmethod
from enum import Enum

class KeyAlgorithm(Enum):
    """A cryptographic key algorithm"""

    ED22519 = 1
    """The Edwards-curve Digital Signature Algorithm using elliptical curve Curve25519,\
    provides smaller keys and faster crypto, recommended to use where supported. Can   \
    only be used for signing."""

    RSA = 2
    """The Rivest-Shamir-Adleman algorithm, relies on integer factorization, most      \
    widely used, but requires larger key sizes (2048+ bits) to be secure, and provides \
    slower key generation. Can be used for signing and encryption."""

    ECDSA = 3
    """An elliptical curve Digitial Signature Algorithm which may be vulnerable to     \
    insufficient randomization in the RNG, but is the most commonly supported ECC      \
    algorithm used for TLS. Can only be used for signing."""

class PublicKey(ABC):
    """An abstract class which provides the interface to a generic cryptographic public key"""
    @abstractmethod
    def to_bytes(self) -> bytes:
        """Prints the raw PEM-formatted key"""

class PrivateKey(ABC):
    """An abstract class which provides the interface to a generic cryptographic private key"""
    @abstractmethod
    def public_key(self) -> PublicKey:
        """Returns the associated public key"""

    @abstractmethod
    def to_bytes(self) -> bytes:
        """Prints the raw PEM-formatted key"""
