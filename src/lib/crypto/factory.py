"""A module which provides factory utilities for cryptographic types"""
from lib.crypto.rsa import RSAPrivateKey
from lib.crypto.types import KeyAlgorithm, PrivateKey

class KeyFactory:
    """A factory which produces cryptographic keys"""
    DEFAULT_EXPONENT: int = 65537
    """The default exponent for use in key generation"""

    DEFAULT_KEY_SIZE: int = 4096
    """The default key size in bits for generation, only 2048+ is considered secure"""

    @staticmethod
    def create(algorithm: KeyAlgorithm) -> PrivateKey:
        """Creates a cryptographic key pair based on the specified algorithm"""

        if algorithm == KeyAlgorithm.RSA:
            key = RSAPrivateKey(KeyFactory.DEFAULT_EXPONENT, KeyFactory.DEFAULT_KEY_SIZE)
        else:
            raise ValueError(f"Algorithm not supported: {algorithm}")

        return key
