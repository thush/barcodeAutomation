import xml.etree.ElementTree as ET


"""
 | **TagParser**Class
 |  1. Tag Parser tree with ElementTree
 |  2. BaroodeMap.xml Path has to be given with RelativePath
 |  3. Please verify with the BarCodeMap.xml
 """

#tree = ET.parse('..', 'Barcode_Map.xml')
#tree = ET.parse('Barcode_Map.xml')

# root = tree.getroot()

class TagParser:
    def __init__(self, path):
        self.__path = path
        self.__tree = ET.parse(self.__path)
        self.root = self.__tree.getroot()

    def getElinkFile(self, tagName):
        eLinkFile = None

        bTag = self.root.find(tagName)
        if bTag is not None:
            eLinkFileTag = bTag.find('eInkFile')
            if eLinkFileTag is not None:
                eLinkFile = eLinkFileTag.get('name').strip()

        return eLinkFile


if __name__ == '__main__':
    tagParser = TagParser('../Barcode_Map.xml')
    print tagParser.getElinkFile('B1')