from abc import ABCMeta
from multiprocessing.sharedctypes import Value
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption
from enum import Enum


class SignatureType(Enum):
    ED22519 = 1
    RSA = 2


class MessagingService:
    RSA_EXPONENT: int = 65537
    RSA_KEY_SIZE: int = 2048

    def gen_key(self, type: SignatureType):
        private_key = MessagingService._get_key_type(type)

        bytes = private_key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption())

        print(bytes)

    @staticmethod
    def _get_key_type(type: SignatureType):
        if type == SignatureType.ED22519:
            return Ed25519PrivateKey.generate()
        elif type == SignatureType.RSA:
            return rsa.generate_private_key(
                public_exponent=MessagingService.RSA_EXPONENT,
                key_size=MessagingService.RSA_KEY_SIZE,
            )
        else:
            raise ValueError("Invalid key algorithm: ${type}")
