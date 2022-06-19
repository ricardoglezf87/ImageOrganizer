#Imports

import datetime
from PIL import Image
import os
import time

#variables globales

INICIAL_PATH = r"C:\Users\rgonzalez.348SERVICIOS\OneDrive - INNI\Escritorio\Nueva carpeta"
FINAL_PATH = r"C:\Users\rgonzalez.348SERVICIOS\OneDrive - INNI\Escritorio\Nueva carpeta2"

#Funtions

def get_date_taken(path):
    t = time.strptime(Image.open(path)._getexif()[36867], "%Y:%m:%d %H:%M:%S")
    return datetime.date.fromtimestamp(time.mktime(t))

def get_date_created(path):
    return datetime.date.fromtimestamp(os.path.getctime(path))

def get_date_modified(path):
    return datetime.date.fromtimestamp(os.path.getmtime(path))

def is_image(path):
    try:
        Image.open(path)
    except IOError:
        return False
    return True

def get_date(path):

    dates = []
    if not is_image(path):
        dates.append(datetime.date.today())
        dates.append(get_date_created(path))
        dates.append(get_date_modified(path))
    else:
        try:
            dates.append(get_date_taken(path))
        except:
            dates.append(datetime.date.today())

        dates.append(get_date_created(path))
        dates.append(get_date_modified(path))
    return min(dates)

def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def move_file(path,path_new):
    if not os.path.isfile(path_new):
        os.rename(path,path_new)

def find_images(dirPath):
    files = [f for f in os.listdir(dirPath)]
    for fil in files:
        if not os.path.isfile(os.path.join(dirPath, fil)):
            find_images(os.path.join(dirPath, fil))
        else:
            d = get_date(os.path.join(dirPath, fil))
            create_folder(os.path.join(FINAL_PATH, str(d.year), str(d.month)))
            move_file(os.path.join(dirPath, fil),os.path.join(FINAL_PATH, str(d.year), str(d.month), fil))
            print(fil + " --> " + str(d.day) + "/" + str(d.month) + "/" + str(d.year))

# function Main
if __name__ == '__main__':
    find_images(INICIAL_PATH)


