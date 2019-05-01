import numpy as np
import sys
import xmltodict
from PIL import Image
import os

dir = sys.argv[1]
files = os.listdir(dir)
img_size = (500, 500)
class_dict={'background':0,
            'plane':1,
            'bike':2,
            'bird':3,
            'boat':4,
            'bottle':5,
            'bus':6,
            'car':7,
            'cat':8,
            'chair':9,
            'cow':10,
            'table':11,
            'dog':12,
            'horse':13,
            'motorbike':14,
            'person':15,
            'plant':16,
            'sheep':17,
            'sofa':18,
            'train':19,
            'monitor':20}
try:
    os.mkdir('images')
except:
    pass
for file in files:
    with open(os.path.join(dir,file)) as f:
        dict = xmltodict.parse(f.read())
        img_size = (int(dict['annotation']['size']['width']),int(dict['annotation']['size']['height']))
        img = np.full(img_size, 255)
        data = dict['annotation']['polygon']
        if not isinstance(data, list):
            data = [data]
        for items in data:
            try:
                id = class_dict[items['tag']]
            except:
                print(len(dict['annotation']['polygon']))
            points = items['point']
            if not isinstance(points, list):
                points = [points]
            for a in points:
                img[max(int(a['X'])-3,0):min(int(a['X'])+3,img_size[0]),max(int(a['Y'])-3,0):min(int(a['Y'])+3,img_size[1])] = int(id)

    im = Image.fromarray(np.uint8(img))
    im.save('images/'+dict['annotation']['filename'][:-3]+"png")
