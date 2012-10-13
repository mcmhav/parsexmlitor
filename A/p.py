#from xml.dom.minidom import parse, parseString

#t = parseString('/home/cube/Desktop/test.xml')

#d = open('/home/cube/Desktop/test.xml')

#t2 = parse(d)

from xml.dom.minidom import parse

dom = parse('/home/cube/Desktop/rhythmdb-old.xml')

true = 1
false = 0


def t2(dom):
    x = dom.createElement("play-count")
    txt = dom.createTextNode("1")
    x.appendChild(txt)
    dom.getElementsByTagName("hackmal")[0]
    dom.childNodes[0].appendChild(x)
    print dom.toxml()


def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)


def test(t):
    ht(t.getElementsByTagName("slide")[0])


def ht(s):
    print "<la>%s</la>" % getText(s.childNodes)
    print "test"


def handleSlideshow(slideshow):
    print "<html>"
    slideshow.createAttribute('<test>')
    slideshow.createElement('<test2>')
#    print "<play-count>1</play-count>" #% getText(slideshow.getElementsByTagName("test2"))
#    slideshow.setAttribute('<test>','2')
#    slideshow.setIdAttribute('<test>')
    handleSlideshowTitle(slideshow.getElementsByTagName("title")[0])
    slides = slideshow.getElementsByTagName("slide")
    handleToc(slides)
    handleSlides(slides)
    print "</html>"


def handleSlides(slides):
    for slide in slides:
        handleSlide(slide)


def handleSlide(slide):
    handleSlideTitle(slide.getElementsByTagName("title")[0])
    handlePoints(slide.getElementsByTagName("point"))


def handleSlideshowTitle(title):
    print "<title>%s</title>" % getText(title.childNodes)


def handleSlideTitle(title):
    print "<h2>%s</h2>" % getText(title.childNodes)


def handlePoints(points):
    print "<ul>"
    for point in points:
        handlePoint(point)
    print "</ul>"


def handlePoint(point):
    print "<li>%s</li>" % getText(point.childNodes)


def handleToc(slides):
    for slide in slides:
        title = slide.getElementsByTagName("title")[0]
        print "<p>%s</p>" % getText(title.childNodes)


def t(ry):
	print "<?xml version='1.0' standalone='yes'?>"
	print "<rhythmdb version='1.7'>"
	es = ry.getElementsByTagName("entry")
	entrys(es)
	print "</rhythmdb>"


def entrys(es):
	for e in es:
		entry(e)


def leng(e,s):
	if e.getElementsByTagName(s).length > 0:
		return true
	return false


def p(e,s):
	temp = e.getElementsByTagName(s)[0]
	temp3 = getText(temp.childNodes)
	temp2 = "    <"+s+">"+temp3+"</"+s+">"
	print temp2


def entry(e):
	print "  <entry type='song'>"

	if leng(e,"title") > 0:
		p(e,"title")

	if leng(e,"genre") > 0:
		p(e,"genre")

	if leng(e,"artist") > 0:
		p(e,"artist")

	if leng(e,"album") > 0:
		p(e,"album")

	if leng(e,"track-number") > 0:
		p(e,"track-number")

	if leng(e,"disc-number")>0:
		p(e,"disc-number")

	if leng(e,"duration")>0:
		p(e,"duration")

	if leng(e,"file-size")>0:
		p(e,"file-size")

	if leng(e,"location")>0:
		p(e,"location")

	if leng(e,"mountpoint")>0:
		p(e,"mountpoint")

	if leng(e,"mtime")>0:
		p(e,"mtime")

	if leng(e,"first-seen")>0:
		p(e,"first-seen")

	if leng(e,"last-seen")>0:
		p(e,"last-seen")

	if leng(e,"rating")>0:
		p(e,"rating")

	if leng(e,"play-count")>0:
		if leng(e,"rating")>0:
			temp = e.getElementsByTagName("rating")[0]
			r = getText(temp.childNodes)
			r5 = r
			r5 = "5"
			r4 = r
			r4 = "4"
			r3 = r
			r3 = "3"
			r2 = r
			r2 = "2"
			if r==r5:
				print "    <play-count>50</play-count>"
			elif r==r4:
				print "    <play-count>25</play-count>"
			elif r==r3:
				print "    <play-count>3</play-count>"
			elif r==r2:
				print "    <play-count>2</play-count>"
			else:
				print "    <play-count>1</play-count>"
		else:
			p(e,"play-count")
	else:
		print "    <play-count>1</play-count>"

	if leng(e,"last-played")>0:
		p(e,"last-played")
	else:
		temp = e.getElementsByTagName("last-seen")[0]
		print "    <last-played>%s</last-played>" % getText(temp.childNodes)
		#print "    <last-played>1303150923</last-played>"

	if leng(e,"bitrate")>0:
		p(e,"bitrate")

	if leng(e,"date")>0:
		p(e,"date")

	if leng(e,"mimetype")>0:
		p(e,"mimetype")

	if leng(e,"comment")>0:
		p(e,"comment")

	if leng(e,"album-artist")>0:
		p(e,"album-artist")

	if leng(e,"beats-per-minute")>0:
		p(e,"beats-per-minute")

	print "  </entry>"

#handleSlideshow(dom)
t(dom)
#test(dom)
#t2(dom)
