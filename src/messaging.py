"""A module with Messaging utilities"""

from crypto.factory import KeyFactory
from crypto.rsa import RSAPrivateKey
from crypto.types import KeyAlgorithm

class MessagingService:
    """A service which provides messaging functionality"""

    def gen_key(self, algorithm: KeyAlgorithm) -> RSAPrivateKey:
        """Generates a key of the specified type"""
        key = KeyFactory.create(algorithm)

        return key
