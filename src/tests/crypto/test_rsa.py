"""Tests the RSA module"""
import unittest

from lib.crypto.rsa import RSAPrivateKey

class RsaTest(unittest.TestCase):
    """The RSA test class"""

    def test_message_encryption(self):
        """Tests for correct message encryption"""
        private_key = RSAPrivateKey(public_exponent=65537, key_size=1024)

        expected_message = b"Hey Bob, it's me Alice. How are you?"
        ciphertext = private_key.public_key().encrypt(expected_message)

        output_message = private_key.decrypt(ciphertext)

        self.assertEqual(expected_message, output_message)

if __name__ == '__main__':
    unittest.main()
