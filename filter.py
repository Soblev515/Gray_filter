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
        new_img_name = input("Введите новое название изображения: ") 
        res = Image.fromarray(self.arr)
        res.save(new_img_name)

    def __OpenImage(self):
        img = Image.open(input("Введите название изображение: "))
        self.arr = np.array(img)

    def __SetMosaicSize(self):
        mosaic_size = int(input("Введите размер мозайки: "))
        self.mosaic_size = mosaic_size

    def __SetGrayscale(self):
        grayscale = int(input("Введите размер шага градации серого: "))
        self.grayscale = grayscale
                
    def StartFilter(self):
        self.__OpenImage()
        self.__SetMosaicSize()
        self.__SetGrayscale()
        
        height, width = len(self.arr), len(self.arr[1])
        for y in range(0, height, self.mosaic_size):
            for x in range(0, width, self.mosaic_size):
                self.__DoGray(y, x)
                
        self.__SaveResult()

filtr = Filter()
filtr.StartFilter()
