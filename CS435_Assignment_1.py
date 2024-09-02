import xml.etree.ElementTree as ET
import os

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



def parseXML(xml_file):

    #construct tree
    tree = ET.parse(xml_file)
    root = tree.getroot()

    #iterate over nodes in the tree
    for node in root.iter():
        print(node.tag, node.attrib)

parseXML(folder_path+xml_list[1])