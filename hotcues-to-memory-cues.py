# usage: python3 hotcues-to-memory-cues.py $XML_FILENAME

import xml.etree.ElementTree as ET
import sys

print('converting ' + sys.argv[1])

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for track in root.findall('./COLLECTION/TRACK'):
    for position in track.findall('POSITION_MARK'):
        start = position.get('Start')
        name = position.get('Name')
        # don't create duplicate mem cues
        if track.findall('./POSITION_MARK[@Num="-1"][@Start="' + start + '"]'):
            print('skipping: ' + track.get('Name'))
        else:
            print('processing: ' + track.get('Name'))
            child = ET.Element('POSITION_MARK')
            child.set('Name', name)
            child.set('Type', '0')
            child.set('Num', '-1')
            child.set('Start', start)
            track.append(child)

tree.write(sys.argv[2], encoding='UTF-8', xml_declaration=True)
