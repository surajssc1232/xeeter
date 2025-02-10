class TwitterClient:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        import tweepy
        
        self.auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
        self.api = tweepy.API(self.auth)

    def post_tweet(self, message):
        try:
            self.api.update_status(message)
            print("Tweet posted successfully!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def authenticate(self):
        # This method can be used to verify the authentication
        try:
            self.api.verify_credentials()
            print("Authentication OK")
        except Exception as e:
            print(f"Authentication failed: {e}")