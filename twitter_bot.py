import tweepy
import openai
import random
import time
from keys.keys import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET, OPENAI_API_KEY

client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)

openai.api_key = OPENAI_API_KEY

tech_topics = [
    "JavaScript",
    "Python",
    "Artificial Intelligence",
    "Data Science",
    "Web Development",
    "Machine Learning",
    "Cybersecurity",
    "Blockchain",
    "Cloud Computing",
    "Internet of Things",
    "famous quotes"
]

rest_of_prompt_phrases = [
    "Tweet about",
    "Tweet with a tip about",
    "Tweet your thoughts on",
    "Highlight a tweet-worthy feature of",
    "Tweet a common challenge about",
    "Inspire others with a tweet about"
]

def generate_prompt():

    topic_index = random.randint(0, len(tech_topics) - 1)
    phrase_index = random.randint(0, len(rest_of_prompt_phrases) - 1)

    sentence = rest_of_prompt_phrases[phrase_index] + " " + tech_topics[topic_index]
    print(sentence)

    return sentence

def generate_tweet():
    personality_description = "You are a friendly tech enthusiast. "
    prompt = personality_description + generate_prompt()
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens = 68
    )
    return response.choices[0].text.strip()

tweet = generate_tweet()
print(tweet)
response = client.create_tweet(text=f'{tweet}')

