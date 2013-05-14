import sys
import json



def dict_sentiments():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
		scores[term] = int(score)  # Convert the score to an integer.
	return scores


def main():
	scores = dict_sentiments()
	for key in scores.keys():
		key_phrase = "sentiments["+key+"]"
		print "\t",key_phrase, "=", scores[key]

if __name__ == '__main__':
    main()
