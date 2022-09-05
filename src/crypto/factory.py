"""A module which provides factory utilities for cryptographic types"""
from crypto.rsa import RSAPrivateKey
from crypto.types import KeyAlgorithm

class KeyFactory:
    """A factory which produces cryptographic keys"""
    DEFAULT_EXPONENT: int = 65537
    """The default exponent for use in key generation"""

    DEFAULT_KEY_SIZE: int = 4096
    """The default key size in bits for generation, only 2048+ is considered secure"""

    @staticmethod
    def create(algorithm: KeyAlgorithm) -> RSAPrivateKey:
        """Creates a cryptographic key pair based on the specified algorithm"""

        KeyFactory.__validate_algorithm(algorithm)
        key = RSAPrivateKey(KeyFactory.DEFAULT_EXPONENT, KeyFactory.DEFAULT_KEY_SIZE)
        
        return key

    @staticmethod
    def __validate_algorithm(algorithm: KeyAlgorithm) -> None:
        """Validates the key algorithm requested for generation"""
        if algorithm == KeyAlgorithm.RSA:
            return

        raise ValueError(f"Algorithm not supported: {algorithm}")
