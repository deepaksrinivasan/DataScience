'''Uses the twitter output file (output.txt as provided by problem 1) to compute and print top ten hashtags
Usage: python top_ten.py  <<twitter_filename>>
Note: For non-ascii, non-english fonts streaming from stdout to file not possible always.'''



import sys
import codecs
import json



def print_dict(dictionary):
	for key in dictionary.keys():
		print key, ':',dictionary[key]


def sort_dictionary(dictionary):
	return sorted(dictionary,key = dictionary.get,reverse = True)

	

def main():
	tweet_file = sys.argv[1]
	#fp = codecs.open(tweet_file,'r','utf-16')
	fp = open(tweet_file,'r')
	#print fp
	hashtags_dict = {}
	for tweet in fp:
		try:
			hashtag = json.loads(tweet)["entities"]["hashtags"][0]["text"]
			if not hashtag in hashtags_dict:
				hashtags_dict[hashtag] = 1
			else:
				hashtags_dict[hashtag] += 1
		except:	
			pass
	#print_dict(hashtags_dict)
	frequent_hashtags = sort_dictionary(hashtags_dict)
	#print type(frequent_hashtags)
	ten = 10
	for tag in frequent_hashtags[:ten]:
		print tag,' ',hashtags_dict[tag]
	




if __name__ == '__main__':
    main()
