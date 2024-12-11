import cv2
import imghdr
from matplotlib import pyplot as plt
import os


dataDir = 'trainingData'

possibleExtensions = ['jpeg', 'jpg', 'bmp', 'png']

for imgClass in os.listdir(dataDir):

    for img in os.listdir(os.path.join(dataDir, imgClass)):

        imgPath = os.path.join(dataDir, imgClass, img)

        try: 
            imgn = cv2.imread(imgPath)   
            tip = imghdr.what(imgPath)

            if tip not in possibleExtensions:
                print(f"Images with such extension are not allowed\n  (only {possibleExtensions})")
                os.remove(imgPath)
                
        except Exception as ex:
            print(f"unusual issue with image {imgPath}")
            os.remove(imgPath)

print("all unsuitable images where removed")
