import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
import lxml.html 
root = lxml.html.fromstring(html)#turnourHTMLintoanlxmlobject 
trs = root.cssselect('tr')#getallthe<tdtags
for tr in trs:
    print tr.text_content()
for tr in trs:
    record = { "tr" : tr.text_content() } # column name and value try:
    scraperwiki.sqlite.save(["tr"], record)
    #try:
        #scraperwiki.sqlite.save(["td"], record) # save the records one by one 
    #except:
        #record = { "td" : "NO ENTRY" } # column name and value 
        #scraperwiki.sqlite.save(["td"], record) # save the records one by one
