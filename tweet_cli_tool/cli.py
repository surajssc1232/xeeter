import argparse
from .twitter.client import TwitterClient

def main():
    parser = argparse.ArgumentParser(description='A simple CLI tool to post tweets.')
    parser.add_argument('message', type=str, help='The message to tweet')
    
    args = parser.parse_args()
    
    twitter_client = TwitterClient()
    twitter_client.authenticate()
    twitter_client.post_tweet(args.message)
    print(f'Tweeted: {args.message}')

if __name__ == '__main__':
    main() 