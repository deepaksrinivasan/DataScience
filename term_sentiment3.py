'''This file computes the scores for previously undefined sentiments. The score function of a new sentiment is defined as in following
score(New_Sentiment | all tweets) = E(scores | scores >0 ^ New_Sentiment in tweet ) + E(scores | scores<0 ^ New_Sentiment in tweet)
where E(..) denotes the average. In essence, score of a previously undefined sentiment term is the sum of all scores of positive tweets containing the 
new term and all negtive scored tweets containing the new term.
Use case of the program is :
python term_sentiment.py new_sentiments_file.txt output.txt
where new_sentiments_file.txt is the txt file containing all the previously undefined sentiments one per line, output.txt is defined
as in problem 1. Make sure AFINN-111.txt is present as well in the current directory.

'''


import sys
import codecs
import json


sentiments = {}
## Parse the sentiments file to create a dictionary of scores and emotions
def dict_sentiments():
	global sentiments
	afinnfile = open("AFINN-111.txt")
	#global sentiments = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		sentiments[term] = int(score)  # Convert the score to an integer.
	return sentiments


# compute the sentiments score of a tweet. Retuens the sentiment words found in a tweet along with a cumulative score of a tweet
def sentiments_score_tweet(tweet_text):
	tweet_score = 0
	#slist_in_tweet = []
	for term in tweet_text.split():
		if sentiments.has_key(term):
			#slist_in_tweet.append(str(term))
			#sys.stdout.write(term)
			#sys.stdout.write(" : ")
			tweet_score += sentiments[term]
	return tweet_score





'''def main_1():
	dict_sentiments()
	print sentiments
	tweet_file = sys.argv[1]
	fp = codecs.open(tweet_file,'r','utf-16')
	for tweet in fp:
		try:
			tweet_text = json.loads(tweet)["text"]
			print sentiments_score_tweet(tweet_text)
		except:
			pass'''
	
	



def parse_all_tweets(fp):
	alltweet_texts = []
	for tweet in fp:
		try:
			alltweet_texts.append(json.loads(tweet)["text"])
		except:
			pass
	return alltweet_texts
			

def main():
	dict_sentiments()
	#print sentiments
	sent_file = sys.argv[1]
	tweet_file = sys.argv[2]
	sp = open(sent_file,'r')
	#fp = codecs.open(tweet_file,'r','utf-16')
	fp = open(tweet_file,'r')
	alltweet_texts = parse_all_tweets(fp)
	#print fp
	for line in sp:
		new_sentiment = line.strip('\n')
		#print 'searching', new_sentiment, type(new_sentiment)
		positive_tweets = []
		negative_tweets = []
		ave_postive_score = 0
		ave_negative_score = 0
		for tweet in alltweet_texts:
			#print tweet
			if new_sentiment in tweet:
				#print 'Found..',new_sentiment
				tweet_score = sentiments_score_tweet(tweet)
				if tweet_score > 0:
					positive_tweets.append(tweet_score)
				else:
					negative_tweets.append(tweet_score)
		#print positive_tweets, negative_tweets
		if positive_tweets != []:
			ave_postive_score = float(sum(positive_tweets))/len(positive_tweets)
		if negative_tweets != []:
			ave_negative_score = float(sum(negative_tweets))/len(negative_tweets)
		print new_sentiment,' ',ave_postive_score + ave_negative_score
			
			
					
				
	

if __name__ == '__main__':
    main()
	





