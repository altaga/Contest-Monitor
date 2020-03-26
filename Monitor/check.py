from selenium import webdriver
from time import sleep
import cv2
import time
import webbrowser
import argparse

parser = argparse.ArgumentParser(description='Test.')
parser.add_argument('url', action='store', type=str, help='The text to parse.')

args = parser.parse_args()


url = args.url

driver = webdriver.Firefox()
driver.get(url)
sleep(1)
driver.get_screenshot_as_file("screenshotmem.png")

counter=time.time()
timer=time.time()

try:
    while 1:
        counter=time.time()-timer
        while(counter > 60):
            driver.get(url)
            sleep(1)
            driver.get_screenshot_as_file("screenshot.png")
            
            # load images
            image1 = cv2.imread("screenshotmem.png")
            image2 = cv2.imread("screenshot.png")

            # compute difference
            difference = cv2.subtract(image1, image2)

            i=0
            j=0
            dif=0
            for i in range(len(difference)):
                for j in range(len(difference[i])):
                    dif=dif + difference[i][j][0]
                    dif=dif + difference[i][j][1]
                    dif=dif + difference[i][j][2]
            print(dif)
            if(dif!=0):
                print("Results have been published!")
                webbrowser.open(url, new=2)
                raise KeyboardInterrupt
            timer=time.time()
            break
            
except KeyboardInterrupt:
    driver.quit()
    print("end...")