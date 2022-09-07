"""A module with Messaging utilities"""

from lib.crypto.factory import KeyFactory
from lib.crypto.types import KeyAlgorithm, PrivateKey

class MessagingService:
    """A service which provides messaging functionality"""

    def gen_key(self, algorithm: KeyAlgorithm) -> PrivateKey:
        """Generates a key of the specified type"""
        key = KeyFactory.create(algorithm)

        return key
