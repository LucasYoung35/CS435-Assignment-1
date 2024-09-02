import xml.etree.ElementTree as ET
import os

from PIL import Image
from PIL import ImageDraw

#function to parse through xml file and find leaf nodes with a bounds attribute
#takes xml file path as parameter and returns a list of integers containing information about bounding boxes
def parseXML(xml_file):

    bounding_boxes = []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    for node in root.iter():

        #check if node is a leaf and has bounds attribute
        if len(node) == 0 and node.attrib.get('bounds') is not None:
            bounds = node.attrib.get('bounds')

            #clean up bounding boxes and convert to integers
            bounds = bounds.replace('][', ' ').replace(',', ' ').replace('[', '').replace(']','')
            bounding_boxes.append(list(map(int, bounds.split(' '))))

    return bounding_boxes

#function to draw a rectangle using the Pillow library
#takes image file path and bounding boxes as parameters and saves modified image as png
def drawBox(image, bounding_boxes):

    with Image.open(image) as im:

        for bounds in bounding_boxes:

            box = (bounds[0], bounds[1], bounds[2], bounds[3])
            img1 = ImageDraw.Draw(im)   
            img1.rectangle(box, outline="yellow", width=5)


        try:
            im.save('test.png')
        except OSError:
            print("cannot convert")


def main():

    #path to xml and png files
    folder_path = '.\Programming-Assignment-Data\\'
    dir_list = os.listdir(folder_path)

    #sort xml and png files
    xml_list = []
    png_list = []

    for f in dir_list:
        if f.endswith(".xml"):
            xml_list.append(f)
        else:
            png_list.append(f)

    drawBox(folder_path+png_list[1], parseXML(folder_path+xml_list[1]))



if __name__=="__main__":
    main()