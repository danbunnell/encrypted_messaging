"""Tests for the messaging module"""
import unittest


from unittest import TestCase

from lib.crypto.rsa import RSAPrivateKey
from lib.crypto.types import KeyAlgorithm
from lib.messaging import MessagingService

class MessagingTest(TestCase):
    """Tests for the Messaging module"""

    def test_genkey_rsa(self):
        """Test that `gen_key()` can produce a basic RSA key"""
        svc = MessagingService()

        key = svc.gen_key(KeyAlgorithm["RSA"])

        self.assertIsNotNone(key)
        self.assertIsInstance(key, RSAPrivateKey)

    def test_gen_key_unsupported_algorithm(self):
        """Verify that `gen_key()` raises an error for unsupported key algorithms"""
        svc = MessagingService()

        with self.assertRaises(ValueError):
            svc.gen_key(KeyAlgorithm["ED22519"])


if __name__ == '__main__':
    unittest.main()
