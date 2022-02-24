# Import necessary libraries
import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient

# Connect to API through subscription key and endpoint
subscription_key = "17666311c45f4ac9b2bfbf59ec7b479f"
endpoint = "https://cogser-pbi.cognitiveservices.azure.com/"

# Authenticate
credential = AzureKeyCredential(subscription_key)
cog_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

# Get reviews
reviews_folder = 'reviews'

for file_name in os.listdir(reviews_folder):
    # Read the file contents
    print('\n-------------\n' + file_name)
    text = open(os.path.join(reviews_folder, file_name), encoding='utf8').read()
    print('\n' + text)

    # Get key phrases
    phrases = cog_client.extract_key_phrases(documents=[text])[0].key_phrases
    if len(phrases) > 0:
        print("\nKey Phrases:")
        for phrase in phrases:
            print('\t{}'.format(phrase))

    # Get sentiment
    sentimentAnalysis = cog_client.analyze_sentiment(documents=[text])[0]
    print("\nSentiment: {}".format(sentimentAnalysis.sentiment))
