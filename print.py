import urllib
import json
import sys
print "The len of argument list is", len(sys.argv)

search_phrase = sys.argv[1]

urlstring = "http://search.twitter.com/search.json?q=" + search_phrase

#response = urllib.urlopen(urlstring)

#pyresponse = json.load(response)

for pagenum in range(10):
	response = urllib.urlopen(urlstring+"&page="+str(pagenum+1))
	pyresponse = json.load(response)
	for s in pyresponse["results"]:
		print s["text"].encode("utf-8")