import codecs, json

fp = codecs.open('output.txt','r','utf-16')

for tweet in fp:
	try:
		print json.loads(tweet)["text"]
	except:
		pass
