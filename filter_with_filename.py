from PIL import Image
import numpy as np

class Filter():
    def __GetAverage(self, y, x):
        average = np.sum((self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size]))
        return int(average // (self.mosaic_size*self.mosaic_size))

    def __DoGray(self, y, x):
        average = self.__GetAverage(y, x)
        self.arr[y: y + self.mosaic_size, x: x + self.mosaic_size] = int(average // self.grayscale) * self.grayscale/3

    def __SaveResult(self):
        res = Image.fromarray(self.arr)
        res.save("output2.jpg")

    def StartFilter(self):
        self.arr = np.array(Image.open("input.py"))
        self.mosaic_size = 10
        self.grayscale = 50

        height, width = len(self.arr), len(self.arr[1])
        for y in range(0, height, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                self.__DoGray(y, x)

        self.__SaveResult()

filtr = Filter()
filtr.StartFilter()
