import os
import tweepy

class TwitterClient:
    def __init__(self):
        self.api_key = os.environ.get('TWITTER_API_KEY')
        self.api_secret = os.environ.get('TWITTER_API_SECRET_KEY')
        self.access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')
        self.client = None

    def authenticate(self):
        if not all([self.api_key, self.api_secret, self.access_token, self.access_token_secret]):
            raise ValueError("Missing Twitter API credentials. Please set all required environment variables.")
        
        # Use Client v2
        self.client = tweepy.Client(
            consumer_key=self.api_key,
            consumer_secret=self.api_secret,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def post_tweet(self, message):
        if not self.client:
            raise RuntimeError("Client not authenticated. Call authenticate() first.")
        try:
            response = self.client.create_tweet(text=message)
            return response
        except Exception as e:
            raise Exception(f"Failed to post tweet: {str(e)}") 