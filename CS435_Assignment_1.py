import xml.etree.ElementTree as ET
import os

#function to parse through xml file and find leaf nodes with a bounds attribute
#returns a list of integers containing information about bounding boxes
def parseXML(xml_file):

    bounding_boxes = []

    tree = ET.parse(xml_file)
    root = tree.getroot()

    #iterate over nodes in the tree
    for node in root.iter():

        #check if node is a leaf and has bounds attribute
        if len(node) == 0 and node.attrib.get('bounds') is not None:
            bounds = node.attrib.get('bounds')

            #clean up bounding boxes and convert to integers
            bounds = bounds.replace('][', ' ').replace(',', ' ').replace('[', '').replace(']','')
            bounding_boxes.append(list(map(int, bounds.split(' '))))

    return bounding_boxes


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

    print(parseXML(folder_path+xml_list[1]))


if __name__=="__main__":
    main()