import unittest

from src.MeasureTime import MeasureTime


class MeasureTimeTest(unittest.TestCase):

    def testInit(self):
        sut = MeasureTime()
        self.assertIsInstance(sut, MeasureTime)

    def testIsReturnFromMeasureList(self):
        sut = MeasureTime().measure()
        self.assertIsInstance(sut, list)
