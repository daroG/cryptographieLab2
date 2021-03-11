import unittest

from src.Hashes import Hashes


class HashesTest(unittest.TestCase):

    def testInit(self):
        sut = Hashes()
        self.assertIsInstance(sut, Hashes)

    def testIsReturnFromHashUsingAllAvailableAlgorithmsDictionary(self):
        sut = Hashes().hashUsingAllAvailableAlgorithms("a")
        self.assertIsInstance(sut, dict)

    def testIsEmptyDictionaryWhenStringHasNoChars(self):
        sut = Hashes().hashUsingAllAvailableAlgorithms("")
        self.assertIsInstance(sut, dict)
        self.assertDictEqual(sut, {})
