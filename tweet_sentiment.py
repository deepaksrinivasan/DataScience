'''Uses the sentiment file and twitter output file (output.txt as provided by problem 1) to provide sentiment score for every tweet
Usage: python tweet_sentiment.py <<sentiment_filename>> <<twitter_filename>>'''


import sys
import codecs
import json


## Return the file contents. Not used in the current program. To be used when the twitter file has already been parsed nicely into text sentences.
def lines(fp):
	tweetfeed = codecs.open(fp,'r','utf-16')
	return tweetfeed.readlines()


## Parse the sentiments file to create a dictionary of scores and emotions
def dict_sentiments(fp):
	afinnfile = open(fp)
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	return scores


	


# compute the sentiments score of a tweet. Retuens the sentiment words found in a tweet along with a cumulative score of a tweet
def sentiments_scores_intweet(tweet_text,sentiments):
	tweet_score = 0
	slist_in_tweet = []
	for term in tweet_text.split():
		if sentiments.has_key(term):
			slist_in_tweet.append(str(term))
			#sys.stdout.write(term)
			#sys.stdout.write(" : ")
			tweet_score += sentiments[term]
	return slist_in_tweet, tweet_score
	
				


def main():
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
	sentiments = dict_sentiments(sent_file)
	fp = open(tweet_file,'r')
	#fp = codecs.open(tweet_file,'r','utf-16')
	#print fp
	for tweet in fp:
		try:
			tweet_text = json.loads(tweet)["text"]
			slist_in_tweet,tweet_score = sentiments_scores_intweet(tweet_text,sentiments)
			print float(tweet_score)
		except:
			pass
					
				
	

if __name__ == '__main__':
    main()
