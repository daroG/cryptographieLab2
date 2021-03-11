import timeit
import plotly.graph_objects as go


class MeasureTime:


    def measure(self):
        """
        Method for measure time of hashing different length messages using all available hashing algorithms
        :return: list
        """
        setup = '''
from src.Hashes import Hashes
import os
array = [bytearray(os.urandom(int((10 ** 7) * i / 20))) for i in range(20)]
        '''
        return [timeit.timeit(setup=setup,
                              stmt='Hashes().hashUsingAllAvailableAlgorithms(array[{}], False)'.format(i),
                              number=1)
                for i in range(20)]

    def makeChart(self):
        """
        Method drawing chart from result got from measure method
        :return: Void
        """
        fig = go.Figure(data=go.Scatter(x=[int((10 ** 7) * i / 20) for i in range(20)], y=self.measure()))
        fig.update_layout(xaxis_title="Length", yaxis_title="time")

        fig.show()
