import cohere
import numpy as np

co = cohere.Client("c982jB7monS81SItzYsuCbRiM9KeGK4RhS3C75ZR")

# get the embeddings
phrases = ["I like"
           , "Join us for an unforgettable night of celebration! Our party promises an exhilarating atmosphere with a top-notch DJ spinning the latest hits, ensuring you dance the night away to your favorite tunes. We've got an open bar stocked with a variety of drinks, including beer, vodka, and cocktails to quench your thirst. The event starts at 9:00 PM and goes on until the break of dawn. For entry, it's just $20 at the door. Grab your friends and get ready to make memories that will last a lifetime."
           , "Get ready to groove at our upcoming beach party! We're serving up ice-cold beer and tropical cocktails to keep you refreshed as you enjoy the sunset. The party kicks off at 3:00 PM, so you'll have plenty of time to soak up the sun. The entry fee is only $15, and we're featuring live reggae music that will transport you to an island paradise. Don't miss out on the chance to dance in the sand and make waves with us!"
           , "It's time to rock and roll at our rock-themed bash! We're bringing the energy with beer, whiskey, and classic rock anthems. The event starts at 8:00 PM and goes on till the wee hours. Tickets are a steal at just $10. Our live band will be playing your favorite rock hits, so put on your leather jacket and join us for a night of headbanging and fun."
           , "The elegant masquerade ball is here! Sip on champagne and fine wine as you mingle with the city's elite. The party begins at 7:00 PM and lasts until midnight. It's a black-tie event with tickets priced at $100, but the memories you'll create are worth every penny. We've got a live jazz band that will serenade you throughout the evening, making it an event to remember."
           , "Dive into the Caribbean spirit at our tropical luau! We've got piña coladas, mai tais, and fruity punches that'll make you feel like you're on a Hawaiian island. The fun starts at 5:00 PM, so arrive early to enjoy the beach vibes. Tickets are just $25. Our DJ will be playing reggae and calypso beats, setting the mood for a night of dancing and limbo."
           , "Celebrate the holidays with us at our Christmas party! We'll have mulled wine, eggnog, and a variety of seasonal cocktails to keep you warm. The festivities begin at 6:00 PM and continue until midnight. Entry is free, so you can spend your money on gifts. We've got a live orchestra playing classic holiday tunes to put you in the spirit."
           , "Step into the future at our neon-themed rave! We've got glowing cocktails and futuristic shots to keep you energized all night long. The party starts at 10:00 PM and goes until the sun comes up. Tickets are $30, but the experience is priceless. Our DJ will be spinning electronic dance music, providing the perfect backdrop for a night of neon lights and high-energy dancing."
           , "Unleash your inner cowboy at our Western hoedown! Sip on bourbon, whiskey, and cold beer as you two-step the night away. The event kicks off at 7:00 PM and continues until the cows come home. Tickets are $15 and include line dancing lessons. We've got a live country band that'll play all your favorite country hits, so grab your boots and join us for a rootin' tootin' good time."
           , "Embrace the glamour at our Hollywood-themed soirée! Enjoy champagne, cocktails, and mocktails as you walk the red carpet. The party starts at 8:00 PM and goes until 2:00 AM. Tickets are $50, but you'll feel like a star. Our live jazz ensemble will create the perfect ambiance for an evening of glitz and glam."
           , "It's time to fiesta at our Mexican-themed party! We've got tequila, margaritas, and cerveza to keep the celebration going. The event begins at 6:00 PM and lasts until late into the night. Tickets are $20 and include a taco bar. Our mariachi band will provide lively music that will transport you to the heart of Mexico for a night of dancing and revelry."]
(soup1, soup2, soup3, soup4, soup5, soup6, soup7, soup8, soup9, soup10) = co.embed(phrases).embeddings

# compare them
def calculate_similarity(a, b):
  return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

print(calculate_similarity(soup1, soup2))
print(calculate_similarity(soup1, soup3)) 
print(calculate_similarity(soup1, soup4)) 
print(calculate_similarity(soup1, soup5)) 
print(calculate_similarity(soup1, soup6)) 
print(calculate_similarity(soup1, soup7)) 
print(calculate_similarity(soup1, soup8)) 
print(calculate_similarity(soup1, soup9)) 
print(calculate_similarity(soup1, soup10)) 