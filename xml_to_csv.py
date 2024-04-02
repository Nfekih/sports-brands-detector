import os
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
  xml_list = []
  #xml_paths = os.listdir(path + '/*.xml')
  xml_paths = glob.glob(path + '/*.xml')
  for xml_file in xml_paths:
    print(xml_file)
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for member in root.findall('object'):
      value = (root.find('filename').text,
                int(root.find('size')[0].text),
                int(root.find('size')[1].text),
                member[0].text,
                int(member[4][0].text),
                int(member[4][1].text),
                int(member[4][2].text),
                int(member[4][3].text)
                )
      xml_list.append(value)
  column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
  xml_df = pd.DataFrame(xml_list, columns=column_name)
  return xml_df

def main(directory_list):
  for Image_cat in directory_list:
    print("loading ... ", Image_cat)
    image_path = os.path.join(os.getcwd(), 'images/{}'.format(Image_cat))
    print(image_path)
    xml_df = xml_to_csv(image_path) 
    xml_df.to_csv('data/{}_labels.csv'.format(Image_cat), index=None)
    print('Successfully converted xml to csv.')

main(['train','test'])