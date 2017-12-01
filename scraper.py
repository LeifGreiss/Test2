import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
importlxml.html 
root=lxml.html.fromstring(html)#turnourHTMLintoanlxmlobject tds=root.cssselect('td')#getallthe<tdtags
for td in tds:
    record = { "td" : td.text } # column name and value try:
    try:
        scraperwiki.sqlite.save(["td"], record) # save the records one by one 
    except:
        record = { "td" : "NO ENTRY" } # column name and value 
        scraperwiki.sqlite.save(["td"], record) # save the records one by one
