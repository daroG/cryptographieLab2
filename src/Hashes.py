import hashlib as hl
import os
from typing import Optional


class Hashes:

    def __init__(self):
        pass

    @staticmethod
    def hashUsingAllAvailableAlgorithms(text: str, encode: bool = True) -> dict:
        """
        Method hashing given text (or bytesarray) using all available algorithms
        :param text: str
        :param encode: bool
        :return: dict
        """

        if len(text) == 0:
            return {}

        hashesOfText = dict.fromkeys(hl.algorithms_guaranteed)

        for alg in hl.algorithms_guaranteed:
            h = hl.new(alg)
            if encode:
                h.update(text.encode())
            else:
                h.update(text)
            if alg.startswith('shake_'):
                hashesOfText[alg] = h.hexdigest(64)
            else:
                hashesOfText[alg] = h.hexdigest()

        return hashesOfText

    @staticmethod
    def hashFileFromDisk(path: str) -> Optional[str]:
        """
        Method returning hash of file in given path
        None is return when no file in given path
        :param path: str
        :return: str|None
        """

        sha256 = hl.sha256()

        if os.path.exists(path):
            with open(path, 'rb') as file:
                while True:
                    data = file.read(65536)
                    if not data:
                        break
                    sha256.update(data)

            return sha256.hexdigest()

        return None
