# import xml.dom.ext
import xml.dom.minidom

# <entry type="song">
#     <title>Nightcall</title>
#     <genre>Soundtrack</genre>
#     <artist>Kavinsky &amp; Lovefoxxx</artist>
#     <album>Drive (Original Motion Picture Soundtrack)</album>
#     <track-number>1</track-number>
#     <duration>259</duration>
#     <file-size>4191454</file-size>
#     <location>file:///home/martin/Music/01%20-%20Kavinsky%20&amp;%20Lovefoxxx%20-%20Nightcall.mp3</location>
#     <mtime>1327228704</mtime>
#     <first-seen>1342816661</first-seen>
#     <last-seen>1342816661</last-seen>
#	  <rating>5</rating>
#     <play-count>1</play-count>
#     <last-played>1342817082</last-played>
#     <bitrate>128</bitrate>
#     <date>734138</date>
#     <media-type>audio/mpeg</media-type>
#   </entry>

#ifile = open('/home/martin/drive/repos/parseTestFile.xml')
#rdbfile = open('/home/martin/drive/repos/rhythmdbTest.xml')
ifile = open('/home/martin/drive/repos/ilib.xml')
rdbfile = open('/home/martin/drive/repos/rhythmdb.xml')

newdb = open('/home/martin/drive/repos/newdb.xml', 'r+')

#itfile = ifile.read()

ixml = xml.dom.minidom.parseString(ifile.read())
rdxml = xml.dom.minidom.parseString(rdbfile.read())

#ifile.close()

doc = xml.dom.minidom.Document()

def chopDow():
    alliSongs = ixml.getElementsByTagName('dict')[0].getElementsByTagName('dict')[0]
    for isong in alliSongs.getElementsByTagName('dict'):
        relevant = False
        for i in isong.getElementsByTagName('key'):
            if i.toxml() == '<key>Rating</key>' or i.toxml() == '<key>Play Count</key>':
                relevant = True
                break
        if not relevant:
            alliSongs.removeChild(isong)


def handleSongs():
    chopDow()
    rhythm = doc.createElementNS("rhythmdb","rhythmdb")
    doc.appendChild(rhythm)
    song = doc.createElementNS("entry", "entry")
    rhythm.appendChild(song)
    allRSongs = rdxml.getElementsByTagName('rhythmdb')[0]
    alliSongs = ixml.getElementsByTagName('dict')[0].getElementsByTagName('dict')[0]
    foundi = False
    count = 0
    for rsong in allRSongs.getElementsByTagName('entry'):
        if rsong.getElementsByTagName('file-size') != []:
            rsongSizeTag = rsong.getElementsByTagName('file-size')[0]
            rsongSize = rsongSizeTag.childNodes[0].toxml()
        else:
            rsongSize = '-1'
            print "fuckyoumaddafakkasssszzz"
        foundi = False
        count = count + 1
        print count
        relevant = False
        for isong in alliSongs.getElementsByTagName('dict'):
            for i in isong.getElementsByTagName('key'):
                if i.toxml() == "<key>Size</key>":
                    if i.nextSibling.childNodes[0].toxml() == rsongSize:
                        foundi = True
                        for j in isong.getElementsByTagName('key'):
                            if j.toxml() == '<key>Rating</key>' and rsong.getElementsByTagName('rating') == []:
                                temp = doc.createTextNode(convertRating(j.nextSibling.childNodes[0].toxml()))
                                rating = doc.createElement('rating')
                                rating.appendChild(temp)
                                rsong.insertBefore(rating, rsongSizeTag)
                            elif j.toxml() == '<key>Play Count</key>' and rsong.getElementsByTagName('play-count') == []:
                                temp = doc.createTextNode(j.nextSibling.childNodes[0].toxml())
                                play = doc.createElement('play-count')
                                play.appendChild(temp)
                                rsong.insertBefore(play, rsongSizeTag)
                    break
            if foundi:
                alliSongs.removeChild(isong)
                break
    print ""
    print rdxml.toxml()
    print ""
    newdb.write(rdxml.toxml())
    newdb.close()

def convertRating(rating):
    if rating == '100':
        return '5'
    elif rating == '80':
        return '4'
    elif rating == '60':
        return '3'
    elif rating == '40':
        return '2'
    elif rating == '20':
        return '1'
    else:
        return '1'

handleSongs()
