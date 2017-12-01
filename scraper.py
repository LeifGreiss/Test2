import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
import lxml.html 
root = lxml.html.fromstring(html)#turnourHTMLintoanlxmlobject 
tds = root.cssselect('td')#getallthe<tdtags
for td in tds:
    print td.text
for td in tds:
    record = { "td" : td.text_content() } # column name and value try:
    try:
        scraperwiki.sqlite.save(["td"], record) # save the records one by one 
    except:
        record = { "td" : "NO ENTRY" } # column name and value 
        scraperwiki.sqlite.save(["td"], record) # save the records one by one
