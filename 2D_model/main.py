# some_file.py
from box import box
from cargo import cargo
from model2D_versione2 import model2D
import random

def main():
    packages =[]
    for i in range(7):
        w=random.randint(40,50)
        d=random.randint(40,50)
        packages.append(box([w,d]))

    camion =cargo([90,100])
    model2D(packages,camion)

if __name__ == "__main__":
    main()