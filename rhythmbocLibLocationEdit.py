import xml.dom.minidom


#rdbfileOld = open('/home/m/drive/repos/rhythmdb.xml')
#rdbfileNew = open('/home/m/drive/repos/newdb.xml', 'r+')

rdbfileOld = open('/home/m/Insync/mcmhav@gmail.com/repos/ParseXMLRIDB/parseTestFile.xml')
rdbfileNew = open('/home/m/Insync/mcmhav@gmail.com/repos/ParseXMLRIDB/newdb.xml', 'r+')


old = xml.dom.minidom.parseString(rdbfileOld.read())


new = xml.dom.minidom.parseString(ifile.read())


def editor():
    for i in old.getgetElementsByTagName('location'):
        print i
