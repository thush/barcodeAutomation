from BarcodeDriver import BarcodeDriver
from TagParser import TagParser


"""
 | **getBitMapFileName**:
 |  1. Input Barcode TagId names
 |  2. Return: BarCodeFile as on BaroodeMapper
 |  3. Please verify with the BarCodeMap.xml
 """

def getBitMapFileName(tagParser, tagId):
    return tagParser.getElinkFile(tagId)


"""
 | **sendBarCode(<BarcodeTag>)**:
 |  1. Input <BTag> name
 |  2. Return: BarCodeFile as on BaroodeMapper
 |  3. Please verify with the BarCodeMap.xml
 |  4. sendBarCode() called from ClientEnd
  
 """

def sendBarCode(BarcodeTag):
    xmlParser = TagParser('Barcode_Map.xml')
    image = getBitMapFileName(xmlParser, BarcodeTag)
    if image == '':
        print("Failed to parse with given TagID")
        return -1



    print("Show bar code")
    bCodeDrv = BarcodeDriver()
    if bCodeDrv.showBarcode(image) == 0:
        print("Success")
        return 0
    else:
        print("Failed to show barcode")
        return -1




sendBarCode('B5')

"""     
 | **packData(<DataPacket>)**:
 |  1. Input <dataChunk Array> 
 |  2. Return: Packet packed
 |  3. Please verify with the Packet struct defined on DataPacket.py
 """


"""
 | **packData(<CommandPacket>)**:
 |  1. Input <CommandPacket Parameters> 
 |  2. Return: Packet packed
 |  3. Please verify with the Packet struct defined on CommandPacket.py
 """