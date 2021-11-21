from PIL import Image
import numpy as np

class Filter():
    """
    Return average bright
    :param y: start y coord
    :param x: start x coord
    :return: average bright
    >>> Filter._Filter__GetAverage(filtr,0, 0)
    0
    """
    def __GetAverage(self, y, x):
        average = np.sum((self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size]))
        return int(average // (self.mosaic_size*self.mosaic_size))

    """
    Set array pixels to gray
    :param y: start y coord
    :param x: start x coord
    """
    def __DoGray(self, y, x):
        average = self.__GetAverage(y, x)
        self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size] = int(average // self.grayscale) * self.grayscale/3

    """
    Save result to .jpg
    """
    def __SaveResult(self):
        res = Image.fromarray(self.arr)
        res.save(input("Введите новое название изображения: "))

    """
    Start filter
    """
    def StartFilter(self):
        self.img = Image.open(input("Введите название изображение: "))
        self.arr = np.array(self.img)
        self.mosaic_size = int(input("Введите размер мозайки: "))
        self.grayscale = int(input("Введите размер шага градации серого: "))

        height, width = len(self.arr), len(self.arr[1])
        for y in range(0, height, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                self.__DoGray(y, x)

        self.__SaveResult()

filtr = Filter()
filtr.StartFilter()

if __name__ == "__main__":
    import doctest
    doctest.testmod()