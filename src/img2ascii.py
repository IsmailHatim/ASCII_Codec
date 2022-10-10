from PIL import Image,ImageOps
from math import *

SAMPLER_SIZE = 10

def list_to_array(data : list):
    return [([data[i] for i in range(k*width,(k+1)*width) ]) for k in range(0, height)]

def array_to_list(data : list):
    ulist = []
    for i in range(0,len(data)):
        for j in range(0,len(data[0])):
            ulist.append()


class Sub_sampler:
    def __init__(self, mat : list, size : int):
        self.mat = mat
        self.size = size

    def sample(self) -> list:
        sampled_mat = []
        for h in range(0,len(self.mat),self.size):
            moy = 0
            line = []
            for k in range(0,len(self.mat[0]),self.size):
                for i in range(0,self.size):
                    for j in range(0,self.size):
                        moy += self.mat[h+i][k+j]
                moy = moy/(self.size*self.size)
                line.append(moy)
            sampled_mat.append(line)
        return sampled_mat

with Image.open("data/img.jpg") as img:
    img_cropped_grey = ImageOps.fit(img.convert("L"),(img.size[0]-img.size[0]%SAMPLER_SIZE,img.size[1]-img.size[1]%SAMPLER_SIZE))
    width = img_cropped_grey.size[0]
    height = img_cropped_grey.size[1]
    
    data = list(img_cropped_grey.getdata())


(ImageOps.fit(img.convert("L"),(width,height))).show()

data = list_to_array(data)

sub_sampler = Sub_sampler(data,SAMPLER_SIZE)

sampled_data = sub_sampler.sample()

ascii = " .:s%@"
print(data)
print(sampled_data)

#sampled_data = array_to_list(sampled_data)

sampled_img = Image.fromarray(sampled_data)
