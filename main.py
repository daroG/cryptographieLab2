from src.Hashes import Hashes
from src.MeasureTime import MeasureTime


if __name__ == '__main__':
    print(Hashes().hashUsingAllAvailableAlgorithms("Darek"))

    print(Hashes().hashFileFromDisk("D:\\Pobrane\\ubuntu-20.04.2.0-desktop-amd64.iso"))

    MeasureTime().makeChart()
