import scraperwiki
html = scraperwiki.scrape('http://inmo.ie/6022')
print "Click on the ...more link to see the whole page"
import lxml.html
root = lxml.html.fromstring(html) # turn our HTML into an lxml object
tds = root.cssselect('td') # get all the <td> tags
for td in tds:
    record = { "td" : td.text } # column name and values
    try: 
        scraperwiki.sqlite.save(["td"], record)
    except:
        record = {"td" : "NO ENTRY" }
        scraperwiki.sqlite.save(["td"], record)
