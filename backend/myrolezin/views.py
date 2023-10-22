from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MyRolezinSerializer
from .models import MyRolezin
from rest_framework.decorators import api_view
from django.http import HttpResponse
import json
import cohere
import numpy as np

# Create your views here.

class MyRolezinView(viewsets.ModelViewSet):
    serializer_class = MyRolezinSerializer
    queryset = MyRolezin.objects.all()




@api_view(['GET'])
def filter(request):
    co = cohere.Client("c982jB7monS81SItzYsuCbRiM9KeGK4RhS3C75ZR")

    #Client information from the form
    drink_type = request.GET.get('drink', None)
    start_time = request.GET.get('hour', None)
    price = request.GET.get('price', None)
    music_type = request.GET.get('music', None)
    

    # get the embeddings
    phrases = [f"I like driking {drink_type}. The begin time could be anytime after {start_time}, when the night comes alive. As for the price, I prefer to pay around ${price}. And when I'm sipping my {drink_type}, I enjoy some {music_type} playing in the background, setting the mood just right."
            , "Join us for an unforgettable night of celebration! Our party promises an exhilarating atmosphere with a top-notch DJ spinning the latest hits, ensuring you dance the night away to your favorite tunes. We've got an open bar stocked with a variety of drinks, including beer, vodka, and cocktails to quench your thirst. The event starts at 9:00 PM and goes on until the break of dawn. For entry, it's just $20 at the door. Grab your friends and get ready to make memories that will last a lifetime."
            , "Get ready to groove at our upcoming beach party! We're serving up ice-cold beer and tropical cocktails to keep you refreshed as you enjoy the sunset. The party kicks off at 3:00 PM, so you'll have plenty of time to soak up the sun. The entry fee is only $15, and we're featuring live reggae music that will transport you to an island paradise. Don't miss out on the chance to dance in the sand and make waves with us!"
            , "It's time to rock and roll at our rock-themed bash! We're bringing the energy with beer, whiskey, and classic rock anthems. The event starts at 8:00 PM and goes on till the wee hours. Tickets are a steal at just $10. Our live band will be playing your favorite rock hits, so put on your leather jacket and join us for a night of headbanging and fun."
            , "The elegant masquerade ball is here! Sip on champagne and fine wine as you mingle with the city's elite. The party begins at 7:00 PM and lasts until midnight. It's a black-tie event with tickets priced at $100, but the memories you'll create are worth every penny. We've got a live jazz band that will serenade you throughout the evening, making it an event to remember."
            , "Dive into the Caribbean spirit at our tropical luau! We've got piña coladas, mai tais, and fruity punches that'll make you feel like you're on a Hawaiian island. The fun starts at 5:00 PM, so arrive early to enjoy the beach vibes. Tickets are just $25. Our DJ will be playing reggae and calypso beats, setting the mood for a night of dancing and limbo."
            , "Celebrate the holidays with us at our Christmas party! We'll have mulled wine, eggnog, and a variety of seasonal cocktails to keep you warm. The festivities begin at 6:00 PM and continue until midnight. Entry is free, so you can spend your money on gifts. We've got a live orchestra playing classic holiday tunes to put you in the spirit."
            , "Step into the future at our neon-themed rave! We've got glowing cocktails and futuristic shots to keep you energized all night long. The party starts at 10:00 PM and goes until the sun comes up. Tickets are $30, but the experience is priceless. Our DJ will be spinning electronic dance music, providing the perfect backdrop for a night of neon lights and high-energy dancing."
            , "Unleash your inner cowboy at our Western hoedown! Sip on bourbon, whiskey, and cold beer as you two-step the night away. The event kicks off at 7:00 PM and continues until the cows come home. Tickets are $15 and include line dancing lessons. We've got a live country band that'll play all your favorite country hits, so grab your boots and join us for a rootin' tootin' good time."
            , "Embrace the glamour at our Hollywood-themed soirée! Enjoy champagne, cocktails, and mocktails as you walk the red carpet. The party starts at 8:00 PM and goes until 2:00 AM. Tickets are $50, but you'll feel like a star. Our live jazz ensemble will create the perfect ambiance for an evening of glitz and glam."
            , "It's time to fiesta at our Mexican-themed party! We've got tequila, margaritas, and cerveza to keep the celebration going. The event begins at 6:00 PM and lasts until late into the night. Tickets are $20 and include a taco bar. Our mariachi band will provide lively music that will transport you to the heart of Mexico for a night of dancing and revelry."
            , "Imagine a vibrant and exciting party where the atmosphere is electrified by the choice of drinks. You can quench your thirst with ice-cold beer or enjoy the smoothness of vodka-based cocktails. As the clock strikes 8 PM, the party begins, setting the stage for a night of revelry. What makes it even better is that the prices of drinks are quite affordable, ranging from $5 to $12. The music choice for this gathering is a blend of hiphop and R&B, creating a rhythm that encourages everyone to hit the dance floor."
            , "A great party is all about variety. This one features an array of drink options, from craft beer to creative vodka concoctions. Starting at 9 PM, the night is filled with excitement and anticipation. The prices are reasonable, with drinks ranging from $7 to $15, ensuring that everyone can join in on the fun. The sound system is pumping out reggae tunes that make you feel like you're on an island getaway, setting the perfect mood for a tropical-themed bash."
            , "The heart of this fantastic party is the fantastic drink selection. From the frothy goodness of beer to the elegance of vodka, there's something for every taste. As the clock strikes 10 PM, the party comes alive, and the energy is contagious. The drink prices are budget-friendly, ranging from $6 to $14, making sure no one breaks the bank. Funk music rules the night, setting a groovy tone that gets everyone moving to the rhythm."
            , "An unforgettable party comes to life with a diverse drink menu. Guests can enjoy the rich flavors of beer, take shots of vodka, or sip on signature cocktails. Starting at 8:30 PM, the party thrives with excitement and a sense of community. Drink prices range from $7 to $18, allowing for a range of options that accommodate different budgets. The night's soundtrack is a blend of electronic dance music (EDM), creating an energetic atmosphere that's impossible to resist."
            , "When it comes to an epic party, the choice of drinks is crucial. From beer to vodka to an array of specialty cocktails, there's no shortage of options. As the clock strikes 9:30 PM, the party begins with an infectious buzz. The drink prices are competitive, ranging from $8 to $16, making it an inclusive celebration. The music selection includes classic rock and pop, ensuring that everyone can sing along and dance the night away."
            ]
    names = [
    "Neon Glow Rave Extravaganza",
    "Tropical Luau Paradise",
    "Retro Disco Fever Bash",
    "Carnival of Colors",
    "Under the Stars Soiree",
    "Casino Night Gala",
    "Enchanted Garden Fête",
    "Masquerade Masquerave",
    "Space Odyssey: A Cosmic Celebration",
    "Pirate's Plunder: Swashbuckling Shindig",
    "Electric Jungle Jam",
    "Mystic Moonlit Masquerade",
    "Beach Bonfire Bliss",
    "Midnight Masquerade Ball",
    "Galactic Groove Odyssey"
    ]

    namesDictionary = {}
    # fill names dict
    for i in range(len(names)):
        namesDictionary[phrases[i+1]] = names[i]

    

    soupVector = co.embed(phrases).embeddings

    # compare them
    def calculate_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

    max = 0
    aux_i = 0 

    similarityV = []

    for i in range(len(soupVector) - 1):
        aux = calculate_similarity(soupVector[0], soupVector[i + 1])
        similarityV.append(aux)
        # if aux > max:
        # max = aux
        # aux_i = i
        
    sorted_indices_descending = np.argsort(similarityV)[::-1]
    print(sorted_indices_descending)

    output = []
    #create output dict
    for i in range(len(names)):
        index = sorted_indices_descending[i]
        print(index)
        output.append({'name': namesDictionary[phrases[index+1]], 'description': phrases[index+1], 'score': similarityV[index]})


    # Use json.dumps para serializar o dicionário em JSON
    output_json = json.dumps(output)

    # Retorne uma resposta JSON
    return HttpResponse(output_json, content_type='application/json')