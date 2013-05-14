'''Uses the twitter output file (output.txt as provided by problem 1) to compute frequency of terms occuring in tweet
Usage: python frequency.py  <<twitter_filename>>
Note: data quite noisy'''



import sys
import codecs
import json

def main():
	tweet_file = sys.argv[1]
	#fp = codecs.open(tweet_file,'r','utf-16')
	fp = open(tweet_file,'r')
	#print fp
	terms_list = []
	term_freq_dict = {}
	for tweet in fp:
		try:
			tweet_text = json.loads(tweet)["text"]
			#print tweet_text
			for term in tweet_text.split():
				if not term in terms_list :
					terms_list.append(str(term))
					#sys.stdout.write(term)
					#sys.stdout.write(" : ")
					term_freq_dict[term] = 1
				else:
					term_freq_dict[term] += 1
		except:
			pass
		#print term_freq_dict
	#print terms_list
	total_term_counts = sum(term_freq_dict.values())
	#[(print term,':',term_freq_dict[term]/float(total_term_counts)) for term in term_freq_dict.keys()]
	for term in term_freq_dict.keys():
		print term, ' ', term_freq_dict[term]/float(total_term_counts)


if __name__ == '__main__':
    main()
				
