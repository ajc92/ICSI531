import twitter, sys, json, os
reload(sys)
sys.setdefaultencoding("utf-8")
myApi=twitter.Api(consumer_key='PeH7lROp4ihy4QyK87FZg', \
                  consumer_secret='1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og', \
                  access_token_key='1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7', \
                  access_token_secret='e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw')

def query1():
	query = '(cold OR hot OR raining OR snowing OR humid OR freezing OR sunny) AND (outside OR now)'
	geo = ('40.735113', '-74.169009', '50mi') # Newark
	MAX_ID = None
	for it in range(45): # Retrieve up to 2250 tweets
		tweets = [json.loads(str(raw_tweet)) for raw_tweet \
		in myApi.GetSearch(query, geo, count = 50, max_id = MAX_ID, result_type='recent')]
	outfile = open('newark_tweets.txt', 'a')
        print len(tweets)
	for tweet in tweets:
		outfile.write(json.dumps(tweet['text']) + '\n\n')
	outfile.close()

def query2():
	query = '(sunny OR hot or humid OR breezy) AND (pool OR swimming OR hiking)'
	geo = ('40.735113', '-74.169009', '50mi')
	MAX_ID = None
	for it in range(45): # Retrieve up to 2250 tweets
		tweets = [json.loads(str(raw_tweet)) for raw_tweet \
		in myApi.GetSearch(query, geo, count = 50, max_id = MAX_ID, result_type='recent')]
	outfile = open('newark_tweets.txt', 'a')
	print len(tweets)
	for tweet in tweets:
		outfile.write(json.dumps(tweet['text']) + '\n\n')
	outfile.close()

def query3():
	query = '(cold OR cloudy or freezing OR bitter OR windy) AND (snow OR shoveling OR ice OR sleet)'
	geo = ('40.735113', '-74.169009', '50mi')
	MAX_ID = None
	for it in range(45): # Retrieve up to 2250 tweets
		tweets = [json.loads(str(raw_tweet)) for raw_tweet \
		in myApi.GetSearch(query, geo, count = 50, max_id = MAX_ID, result_type='recent')]
	outfile = open('newark_tweets.txt', 'a')
	print len(tweets)
	for tweet in tweets:
		outfile.write(json.dumps(tweet['text']) + '\n\n')
	outfile.close()

def query4():
	query = 'weather OR snowing OR sunny OR raining OR windy OR cloudy OR hot OR cold OR freezing OR humid'
	geo = ('40.735113', '-74.169009', '50mi')
	MAX_ID = None
	for it in range(45): # Retrieve up to 2250 tweets
		tweets = [json.loads(str(raw_tweet)) for raw_tweet \
		in myApi.GetSearch(query, geo, count = 50, max_id = MAX_ID, result_type='recent')]
	outfile = open('newark_tweets.txt', 'a')
	print len(tweets)
	for tweet in tweets:
		outfile.write(json.dumps(tweet['text']) + '\n\n')
	outfile.close()

def main():
        if not os.path.exists("tweets"):
		os.mkdir("tweets")
	os.chdir("tweets")
	query1()
	query2()
	query3()
	query4()
	pass

if __name__ == '__main__':
	main()
