"""A module with Messaging utilities"""

from crypto.factory import KeyFactory
from crypto.rsa import RSAPrivateKey
from crypto.types import KeyAlgorithm

class MessagingService:
    """A service which provides messaging functionality"""
    RSA_EXPONENT: int = 65537
    RSA_KEY_SIZE: int = 2048

    def gen_key(self, algorithm: KeyAlgorithm) -> RSAPrivateKey:
        """Generates a key of the specified type"""
        key = KeyFactory.create(algorithm)

        return key
