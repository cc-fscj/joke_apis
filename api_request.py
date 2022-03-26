#!/usr/bin/env python3

#Colin Coyne

#Import modules
import requests

#Constants
ADDRESS = 'https://icanhazdadjoke.com/'
PAYLOAD = {}
HEADER = {
    'Accept' : 'application/json'
}

#Form API request
joke = requests.request('GET',ADDRESS,headers=HEADER,data=PAYLOAD)

#Format request in JSON
joke_json = joke.json()

#Print joke
print("Joke: " + str(joke_json['joke']))
