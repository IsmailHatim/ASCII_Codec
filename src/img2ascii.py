from PIL import Image,ImageOps
from math import *
import numpy as np

SAMPLER_SIZE = 10
ASCII_SHADERS = " .:s%@"



def list_to_array(data : list) -> list:
    return [[data[i] for i in range(k*width,(k+1)*width) ] for k in range(0, height)]

class Sub_sampler:
    """The main class that permit to sample a High resolution image into a lower resolution with given size of sub_sampling

    """
    sampled_mat = []

    def __init__(self, mat : list, size : int):
        self.mat = list_to_array(mat)
        self.size = size

    def sample(self) -> Image.Image:
        for h in range(0,len(self.mat),self.size):
            moy = 0
            line = []
            for k in range(0,len(self.mat[0]),self.size):
                for i in range(0,self.size):
                    for j in range(0,self.size):
                        moy += self.mat[h+i][k+j]
                moy = moy/(self.size*self.size)
                line.append(int(moy))
            self.sampled_mat.append(line)
        return Image.fromarray(np.array(self.sampled_mat))

with Image.open("data/img.jpg") as img:
    img_cropped_grey = ImageOps.fit(img.convert("L"),(img.size[0]-img.size[0]%SAMPLER_SIZE,img.size[1]-img.size[1]%SAMPLER_SIZE))
    width = img_cropped_grey.size[0]
    height = img_cropped_grey.size[1]
    
    data = list(img_cropped_grey.getdata())


def main():
    (ImageOps.fit(img.convert("L"),(width,height))).show()

    sub_sampler = Sub_sampler(data,SAMPLER_SIZE)

    sampled_img = sub_sampler.sample()

    sampled_img.show()

    


main()

