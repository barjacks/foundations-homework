import requests

#Finding the Artists
Favorite_Artists = input("What is your favorite Artist on Spotify? ")
#print(Favorite_Artists)

response = requests.get("https://api.spotify.com/v1/search?query=" + Favorite_Artists + "&type=artist&limit=50&market=US")
Favorite_Artists = response.json()

print('There are', Favorite_Artists['artists']['total'], 'Artists with that in their name. We are giong to print the top 20 for you.')

#printing our the list
Favorite_Artists_List = Favorite_Artists['artists']['items']
#numbering the list
artist_number = 0
artist_list_numbered = []
for artist in Favorite_Artists_List:
    artist_number = artist_number + 1
    print(artist_number, artist['name'])
    artist_list_numbered.append(artist['name'])
#print(artist_list_numbered)

#Which artist was the user looking for?
artist_number_input = input("Which artist were you looking for, please enter the correspondin number?")
artist_number_input = int(artist_number_input) - 1
#print(artist_list_numbered[artist_number_input])
artist = artist_list_numbered[artist_number_input]
print(artist)

#defining the aritsts ID
for n in Favorite_Artists_List:
    if n['name'] == artist:
        #print(n['name'], n['id'])
        artist_ID = n['id']

#importing the artist's data
response = requests.get("https://api.spotify.com/v1/artists/" + artist_ID + "/top-tracks?country=US")
Artist_data = response.json()

print("Here's a list of top tracks by the band or artist", artist)
for tracks in Artist_data['tracks']:
    print(tracks['name'])

#looking up the artist's top album
response = requests.get("https://api.spotify.com/v1/artists/" + artist_ID + "/albums?country=US")
Artist_album_data = response.json()

#print(Artist_album_data['items'])
print("Here's a list of", artist, "albums:")
for Album in Artist_album_data['items']:
    print(Album['name'], Album['id'])

#Getting 

#for artist in Lil_artists:
    #print("Comparing", artist['popularity'], 'to', most_popular_score)
#    if artist['popularity'] > most_popular_score:
#        print("checking for Lil Wayne")
#        if artist['name'] == 'Lil Wayne':
#            print('go away')
#        else:
        #The change you are keeping track of
        #a.k.a. what you are keeping track of
#            print('not Lil Wayne, updating our notebook')
#            most_popular_name = artist['name']
#            most_popular_score = artist['popularity']


#Establishing, whether we need to print out more?
#print('Is the artist you are looking for among these top 20? Please \
#type the full name below. If not, just retype your query being a little bit \
#more precise.')

#artist_number = 0
#artist_list_numbered = []
#for artist in Favorite_Artists_List:
#    artist_number = artist_number + 1
#    print(artist_number, artist['name'])
#    artist_list_numbered.append({artist_number: artist['name']})
#print(artist_list_numbered)


#Favorite_Artists = input("What is your favorite Artist on Spotify? ")
#print(Favorite_Artists)
