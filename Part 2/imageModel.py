## This is the abstract class that the students should implement  


import numpy as np
import cv2 as cv
import numpy as np
# from main import ApplicationWindow


class ImageModel():
    """
    A class that represents the ImageModel"
    """

    def __init__(self):
        pass

    def __init__(self, imgPath: str):
        self.imgPath = imgPath
        ###
        # ALL the following properties should be assigned correctly after reading imgPath
        ###
        self.imgByte = cv.cvtColor(cv.imread(self.imgPath), cv.COLOR_BGR2GRAY)
        self.dft = np.fft.fft2(self.imgByte)
        self.real = np.real(self.dft)
        self.imaginary = np.imag(self.dft)
        self.magnitude = np.abs(self.dft)
        self.phase = np.angle(self.dft,deg=False)

