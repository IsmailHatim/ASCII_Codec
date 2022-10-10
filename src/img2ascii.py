import string
from PIL import Image, ImageOps, ImageFont, ImageDraw
from math import *
import numpy as np

SAMPLER_SIZE = 20
ASCII_SHADERS = " .:-=+*#%@"
FONT_PATH = "data/fonts/PIXEARG_.TTF"



def list_to_array(data : list) -> list:
    return [[data[i] for i in range(k*width,(k+1)*width) ] for k in range(0, height)]

class Sub_sampler:
    """The main class that permit to sample a High resolution image into a lower resolution with given size of sub_sampling
    """
    sampled_mat = []

    def __init__(self, size : int):
        self.size = size

    def sample(self, mat : list) -> Image.Image:
        mat = list_to_array(mat)
        for h in range(0,len(mat),self.size):
            moy = 0
            line = []
            for k in range(0,len(mat[0]),self.size):
                for i in range(0,self.size):
                    for j in range(0,self.size):
                        moy += mat[h+i][k+j]
                moy = moy/(self.size*self.size)
                line.append(int(moy))
            self.sampled_mat.append(line)
        return Image.fromarray(np.array(self.sampled_mat))

class Codec:
    """Class that permits to turn greyscales into ascii characters according to their value
    """
    txt = ""
    data = []

    def __init__(self, shader : string):
        self.shader = shader



    def imgtotext(self, data : list) -> string:
        txt = ""
        for i in range(0, len(data)):
            for j in range(0, len(data[0])):
                if data[i][j] < 25:
                    self.txt += self.shader[9]
                elif data[i][j] < 50 and data[i][j] > 25:
                    self.txt += self.shader[8]
                elif data[i][j] < 75 and data[i][j] > 50:
                    self.txt += self.shader[7]
                elif data[i][j] < 100 and data[i][j] > 75:
                    self.txt += self.shader[6]
                elif data[i][j] < 125 and data[i][j] > 100:
                    self.txt += self.shader[5]
                elif data[i][j] < 150 and data[i][j] > 125:
                    self.txt += self.shader[4]
                elif data[i][j] < 175 and data[i][j] > 150:
                    self.txt += self.shader[3]
                elif data[i][j] < 200 and data[i][j] > 175:
                    self.txt += self.shader[2]
                elif data[i][j] < 225 and data[i][j] > 200:
                    self.txt += self.shader[1]
                elif data[i][j] < 255 and data[i][j] > 225:
                    self.txt += self.shader[0]
            self.txt += "\n"    
        return self.txt

    def texttoimg(self, data : list) -> Image.Image:
                count = 0
                if self.txt=="":
                    self.imgtotext()
                image_fin = Image.new("L",(width,height))
                fnt = ImageFont.truetype(FONT_PATH, 40)
                d = ImageDraw.Draw(image_fin)

                for i in range(0,len(self.txt)):
                    if (self.txt[i]) == "\n":
                        count += 1
                    d.text((i*SAMPLER_SIZE,count*SAMPLER_SIZE), self.txt[i], fill = 255)
                
                return image_fin
            
        


with Image.open("data/img2.jpg") as img:
    img_cropped_grey = ImageOps.fit(img.convert("L"),(img.size[0]-img.size[0]%SAMPLER_SIZE,img.size[1]-img.size[1]%SAMPLER_SIZE))
    width = img_cropped_grey.size[0]
    height = img_cropped_grey.size[1]
    data = list(img_cropped_grey.getdata())


def main():
    

    sub_sampler = Sub_sampler(SAMPLER_SIZE)
    codec = Codec(ASCII_SHADERS)
    
    sampled_img = sub_sampler.sample(data)
    sampled_img.show()



    txt = codec.imgtotext(sub_sampler.sampled_mat)
    print(txt)
    codec.texttoimg(sub_sampler.sampled_mat).show()

main()

