import scraperwiki
html = scraperwiki.scrape('https://en.wikipedia.org/wiki/List_of_British_racecourses')
import lxml.html 
root = lxml.html.fromstring(html)#turnourHTMLintoanlxmlobject 
tds = root.cssselect('td')#getallthe<tdtags
for td in tds:
    print td.text_content()
for td in tds:
    record = { "td" : td.text_content() } # column name and value try:
    scraperwiki.sqlite.save(["td"], record)
    #try:
        #scraperwiki.sqlite.save(["td"], record) # save the records one by one 
    #except:
        #record = { "td" : "NO ENTRY" } # column name and value 
        #scraperwiki.sqlite.save(["td"], record) # save the records one by one
