"""Tests for the messaging module"""
import unittest


from unittest import TestCase

from crypto.rsa import RSAPrivateKey
from crypto.types import KeyAlgorithm
from messaging import MessagingService

class MessagingTest(TestCase):
    """Tests for the Messaging module"""

    def test_base(self):
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

    def test_message_encryption(self):
        """Tests for correct message encryption using RSA"""
        svc = MessagingService()

        private_key = svc.gen_key(KeyAlgorithm["RSA"])

        expected_message = b"Hey Bob, it's me Alice. How are you?"
        ciphertext = private_key.public_key().encrypt(expected_message)

        output_message = private_key.decrypt(ciphertext)

        self.assertEqual(expected_message, output_message)


if __name__ == '__main__':
    unittest.main()
