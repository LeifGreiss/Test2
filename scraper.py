import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
tds = root.cssselect('tr') # get all the <td> tags
for tr in trs:
    record = { "tr" : tr.text } # column name and values
    try: 
        scraperwiki.sqlite.save(["tr"], record)
    except:
        record = {"tr" : "NO ENTRY" }
        scraperwiki.sqlite.save(["td"], record)
