import tweepy
import requests
import json

# Authentification Twitter
consumer_key = "Votre Consumer Key"
consumer_secret = "Votre Consumer Secret"
access_token = "Votre Access Token"
access_token_secret = "Votre Access Token Secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Connexion à l'API Twitter
api = tweepy.API(auth)

# Écoute des nouveaux tweets
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Envoi du message au webhook Discord
        webhook_url = "https://discord.com/api/webhooks/XXXXX/XXXXXXXXXX" # Remplacez XXXXX par l'ID de votre webhook et XXXXXXXXXX par son jeton
        data = {
            "content": f"**{status.user.screen_name}** a tweeté : {status.text}"
        }
        response = requests.post(webhook_url, data=json.dumps(data), headers={"Content-Type": "application/json"})

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['mot-clé']) # Remplacez "mot-clé" par le mot-clé que vous souhaitez écouter
