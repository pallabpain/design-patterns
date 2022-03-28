import abc
import hashlib


class Encryptor(object):
    """
    This is the Creator class
    """
    __metaclass__ = abc.ABCMeta

    def write_to_disk(self, plaintext, filename):
        encryption_algorithm = self.get_encryption_algorithm()
        ciphertext = encryption_algorithm.encrypt(plaintext)
        try:
            with open(filename, "w") as f:
                f.write(ciphertext)
        except Exception as err:
            print(err)

    @abc.abstractmethod
    def get_encryption_algorithm(self):
        pass


class EncryptionAlgorithm(object):
    """
    This is the Product class
    """
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def encrypt(self, plaintext):
        pass


class Sha256Encryptor(Encryptor):
    """
    This is a Concrete Creator class
    """
    def get_encryption_algorithm(self):
        return Sha256Algorithm()


class Sha512Encryptor(Encryptor):
    """
    This is another Concrete Creator
    """
    def get_encryption_algorithm(self):
        return Sha512Algorithm()


class Sha256Algorithm(EncryptionAlgorithm):
    """
    This is a Concrete Product class
    """
    def encrypt(self, plaintext):
        return hashlib.sha256(plaintext.encode()).hexdigest()


class Sha512Algorithm(EncryptionAlgorithm):
    """
    This is another Concrete Product class
    """
    def encrypt(self, plaintext):
        return hashlib.sha512(plaintext.encode()).hexdigest()


class PersistedFile(object):
    """
    This is a driver class
    """
    def __init__(self, path, contents, encryptor):
        if not isinstance(encryptor, Encryptor):
            raise TypeError(
                "{} is not a subclass of Encryptor".format(encryptor))
        self.path = path
        self.contents = contents
        self.encryptor = encryptor

    def persist(self):
        self.encryptor.write_to_disk(self.contents, self.path)


if __name__ == "__main__":
    persisted_file = PersistedFile(
        "file.txt", "Some text data", Sha512Encryptor()
    )
    persisted_file.persist()
