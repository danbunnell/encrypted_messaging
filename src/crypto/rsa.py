"""A module which provides RSA-based cryptography"""
from cryptography.hazmat.primitives.asymmetric.padding import (
    AsymmetricPadding, MGF1, OAEP
)
from cryptography.hazmat.primitives.asymmetric.rsa import (
    generate_private_key, RSAPublicKey as InternalPublicKey
)
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import (
    Encoding, PublicFormat, PrivateFormat, NoEncryption
)

class RSAConfigurationProvider:
    """Constant values used for RSA algorithms"""
    def get_encryption_padding(self) -> AsymmetricPadding:
        """The default padding scheme for RSA encryption"""
        return OAEP(
            mgf=MGF1(
                algorithm =SHA256()),
            algorithm=SHA256(),
            label=None)


class RSAPublicKey:
    """An RSA-based public, or verify, key"""

    def __init__(self, inner_key: InternalPublicKey, config):
        """Initializes a new instance of the `RSAPublicKey` class"""
        self.__key = inner_key
        self.__config = config

    def encrypt(self, data: bytes) -> bytes:
        """Encrypts the provided data"""
        return self.__key.encrypt(data, self.__config.get_encryption_padding())

    def to_bytes(self) -> bytes:
        """Prints the raw PEM-formatted key"""
        return self.__key.public_bytes(
            encoding=Encoding.PEM,
            format=PublicFormat.SubjectPublicKeyInfo)


class RSAPrivateKey:
    """An RSA-based private, or signing, key"""

    DEFAULT_ENCRYPTION_PADDING: AsymmetricPadding = OAEP
    """The default encryption padding scheme, OAEP is the highly recommended standard"""

    def __init__(self, public_exponent, key_size, config = RSAConfigurationProvider()):
        """Initializes a new instance of the RSAPrivateKey class"""
        self.__key = generate_private_key(
                public_exponent,
                key_size,
            )
        self.__config = config

    def decrypt(self, data: bytes) -> bytes:
        """Decrypts the provided data"""
        return self.__key.decrypt(data, self.__config.get_encryption_padding())

    def public_key(self) -> RSAPublicKey:
        """Returns the associated public key"""
        return RSAPublicKey(self.__key.public_key(), self.__config)

    def to_bytes(self) -> bytes:
        """Prints the raw PEM-formatted key"""
        return self.__key.private_bytes(
            encoding=Encoding.PEM,
            format=PrivateFormat.PKCS8,
            encryption_algorithm=NoEncryption())
